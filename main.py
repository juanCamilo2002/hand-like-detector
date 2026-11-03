from pathlib import Path
from time import monotonic_ns
from math import hypot

import cv2
import mediapipe as mp


def count_raised_fingers(landmark):
    count = 0

    # For the thumb, we compare distances relative to the base of the little finger.
    thumb_tip = landmark[4]
    thumb_joint = landmark[3]
    pinky_base = landmark[17]

    thumb_tip_distance = (
        (thumb_tip.x - pinky_base.x) ** 2 
        + (thumb_tip.y - pinky_base.y) ** 2
    )
    thumb_joint_distance = (
        (thumb_joint.x - pinky_base.x) ** 2
        + (thumb_joint.y - pinky_base.y) ** 2
    )

    if (thumb_tip_distance > thumb_joint_distance):
        count += 1

    # Index, middle, ring, and little fingers: tip above the joint.
    for tip, joint in [(8, 6), (12, 10), (16, 14), (20, 18)]:
        if landmark[tip].y < landmark[joint].y:
            count += 1

    return count

def detect_gesture(landmarks):
    wrist = landmarks[0]

    # A finger is considered bent if its tip is closer to the
    # wrist than its middle joint.
    for tip_index, joint_index in [(8, 6), (12, 10), (16, 14), (20, 18)]:
        tip = landmarks[tip_index]
        joint = landmarks[joint_index]

        tip_distance = (tip.x - wrist.x) ** 2 + (tip.y - wrist.y) ** 2
        joint_distance = (joint.x - wrist.x) ** 2 + (joint.y - wrist.y) ** 2

        if tip_distance >= joint_distance:
            return None


    thumb_tip = landmarks[4]
    thumb_joint = landmarks[3]
    thumb_base = landmarks[2]

    if thumb_tip.y < thumb_joint.y < thumb_base.y:
        return "Like"

    if thumb_tip.y > thumb_joint.y > thumb_base.y:
        return "Dislike"

    return None



def main():
    model_path = Path(__file__).parent / "hand_landmarker.task"

    if not model_path.is_file():
        print(f"Error: no se encontró el modelo en {model_path}")
        return

    options = mp.tasks.vision.HandLandmarkerOptions(
        base_options=mp.tasks.BaseOptions(model_asset_path=str(model_path)),
        running_mode=mp.tasks.vision.RunningMode.VIDEO,
        num_hands=1,
    )

    with mp.tasks.vision.HandLandmarker.create_from_options(options) as landmarker:
        camera = cv2.VideoCapture(0)
        
        if not camera.isOpened():
            camera.release()
            print("Error: no se pudo abrir la cámara")
            return

        previous_timestamp = -1
        canvas = None
        previous_point = None
        
        try:
            while True:
                success, frame = camera.read()
        
                if not success:
                    print("Error: no se pudo leer la imagen de la cámara.")
                    break

                frame = cv2.flip(frame, 1)
                rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)

                # Each image requires a timestamp greater than the previous one.
                timestamp = max(monotonic_ns() // 1_000_000, previous_timestamp + 1)
                previous_timestamp = timestamp

                result = landmarker.detect_for_video(image, timestamp)

                height, width = frame.shape[:2]

                if canvas is None or canvas.shape != frame.shape:
                    canvas = frame.copy()
                    canvas[:] = 0
                    previous_point = None

                if not result.hand_landmarks:
                    previous_point = None

                for hand_landmarks in result.hand_landmarks:
                    for landmark in hand_landmarks:
                        x = int(landmark.x * width)
                        y = int(landmark.y * height)
                        cv2.circle(frame, (x, y), 5, (0, 255, 0), -1)

                    finger_count = count_raised_fingers(hand_landmarks)

                    cv2.putText(
                        frame,
                        f"Dedos: {finger_count}",
                        (20, 40),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1,
                        (0, 255, 0),
                        2,
                    )

                    gesture = detect_gesture(hand_landmarks)

                    if gesture is not None:
                        cv2.putText(
                            frame,
                            f"Gesto: {gesture}",
                            (20, 80),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            1,
                            (0, 255, 0),
                            2,
                        )

                    index_tip = hand_landmarks[8]
                    thumb_tip = hand_landmarks[4]
                    wrist = hand_landmarks[0]
                    middle_base = hand_landmarks[9]

                    index_point = (
                        int(index_tip.x * width),
                        int(index_tip.y * height),
                    )

                    pinch_distance = hypot(
                        (index_tip.x - thumb_tip.x) * width,
                        (index_tip.y - thumb_tip.y) * height,
                    )

                    hand_size = hypot(
                        (wrist.x - middle_base.x) * width,
                        (wrist.y - middle_base.y) * height,
                    )

                    if hand_size > 0 and pinch_distance < hand_size * 0.4:
                        if previous_point is not None:
                            cv2.line(
                                canvas,
                                previous_point,
                                index_point,
                                (255, 0, 255),
                                4,
                            )

                        previous_point = index_point
                    else:
                        previous_point = None
        
                mask = cv2.cvtColor(canvas, cv2.COLOR_BGR2GRAY)
                frame[mask > 0] = canvas[mask > 0]

                cv2.imshow("Hand Like Detector", frame)

        
                key = cv2.waitKey(1) & 0xFF

                if key == ord("q"):
                    break
                if key == ord("c"):
                    canvas[:] = 0
                    previous_point = None
        finally:
            camera.release()
            cv2.destroyAllWindows()



if __name__ == "__main__":
    main()