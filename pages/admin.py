import streamlit as st
import pandas as pd

# Authentication check
if not st.session_state.get("is_admin"):
    st.error("⛔ Yönetici erişimi gereklidir!")
    st.switch_page("pages/main_page.py")

st.title("👨‍💻 Yönetici Paneli")
st.subheader("Geri Bildirimler")

try:
    df = pd.read_csv("feedback.csv")

    # Filters
    st.sidebar.header("Filtreleme")
    name_search = st.sidebar.text_input("İsme göre ara")
    date_filter = st.sidebar.date_input("Tarihe göre filtrele")

    if name_search:
        df = df[df["name"].str.contains(name_search, case=False)]
    if date_filter:
        df = df[df["order_date"] == date_filter.strftime("%d.%m.%Y")]

    # Display
    st.dataframe(df)

    # Download
    st.download_button(
        "Veriyi İndir",
        df.to_csv(index=False),
        "happywichs_feedback.csv",
        "text/csv"
    )

except FileNotFoundError:
    st.warning("Henüz geri bildirim bulunmamaktadır")