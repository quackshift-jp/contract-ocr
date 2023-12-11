import pathlib
import sys

import streamlit as st

sys.path.append(str(pathlib.Path().absolute()))

from backend.modules.pdf_to_image import (
    convert_streamlit_pdf_to_images,
)
from frontend.component.organisms.file_processor import process_file
from frontend.component.utils.navigation import next_file, previous_file


def index_page() -> None:
    st.title("OCR自動化プロダクト")
    st.sidebar.markdown("### 読み込む契約書をアップロード（複数ファイル可）")
    upload_files = st.sidebar.file_uploader(
        "Upload a PDF or jpeg file", type=["pdf", "jpg"], accept_multiple_files=True
    )

    # アップされたファイル情報を一枚ずつ表示するため、indexを状態として保持する
    if "current_index" not in st.session_state:
        st.session_state["current_index"] = 0

    if upload_files:
        st.session_state["upload_files"] = upload_files
        file = upload_files[st.session_state["current_index"]]
        if file.type == "application/pdf":
            file = convert_streamlit_pdf_to_images(file)
        st.image(file)

        # TODO:このjson情報を、データベースに保存する必要がある
        edited_json = process_file(file)
        print(edited_json)

        col1, col2 = st.sidebar.columns(2)
        with col1:
            if st.button("前へ"):
                previous_file()

        with col2:
            if st.button("次へ"):
                next_file()


index_page()
