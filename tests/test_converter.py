from src.youtube_to_mp3.converter import (
    create_download_directory,
    delete_file,
)


def test_create_download_directory(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    output_dir = create_download_directory()

    assert output_dir.exists()
    assert output_dir.is_dir()
    assert output_dir.name == "downloads"


def test_delete_file(tmp_path):
    file_path = tmp_path / "test.webm"
    file_path.write_text("test")

    delete_file(file_path)

    assert not file_path.exists()