from pathlib import Path
from pdf2image import convert_from_path


def convert_pdf_to_images(
    google_path: Path, save_path: Path, search_keyword: str
) -> None:
    for pdf in google_path.glob(f"*{search_keyword}*"):
        convert_from_path(
            pdf, output_folder=save_path, fmt="jpeg", output_file=pdf.stem, dpi=200
        )
