import streamlit as st
import pandas as pd
from frontend.component.api.request import request_read_contract_endpoint


def dashboard_page():
    st.title("契約書管理ダッシュボード")
    contracts = request_read_contract_endpoint(
        endpoint="http://127.0.0.1:8000/get/contracts/"
    )
    columns = list(contracts[0].keys())
    sort_column = st.sidebar.selectbox("並び替えるカラムを選択してください", columns)
    df = pd.DataFrame(contracts).sort_values(by=sort_column)

    st.dataframe(df)
