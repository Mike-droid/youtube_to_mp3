# YouTube to MP3

Script sencillo en Python que descarga el audio de un video de YouTube y lo convierte automáticamente a formato `.mp3`.

El programa solicita:

1. La URL del video de YouTube.
2. El nombre que tendrá el archivo MP3 final.

El audio se descarga temporalmente en formato `.webm`, posteriormente se convierte a MP3 utilizando FFmpeg y, si la conversión termina correctamente, el archivo `.webm` temporal se elimina.

## Requisitos

* Python 3
* FFmpeg
* `yt-dlp`

El proyecto fue desarrollado y probado utilizando **Ubuntu mediante WSL**.

## Instalación

Clona el repositorio:

```bash
git clone https://github.com/Mike-droid/youtube_to_mp3
cd youtube_to_mp3
```

Crea y activa un entorno virtual:

```bash
python3 -m venv .venv
source ./venv/bin/activate
```

Instala las dependencias del entorno virtual de Python:

```bash
pip install -r requirements.txt
```

Instala FFmpeg en Ubuntu:

```bash
sudo apt update
sudo apt install ffmpeg
```

Puedes comprobar que todo esté instalado correctamente:

```bash
python --version
yt-dlp --version
ffmpeg -version
```

## Uso

Ejecuta el script:

```bash
python3 src/main.py
```

El programa solicitará la URL del video y el nombre del archivo:

```text
URL de YouTube: https://www.youtube.com/watch?v=XXXXXXXX
Nombre del archivo: Mi_audio
```

El archivo resultante se guardará dentro de la carpeta `downloads`:

```text
downloads/
└── Mi_audio.mp3
```

## ¿Cómo funciona?

El proceso es el siguiente:

```text
YouTube
   │
   ▼
yt-dlp
   │
   ▼
audio.webm
   │
   ▼
FFmpeg
   │
   ▼
audio.mp3
   │
   ▼
Eliminar .webm temporal
```

`yt-dlp` se encarga de descargar el mejor stream de audio disponible.

Posteriormente, FFmpeg convierte el archivo `.webm` a `.mp3` utilizando una calidad de **192 kbps**.

El archivo `.webm` temporal solamente se elimina después de que FFmpeg termina la conversión correctamente. Si ocurre algún error durante la conversión, el archivo original se conserva.

## Estructura del proyecto

```text
.
├── src/main.py && src/downloads/
└── README.md
```

La carpeta `downloads/` se crea automáticamente cuando se ejecuta el programa.

## Características

* Descarga el audio de un video de YouTube.
* Convierte automáticamente el audio a MP3.
* Permite elegir el nombre del archivo.
* Guarda los archivos en una carpeta `downloads`.
* Elimina automáticamente el archivo `.webm` temporal después de una conversión exitosa.
* Utiliza un entorno virtual de Python para aislar las dependencias.

## Notas

Este es un proyecto personal diseñado para realizar una tarea específica de manera sencilla: obtener un archivo MP3 a partir del audio de un video de YouTube.

Utiliza el programa únicamente con contenido que tengas derecho a descargar. Los términos de servicio de YouTube y las leyes de derechos de autor pueden limitar la descarga de determinados contenidos.

## Licencia

Este proyecto se proporciona para uso personal y educativo.

