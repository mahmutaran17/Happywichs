import streamlit as st

if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'username' not in st.session_state:
    st.session_state.username = ""
if 'is_admin' not in st.session_state:
    st.session_state.is_admin = False

with st.sidebar:
    st.success("Sayfalar arasında geçiş yapabilirsiniz")

if st.session_state.logged_in:
    st.write(f"Hoşgeldiniz, {st.session_state.username}!")
    if st.button("Çıkış Yap"):
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.session_state.is_admin = False
        st.rerun()

if st.session_state.is_admin:
    st.markdown("---")
    if st.button("👑 Yönetici Paneli"):
        st.switch_page("pages/admin.py")


st.switch_page("pages/main_page.py")