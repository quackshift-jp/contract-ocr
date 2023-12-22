from PIL.PpmImagePlugin import PpmImageFile
from typing import Union

import streamlit as st
from streamlit.runtime.uploaded_file_manager import UploadedFile

from backend.main import detect, extract_items
from backend.modules.upload_to_s3 import upload_streamlit_file_to_s3
from frontend.component.api.request import insert_contract_endpoint
from frontend.component.api.request import read_specific_contract_endpoint


def is_already_exist(column_name: str, value: str) -> bool:
    response = read_specific_contract_endpoint(
        "http://127.0.0.1:8000/get/contract", column_name, value
    )
    return response is None


def process_file(jpeg_file: Union[UploadedFile, list[PpmImageFile]]) -> None:
    response = detect(jpeg_file)
    contract_items = extract_items(response)

    st.sidebar.markdown("### 項目確認")
    # JSONオブジェクトの各キーと値を表示し、編集可能にする
    edited_json = {}
    for key, value in contract_items["content"].items():
        new_value = st.sidebar.text_input(f"{key}: ", value)
        edited_json[key] = new_value

    if st.sidebar.button("保存", key="保存ボタン"):
        if not is_already_exist("contractor", edited_json["物件名"]):
            st.sidebar.error("エラー: この物件名は既に存在します。")
        else:
            st.sidebar.write("以下の内容で保存されました🎉")
            st.sidebar.json(edited_json)
            upload_streamlit_file_to_s3(jpeg_file, "contract-ocr", edited_json["物件名"])
            insert_contract_endpoint(
                "http://127.0.0.1:8000/insert/contracts", edited_json["物件名"]
            )
