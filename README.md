# 🧠🎴 Oblique Strategies para Badger2040

Versión digital en español del mazo artístico creado por Brian Eno y Peter Schmidt, adaptada a la pantalla e-paper del Badger2040. Este mazo, conocido como "Estrategias Oblicuas", fue concebido como una herramienta para desbloquear la creatividad mediante frases enigmáticas, provocadoras o paradójicas.

Presiona un botón en tu Badger2040 y recibe una frase aleatoria para inspirarte cuando sientas bloqueo creativo.

> “Solo en caso de bloqueo absoluto. Toma una carta. Solo una. Acéptala sin cuestionar. Y continúa.”

## 📂 Estructura del proyecto

Este proyecto está diseñado para integrarse con BadgerOS. Los archivos deben colocarse directamente en la carpeta `apps/`, **no dentro de una subcarpeta**. También es necesario **modificar el archivo `launcher.py`** para que apunte a `apps/` en lugar de `examples/`.

```
apps/
├── Oblique.py
├── icon-Oblique.png
```

## 🛠️ Requisitos
- Pimoroni Badger2040
- Thonny IDE
- MicroPython
- PicoGraphics
- Sistema BadgerOS modificado:
  - Carpeta `/apps/` creada en el dispositivo
  - `launcher.py` actualizado para leer desde `/apps/`

## ✍️ Autor
Luis Raúl González Romo – [@luisgonzalez98](https://www.linkedin.com/in/luis-raul-gonzalez-romo/)

## 📄 Licencia
MIT
