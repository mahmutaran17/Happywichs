import streamlit as st
import pandas as pd

from pages.sign_in import username

ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "1234"

st.title("🔐 Admin Paneli")

if "admin_logged_in" not in st.session_state:
    st.session_state.admin_logged_in = False

if not st.session_state.admin_logged_in:
    st.subheader("Giriş Yap")
    username = st.text_input("Kullanıcı adı", key="admin_username_input")
    password = st.text_input("Şifre", type="password", key="admin_password_input")

    if st.button("Giriş"):
        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            st.session_state.admin_logged_in = True
            st.success("Giriş Başarılı !")
        else:
            st.error("Kullanıcı adı veya şifreniz hatalı !")

if st.session_state.admin_logged_in:
    st.subheader("📋 Müşteri Geri Bildirimleri")

    try:
        df = pd.read_csv("feedback.csv")
        st.dataframe(df, use_container_width=True)
    except FileNotFoundError:
        st.warning("Henüz herhangi bir geri bildirim yok.")

    if st.button("Çıkış Yap"):
        st.session_state.admin_logged_in = False
        st.rerun()