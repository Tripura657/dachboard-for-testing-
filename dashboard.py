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

elif option == "🧠 Mental Health Chat":
    from mental_health_chat import run_mental_health_chat
    run_mental_health_chat()

elif option == "🎭 Talk with a Character":
    from talk_with_character import run_character_chat
    run_character_chat()

elif option == "🤗 Take a Hug":
    from take_a_hug import run_virtual_hug
    run_virtual_hug()

elif option == "🥰 Daily Positivity":
    from daily_positivity import run_daily_positivity
    run_daily_positivity()
