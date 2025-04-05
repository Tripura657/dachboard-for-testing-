import streamlit as st

st.set_page_config(page_title="Mental Health Support Dashboard", layout="centered")

st.title("🧠 Mental Health Support System")

# Button-style tiles for navigation
option = st.radio(
    "Choose a Feature:",
    ("💬 Motivational Chatbot", 
     "🧠 Mental Health Chat", 
     "🎭 Talk with a Character", 
     "🤗 Take a Hug", 
     "🥰 Daily Positivity"),
    label_visibility="collapsed"
)

# Dynamic Module Loader
if option == "💬 Motivational Chatbot":
    from motivational_chatbot import run_motivational_chatbot
    run_motivational_chatbot()

