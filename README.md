# Hand Like Detector

Aplicación en Python que utiliza la cámara del PC para detectar una mano,
contar los dedos levantados, reconocer gestos y dibujar en pantalla.

## Funcionalidades

- Detectar una mano y mostrar sus puntos de referencia.
- Contar los dedos levantados.
- Reconocer los gestos de like y dislike.
- Dibujar en pantalla juntando el pulgar y el índice.
- Mostrar la imagen de la cámara en vista de espejo.

El dibujo permite escribir palabras a mano, pero la aplicación no reconoce
las letras ni las convierte en texto.

## Tecnologías

- Python
- OpenCV
- MediaPipe

La aplicación se ha probado con Python 3.13.3 y MediaPipe 1.2.0.

## Instalación en Windows

Ejecuta los siguientes comandos desde la carpeta del proyecto.

### 1. Crear el entorno virtual

Si todavía no existe:

```powershell
python -m venv venv
```

### 2. Instalar las dependencias

```powershell
.\venv\Scripts\python.exe -m pip install -r requirements.txt
```

### 3. Descargar el modelo de detección

Si `hand_landmarker.task` todavía no está en la carpeta del proyecto:

```powershell
Invoke-WebRequest -Uri "https://storage.googleapis.com/mediapipe-models/hand_landmarker/hand_landmarker/float16/1/hand_landmarker.task" -OutFile "hand_landmarker.task"
```

El archivo debe quedar junto a `main.py`.

## Ejecución

```powershell
.\venv\Scripts\python.exe main.py
```

## Controles

- **Dibujar:** juntar el pulgar y el índice y mover la mano.
- **Detener el trazo:** separar el pulgar y el índice.
- **C:** borrar el dibujo.
- **Q:** cerrar la aplicación.

Para usar las teclas, selecciona primero la ventana de la cámara.

## Limitaciones

El conteo de dedos y el reconocimiento de gestos son aproximados. Pueden
fallar según la posición de la mano, la iluminación o si algunos puntos
quedan ocultos.
