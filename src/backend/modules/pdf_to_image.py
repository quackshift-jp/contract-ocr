from pathlib import Path
from pdf2image import convert_from_path
from streamlit.runtime.uploaded_file_manager import UploadedFile
from PIL import Image
import tempfile


def convert_pdf_to_images(
    google_path: Path, save_path: Path, search_keyword: str
) -> None:
    for pdf in google_path.glob(f"*{search_keyword}*"):
        convert_from_path(
            pdf, output_folder=save_path, fmt="jpeg", output_file=pdf.stem, dpi=200
        )


def convert_streamlit_pdf_to_images(pdf_file: UploadedFile) -> list[Image.Image]:
    # ディスクに一時ファイルを書き出すことで、メモリ消費を抑える
    with tempfile.NamedTemporaryFile() as temp_file:
        temp_file.write(pdf_file.read())
        temp_file_path = temp_file.name

        images = convert_from_path(temp_file_path)
    return images
