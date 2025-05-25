import streamlit as st

if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'username' not in st.session_state:
    st.session_state.username = ""

st.sidebar.success("Sayfalar arasında geçiş yapabilirsiniz")
if st.session_state.logged_in:
    st.sidebar.write(f"Hoşgeldiniz, {st.session_state.username}!")
    if st.sidebar.button("Çıkış Yap"):
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.rerun()