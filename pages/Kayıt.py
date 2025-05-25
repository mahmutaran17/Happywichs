import streamlit as st

st.title("Kayıt Ol")

username = st.text_input("Yeni Kullanıcı Adı")
password = st.text_input("Yeni Şifre", type="password")

cols = st.columns(2)
with cols[0]:
    if st.button("Kayıt Ol"):
        if username and password:
            st.success("Kayıt başarılı! Giriş yapabilirsiniz.")
            st.switch_page("Giriş.py")
        else:
            st.error("Lütfen tüm alanları doldurun")

with cols[1]:
    if st.button("Ana Sayfa"):
        st.switch_page("Ana_Sayfa.py")