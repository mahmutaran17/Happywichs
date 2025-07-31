# 🌟 HappyWichs – Streamlit Feedback App

**HappyWichs** is a lightweight, user-friendly web application built with **Streamlit**. It provides basic user authentication (sign up & login) and allows users to send **feedback** via a form interface. It's ideal as a starter project for those learning about Streamlit apps with session management and form handling.

---

## 🧩 Features

- 🔐 **User Authentication**
  - Secure login & signup system
  - Passwords stored as hashed values
  - Session tracking using `st.session_state`

- 💬 **Feedback Submission**
  - Form includes: Name, Email, Rating, and Message
  - Data saved to a local database or CSV
  - Confirmation message upon submission

- ⚡ **Modern UI with Streamlit**
  - Responsive, real-time interface
  - Clean layout using columns and Streamlit widgets

---

## 📸 Screenshots

> _(![WhatsApp Image 2025-07-31 at 22 17 26](https://github.com/user-attachments/assets/4eef8892-e80d-48ee-8b6c-4ba9200d8fff)
)_

---

## 🛠️ Tech Stack

| Layer        | Technology      |
|--------------|-----------------|
| Frontend     | Streamlit       |
| Backend      | Python          |
| Database     | CSV / SQLite (optional) |
| Auth Logic   | Python (hashlib) |
| Hosting      | Localhost / Streamlit Cloud |

---

## 🔐 Authentication Sample (Python)
```python
import streamlit as st
import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def login(username, password, user_db):
    if username in user_db and user_db[username]['password'] == hash_password(password):
        return True
    return False

# Example usage
user_db = {"mahmut": {"password": hash_password("1234")}}

st.title("Login")
username = st.text_input("Username")
password = st.text_input("Password", type="password")
if st.button("Login"):
    if login(username, password, user_db):
        st.success("Login successful!")
    else:
        st.error("Invalid credentials.")
