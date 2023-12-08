import pathlib
import sys

import streamlit as st

sys.path.append(str(pathlib.Path().absolute()))

from backend.modules.pdf_to_image import (
    convert_streamlit_pdf_to_images,
)
from main import detect


def index_page() -> None:
    st.title("OCR自動化プロダクト")

    st.sidebar.markdown("### 読み込む契約書をアップロード（複数ファイル可）")
    upload_files = st.sidebar.file_uploader(
        "Upload a PDF or jpeg file", type=["pdf", "jpg"], accept_multiple_files=True
    )
    for file in upload_files:
        if file.type == "application/pdf":
            file = convert_streamlit_pdf_to_images(file)

        st.image(file)

        response = detect(file)
        st.write(response)


index_page()
