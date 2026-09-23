# YouTube to MP3

Aplicación sencilla en Python que descarga el audio de un video de YouTube y lo convierte automáticamente a formato `.mp3`.

El programa solicita:

1. La URL del video de YouTube.
2. El nombre que tendrá el archivo MP3 final.

El audio se descarga temporalmente en formato `.webm`, posteriormente se convierte a MP3 utilizando FFmpeg y, si la conversión termina correctamente, el archivo `.webm` temporal se elimina.

## Requisitos

Para ejecutar el proyecto directamente en el sistema se requiere:

* Python 3.12 o superior
* FFmpeg
* `yt-dlp`

El proyecto fue desarrollado y probado utilizando **Ubuntu mediante WSL**.

También es posible ejecutar la aplicación mediante **Docker**, sin necesidad de instalar Python, FFmpeg o `yt-dlp` directamente en el sistema.

## Instalación

### Opción 1: Ejecución local

Clona el repositorio:

```bash
git clone https://github.com/Mike-droid/youtube_to_mp3.git
cd youtube_to_mp3
```

Crea un entorno virtual:

```bash
python3 -m venv .venv
```

Activa el entorno virtual:

```bash
source .venv/bin/activate
```

Instala las dependencias del proyecto:

```bash
pip install -e .
```

Para instalar también las dependencias necesarias para ejecutar las pruebas:

```bash
pip install -e ".[dev]"
```

Instala FFmpeg en Ubuntu:

```bash
sudo apt update
sudo apt install ffmpeg
```

Puedes comprobar que las herramientas principales estén instaladas correctamente:

```bash
python --version
yt-dlp --version
ffmpeg -version
```

### Opción 2: Docker

El proyecto incluye un `Dockerfile` que instala automáticamente Python, FFmpeg y las dependencias necesarias.

Construye la imagen:

```bash
docker build -t youtube-to-mp3 .
```

Ejecuta el contenedor:

```bash
docker run --rm -it \
  -v "$(pwd)/downloads:/app/downloads" \
  youtube-to-mp3
```

El volumen permite conservar los archivos generados en la carpeta `downloads` del proyecto aunque el contenedor sea eliminado.

## Uso

### Ejecución local

Con el entorno virtual activado:

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

### Ejecución con Docker

También es posible ejecutar el programa directamente desde la imagen Docker:

```bash
docker run --rm -it \
  -v "$(pwd)/downloads:/app/downloads" \
  youtube-to-mp3
```

## ¿Cómo funciona?

El proceso de conversión es el siguiente:

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
youtube_to_mp3/
├── .github/
│   └── workflows/
│       └── ci.yml
├── src/
│   ├── main.py
│   └── converter.py
├── tests/
│   └── test_converter.py
├── .dockerignore
├── .gitignore
├── Dockerfile
├── pyproject.toml
└── README.md
```

La carpeta `downloads/` se crea automáticamente cuando se ejecuta el programa y se utiliza para almacenar los archivos generados.

## Pruebas

El proyecto utiliza **pytest** para realizar pruebas automatizadas.

Para ejecutar las pruebas localmente:

```bash
python -m pytest -v
```

Las pruebas verifican diferentes partes de la lógica de conversión y manejo de archivos.

## Integración continua

El proyecto utiliza **GitHub Actions** para automatizar las pruebas y la construcción de la imagen Docker.

El workflow se encuentra en:

```text
.github/workflows/ci.yml
```

El flujo general es:

```text
Push / Pull Request
        │
        ▼
   Ejecutar tests
        │
        ▼
    ¿Tests pasan?
      /       \
    No         Sí
    │           │
    ▼           ▼
  Detener    Build Docker
                │
                ▼
          ¿Push a main?
             /     \
           No       Sí
           │         │
           ▼         ▼
       Solo build  Docker Hub
```

Las pruebas se ejecutan automáticamente en cada `push` y `pull request`.

La imagen Docker se construye después de que las pruebas terminan correctamente.

Las imágenes solamente se publican en Docker Hub cuando corresponde a un flujo de publicación configurado para `main` o una versión de lanzamiento.

## Docker Hub

La imagen Docker del proyecto se publica en **Docker Hub** mediante GitHub Actions.

El flujo de publicación utiliza:

* Docker Login Action
* Docker Metadata Action
* Docker Build and Push Action
* Docker Buildx

Las credenciales de Docker Hub se almacenan como **GitHub Actions Secrets** y no forman parte del código fuente.

La imagen puede utilizarse posteriormente sin necesidad de clonar el repositorio ni configurar manualmente el entorno de Python.

## Versionado de imágenes

El proyecto utiliza **Semantic Versioning (SemVer)** para identificar versiones de las imágenes Docker.

El formato utilizado es:

```text
MAJOR.MINOR.PATCH
```

Por ejemplo:

```text
v0.1.0
v0.1.1
v0.2.0
v1.0.0
```

Los cambios se clasifican de la siguiente manera:

* **PATCH**: correcciones de errores y cambios pequeños que no modifican la compatibilidad.
* **MINOR**: nuevas funcionalidades compatibles con versiones anteriores.
* **MAJOR**: cambios que pueden romper la compatibilidad existente.

Durante la etapa inicial de desarrollo se utiliza la versión `0.x.y`.

Por ejemplo, para crear una nueva versión:

```bash
git tag v0.1.0
git push origin v0.1.0
```

Las etiquetas de versión permiten generar tags específicos para las imágenes Docker, por ejemplo:

```text
youtube-to-mp3:0.1.0
youtube-to-mp3:0.1
```

La etiqueta `latest` representa la versión publicada desde la rama principal según la configuración del workflow.

## Características

* Descarga el audio de un video de YouTube.
* Convierte automáticamente el audio a MP3.
* Permite elegir el nombre del archivo.
* Guarda los archivos en una carpeta `downloads`.
* Elimina automáticamente el archivo `.webm` temporal después de una conversión exitosa.
* Utiliza FFmpeg para realizar la conversión.
* Utiliza un entorno virtual de Python para aislar las dependencias.
* Incluye pruebas automatizadas con pytest.
* Incluye un `Dockerfile` para ejecutar la aplicación en un contenedor.
* Utiliza GitHub Actions para automatizar las pruebas y la construcción de imágenes Docker.
* Publica imágenes Docker en Docker Hub.
* Utiliza versionado basado en Semantic Versioning.

## Tecnologías utilizadas

* **Python** — lenguaje principal.
* **yt-dlp** — descarga del stream de audio.
* **FFmpeg** — conversión de audio.
* **pytest** — pruebas automatizadas.
* **Docker** — contenedorización de la aplicación.
* **GitHub Actions** — integración y automatización del pipeline CI/CD.
* **Docker Hub** — almacenamiento y distribución de imágenes Docker.
* **Git** — control de versiones.

## Notas

Este es un proyecto personal y educativo diseñado para realizar una tarea específica de manera sencilla: obtener un archivo MP3 a partir del audio de un video de YouTube.

Utiliza el programa únicamente con contenido que tengas derecho a descargar. Los términos de servicio de YouTube y las leyes de derechos de autor pueden limitar la descarga de determinados contenidos.

## Licencia

Este proyecto se proporciona para uso personal y educativo.
