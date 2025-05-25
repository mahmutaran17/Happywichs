import streamlit as st
import pandas as pd

st.title("Menümüz")
st.image("static/happywichs.jpg")

menu = {
    "Soğuk Sandviçler": [
        ("Doyuran Sandviç (30 cm)", 269.90),
        ("Vegan Sandviç (30 cm)", 219.90)
    ],
    "İçecekler": [
        ("Pepsi (33 cl)", 70.00),
        ("7UP (33 cl)", 70.00)
    ]
}

for category, items in menu.items():
    st.subheader(category)
    for name, price in items:
        st.write(f"**{name}** - {price:.2f}₺")

if st.button("Ana Sayfaya Dön"):
    st.switch_page("pages/1_🏠_Ana_Sayfa.py")