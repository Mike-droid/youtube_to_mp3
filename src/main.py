from pathlib import Path
import subprocess
import yt_dlp


url = input("URL de YouTube: ").strip()
filename = input("Nombre del archivo: ").strip()

output_dir = Path("downloads")
output_dir.mkdir(exist_ok=True)

webm_path = output_dir / f"{filename}.webm"
mp3_path = output_dir / f"{filename}.mp3"

# 1. Descargar únicamente el mejor audio disponible
options = {
    "format": "bestaudio/best",
    "outtmpl": str(webm_path),
}

try:
    print("\nDescargando audio...")

    with yt_dlp.YoutubeDL(options) as ydl:
        ydl.download([url])

    print("✓ Descarga completada.")

    # 2. Convertir WebM → MP3 usando FFmpeg
    print("\nConvirtiendo a MP3...")

    subprocess.run(
        [
            "ffmpeg",
            "-i", str(webm_path),
            "-vn",
            "-codec:a", "libmp3lame",
            "-b:a", "192k",
            str(mp3_path),
        ],
        check=True,
    )

    print("✓ Conversión completada.")

    # 3. Eliminar el WebM temporal
    webm_path.unlink()

    print(f"\n✓ Archivo final: {mp3_path}")

except Exception as error:
    print(f"\n✗ Ocurrió un error: {error}")
