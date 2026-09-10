from youtube_to_mp3.converter import (
    create_download_directory,
    convert_to_mp3,
    delete_file,
    download_audio,
)


def main() -> None:
    url = input("URL de YouTube: ").strip()
    filename = input("Nombre del archivo: ").strip()

    output_dir = create_download_directory()

    webm_path = output_dir / f"{filename}.webm"
    mp3_path = output_dir / f"{filename}.mp3"

    try:
        print("\nDescargando audio...")

        download_audio(url, webm_path)

        print("✓ Descarga completada.")

        print("\nConvirtiendo a MP3...")

        convert_to_mp3(webm_path, mp3_path)

        print("✓ Conversión completada.")

        delete_file(webm_path)

        print(f"\n✓ Archivo final: {mp3_path}")

    except Exception as error:
        print(f"\n✗ Ocurrió un error: {error}")


if __name__ == "__main__":
    main()