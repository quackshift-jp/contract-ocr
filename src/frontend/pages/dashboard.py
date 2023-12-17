import streamlit as st
import pandas as pd
from frontend.component.api.request import (
    read_contract_endpoint,
    update_contract_endpoint,
)


def render():
    st.title("契約書管理ダッシュボード")
    contracts = read_contract_endpoint(endpoint="http://127.0.0.1:8000/get/contracts/")
    columns = list(contracts[0].keys())
    sort_column = st.sidebar.selectbox("並び替えるカラムを選択してください", columns)
    contract_df = pd.DataFrame(contracts).sort_values(by=sort_column)
    edit_row(contract_df)
    st.markdown("## 契約書一覧")
    st.dataframe(contract_df)


def edit_row(contract_df: pd.DataFrame) -> dict[str, str]:
    contract_id = st.selectbox(label="編集するidを選択", options=contract_df["contract_id"])
    default_contractor = contract_df[contract_df["contract_id"] == contract_id][
        "contractor"
    ].iloc[0]
    contractor = st.text_input(label="編集内容", value=f"{default_contractor}")
    is_exist_text(contractor)

    if st.button("編集保存", key="save_button"):
        response = update_contract_endpoint(
            contract_id=contract_id,
            contractor=contractor,
            endpoint="http://127.0.0.1:8000/update/contracts/",
        )
        contract_df.loc[
            contract_df["contract_id"] == contract_id, "contractor"
        ] = contractor
        st.markdown(
            f"""
        修正が成功しました🎉
        """
        )
        st.balloons()
        return response


def is_exist_text(text):
    if text == "":
        st.error("Please input any text.")
