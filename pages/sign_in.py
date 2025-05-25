import streamlit as st

# Add this at the top
ADMIN_CREDENTIALS = {
    "admin": "admin123"  # Change this in production!
}

st.title("Giriş Yap")

username = st.text_input("Kullanıcı Adı")
password = st.text_input("Şifre", type="password")

cols = st.columns(2)
with cols[0]:
    if st.button("Giriş"):
        if username and password:
            # Add this admin check block
            if username == "admin" and password == ADMIN_CREDENTIALS["admin"]:
                st.session_state.is_admin = True

            st.session_state.logged_in = True
            st.session_state.username = username
            st.success("Başarıyla giriş yaptınız!")
            st.switch_page("pages/main_page.py")
        else:
            st.error("Lütfen bilgilerinizi girin")

with cols[1]:
    if st.button("Ana Sayfa"):
        st.switch_page("pages/main_page.py")