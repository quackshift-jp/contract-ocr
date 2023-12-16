from PIL import Image
from typing import Union

import streamlit as st
from streamlit.runtime.uploaded_file_manager import UploadedFile

from backend.main import detect, extract_items
from frontend.component.api.request import request_insert_contract_endpoint


def process_file(jpeg_file: Union[UploadedFile, Image.Image]) -> dict[str, any]:
    response = detect(jpeg_file)
    contract_items = extract_items(response)

    # JSONオブジェクトの各キーと値を表示し、編集可能にする
    edited_json = {}
    for key, value in contract_items["content"].items():
        new_value = st.sidebar.text_input(f"{key}: ", value)
        edited_json[key] = new_value

    if st.sidebar.button("保存"):
        st.sidebar.write("以下の内容で保存されました🎉")
        st.sidebar.json(edited_json)
        request_insert_contract_endpoint(
            "http://127.0.0.1:8000/insert/contracts", edited_json["物件名"]
        )
