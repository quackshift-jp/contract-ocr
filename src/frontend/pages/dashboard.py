import streamlit as st
import pandas as pd
from frontend.component.api.request import request_read_contract_endpoint


def dashboard_page():
    print("出力")
    contracts = request_read_contract_endpoint(
        endpoint="http://127.0.0.1:8000/get/contracts/"
    )
    df = pd.DataFrame(contracts)
    st.dataframe(df)
