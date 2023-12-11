import pathlib
import sys

import streamlit as st

sys.path.append(str(pathlib.Path().absolute()))

from backend.modules.pdf_to_image import (
    convert_streamlit_pdf_to_images,
)
from backend.main import detect, extract_items


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
        # TODO:フロントの責務を分離する
        contract_items = extract_items(response)

        # JSONオブジェクトの各キーと値を表示し、編集可能にする
        edited_json = {}
        for key, value in contract_items["content"].items():
            new_value = st.sidebar.text_input(f"{key}: ", value)
            edited_json[key] = new_value

        # 編集された内容を表示するボタン
        if st.sidebar.button("更新"):
            st.sidebar.write("更新されたJSON:")
            st.sidebar.json(edited_json)


index_page()
