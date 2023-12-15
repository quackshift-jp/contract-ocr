import streamlit as st

from pages import index, dashboard


def main():
    page = st.sidebar.selectbox(
        label="ページを選択してください", options=["トップページ", "アップロード画面", "ダッシュボード"]
    )

    if page == "アップロード画面":
        index.index_page()
    if page == "ダッシュボード":
        dashboard.dashboard_page()


if __name__ == "__main__":
    main()
