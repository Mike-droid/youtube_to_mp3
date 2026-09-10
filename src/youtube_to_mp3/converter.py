from pathlib import Path
import subprocess
import yt_dlp


def download_audio(url: str, output_path: Path) -> None:
    options = {
        "format": "bestaudio/best",
        "outtmpl": str(output_path),
    }

    with yt_dlp.YoutubeDL(options) as ydl:
        ydl.download([url])


def convert_to_mp3(webm_path: Path, mp3_path: Path) -> None:
    subprocess.run(
        [
            "ffmpeg",
            "-i",
            str(webm_path),
            "-vn",
            "-codec:a",
            "libmp3lame",
            "-b:a",
            "192k",
            str(mp3_path),
        ],
        check=True,
    )


def delete_file(file_path: Path) -> None:
    file_path.unlink()


def create_download_directory() -> Path:
    output_dir = Path("downloads")
    output_dir.mkdir(exist_ok=True)
    return output_dir
