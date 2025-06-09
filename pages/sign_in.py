import streamlit as st


st.title("Giriş Yap")

username = st.text_input("Kullanıcı Adınızı öğrenebilir miyim")
password = st.text_input("Şifre", type="password")

cols = st.columns(2)

with cols[0]:
    if st.button("Giriş Yap"):
        if username and password:
            st.session_state.logged_in = True
            st.session_state.username = username
            st.success("Başarıyla giriş yapıldı!")
            st.switch_page("pages/main_page.py")
        else:
            st.error("Lütfen kullanıcı ad ve şifre girin")

with cols[1]:
    if st.button("Ana Sayfa"):
        st.switch_page("pages/main_page.py")
