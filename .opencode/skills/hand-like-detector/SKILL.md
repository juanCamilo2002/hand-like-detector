---
name: hand-like-detector
description: Guía el desarrollo paso a paso de un proyecto Python para detectar manos, contar dedos y reconocer gestos con la cámara.
---

# Hand Like Detector

## Objetivo

Desarrollar un sistema que use la cámara del PC para:

- Detectar una mano.
- Contar los dedos levantados.
- Reconocer los gestos de like y dislike.
- Mostrar al menos una palabra en pantalla. Acordar con el usuario cómo se elige o escribe esa palabra antes de implementar esta funcionalidad.

## Tecnologías

- Usar Python como lenguaje principal.
- Emplear bibliotecas para acceder a la cámara, procesar imágenes y reconocer manos. OpenCV y MediaPipe son opciones propuestas, sujetas a revisión de compatibilidad y acuerdo con el usuario.
- Mantener las soluciones sencillas y adecuadas a la etapa actual del proyecto.
- Empezar con OpenCV para cámara, imágenes y texto, y MediaPipe para localizar los puntos de la mano. Confirmar versiones compatibles de Python y de las bibliotecas antes de instalarlas.
- Usar `venv` para el entorno virtual y `pip` con `requirements.txt` para las dependencias, sin añadir herramientas hasta que hagan falta.

## Estructura inicial propuesta

```text
hand-like-detector/
├── .opencode/skills/hand-like-detector/SKILL.md
├── .gitignore
├── README.md
├── requirements.txt
└── main.py
```

- `main.py`: punto de entrada y lógica inicial de la aplicación.
- `requirements.txt`: dependencias externas necesarias.
- `README.md`: instrucciones de instalación, ejecución y uso.
- `.gitignore`: excluir el entorno virtual y archivos generados de Python si se usa Git.
- Crear módulos o carpetas adicionales solo cuando una funcionalidad o complejidad real lo justifique; la estructura es una propuesta, no implica que los archivos ya existan.

## Estilo de desarrollo

- Priorizar código limpio, legible y mantenible, sin sobreingeniería.
- Usar nombres descriptivos, funciones pequeñas con responsabilidades claras y convenciones habituales de Python (PEP 8).
- Evitar clases, patrones, capas, configuraciones y dependencias innecesarias; preferir la solución más sencilla que cumpla la necesidad actual.
- Evaluar cada nueva funcionalidad antes de introducir abstracciones o reorganizar el proyecto. Refactorizar cuando exista una necesidad concreta.
- Gestionar los errores relevantes, especialmente el acceso a la cámara, y liberar los recursos al finalizar.
- Verificar cada avance con una prueba apropiada, inicialmente manual cuando sea suficiente; añadir pruebas automatizadas cuando aporten valor.

## Forma de trabajo

- Comunicarse en español y avanzar en pasos pequeños y comprensibles.
- Proporcionar al usuario el código y las instrucciones necesarias para cada paso; el usuario lo implementa y ejecuta.
- Explicar brevemente qué hace el código, cómo ejecutarlo y qué resultado esperar.
- Esperar los resultados o dudas del usuario antes de avanzar al siguiente paso; ayudar a diagnosticar errores cuando aparezcan.
- No modificar archivos del proyecto ni ejecutar la implementación por cuenta propia, salvo que el usuario lo solicite explícitamente.
- Proponer decisiones técnicas cuando sean necesarias sin dar por acordados detalles que el usuario no haya definido.
