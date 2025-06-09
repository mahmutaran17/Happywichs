import streamlit as st
import pandas as pd
from datetime import datetime
import os

def save_feedback(name, surname, age, order_date, order_no, product, comment):
    new_data = pd.DataFrame([{
        "name": name,
        "surname": surname,
        "age": age,
        "order_date": order_date.strftime("%d.%m.%Y"),
        "order_no": order_no,
        "product": product,
        "comment": comment,
        "timestamp": datetime.now().strftime("%d.%m.%Y %H:%M")
    }])

    try:
        existing = pd.read_csv("feedback.csv")
        updated = pd.concat([existing, new_data])
    except FileNotFoundError:
        updated = new_data

    updated.to_csv("feedback.csv", index=False)

st.title("📝 Geri Bildirim Formu")
st.write("Deneyiminizi bizimle paylaşın!")

with st.form("feedback_form"):
    # Personal Information
    st.subheader("Kişisel Bilgiler")
    name = st.text_input("Ad*")
    surname = st.text_input("Soyad")
    age = st.number_input("Yaş", min_value=12, max_value=100)

    st.subheader("Sipariş Bilgileri")
    order_date = st.date_input("Sipariş Tarihi*")
    order_no = st.text_input("Sipariş Numarası*")
    product = st.selectbox(
        "Sipariş Edilen Ürün",
        ["Klasik Happywich", "Vejetaryen Menü", "Acılı Seçim", "Özel Sipariş"]
    )

    st.subheader("Geri Bildiriminiz")
    comment = st.text_area("Yorumunuz*", height=150)

    if st.form_submit_button("Gönder"):
        if name and order_no and comment:
            save_feedback(name, surname, age, order_date, order_no, product, comment)
            st.success("Teşekkür ederiz! Geri bildiriminiz kaydedildi.")
        else:
            st.error("Lütfen * işaretli alanları doldurunuz")


