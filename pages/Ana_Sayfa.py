import streamlit as st

st.title("Happywichs")
st.image("static/happywichs.jpg")
st.header("Hoşgeldiniz!")
st.write("Sandwichs değil, Happywichs")

cols = st.columns(2)
if not st.session_state.logged_in:
    with cols[0]:
        if st.button("Giriş Yap"):
            st.switch_page("pages/2_🔑_Giriş.py")
    with cols[1]:
        if st.button("Kayıt Ol"):
            st.switch_page("pages/3_📝_Kayıt.py")
else:
    st.success(f"Hoşgeldiniz, {st.session_state.username}!")

if st.button("Menümüzü Gör"):
    st.switch_page("pages/4_🍔_Menü.py")