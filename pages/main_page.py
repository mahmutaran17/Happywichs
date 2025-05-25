import streamlit as st

if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'username' not in st.session_state:
    st.session_state.username = ""

st.title("Happywichs")
st.image("static/happywichs.jpg")
st.header("Hoşgeldiniz!")
st.write("Sandwichs değil, Happywichs !")

cols = st.columns(2)
if not st.session_state.logged_in:
    with cols[0]:
        if st.button("Giriş Yap"):
            st.switch_page("pages/sign_in.py")
    with cols[1]:
        if st.button("Kayıt Ol"):
            st.switch_page("pages/sign_up.py")
else:
    st.success(f"Hoşgeldiniz, {st.session_state.username}!")

if st.button("Menümüzü Gör"):
    st.switch_page("pages/menu.py")

if st.button("Öneri ve Şikayetleriniz :)"):
    st.switch_page("pages/feedback.py")