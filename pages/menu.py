import streamlit as st
import pandas as pd

st.title("Menümüz")
st.image("static/happywichs.jpg")

menu = {
    "Soğuk Sandviçler": [
        ("Doyuran Sandviç (30 cm)", 269.90),
        ("Tavuklu Sandviç (30 cm)", 249.90),
        ("Ton Balıklı Sandviç (30 cm)", 259.90),
        ("Vegan Sandviç (30 cm)", 219.90),
        ("Köri Soslu Tavuk Sandviç (30 cm)", 259.90)
    ],
    "Sıcak Sandviçler": [
        ("Kaşarlı Tost (30 cm)", 149.90),
        ("Sucuklu Kaşarlı Tost (30 cm)", 199.90),
        ("Pastırmalı Tost (30 cm)", 229.90),
        ("Karamelize Soğanlı Tost (30 cm)", 219.90)
    ],
    "Menüler": [
        ("Sandviç Menü (Sandviç + Patates + İçecek)", 349.90),
        ("Tost Menü (Tost + Patates + İçecek)", 299.90)
    ],
    "Ekstralar": [
        ("Patates (Standart)", 79.90),
        ("Sos Seçimi", 24.90),
        ("Extra Peynir", 49.90),
        ("Extra Tavuk", 69.90)
    ],
    "İçecekler": [
        ("Pepsi (33 cl)", 70.00),
        ("7UP (33 cl)", 70.00),
        ("Limonata (33 cl)", 80.00),
        ("Ayran (25 cl)", 60.00),
        ("Su (50 cl)", 30.00)
    ],
    "Tatlılar": [
        ("Magnolia", 129.90),
        ("Cookie", 89.90),
        ("Brownie", 79.90)
    ]
}

for category, items in menu.items():
    st.subheader(category)
    for name, price in items:
        st.write(f"**{name}** - {price:.2f}₺")

if st.button("Ana Sayfaya Dön"):
    st.switch_page("main")