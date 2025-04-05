import streamlit as st

st.set_page_config(page_title="Mental Health Dashboard", layout="wide")

st.markdown("<h1 style='text-align: center;'>💙 Mental Health Dashboard</h1>", unsafe_allow_html=True)

# Create clickable sections
st.page_link("Motivational_Chatbot.py", label="💬 Motivational Chatbot", section=None)
st.page_link("Mental_Health_Chat.py", label="🧠 Mental Health Chat", section=None)
st.page_link("Talk_with_a_Character.py", label="🎭 Talk with a Character", section=None)
st.page_link("Take_a_Hug.py", label="🤗 Take a Hug", section=None)
st.page_link("Daily_Positivity.py", label="🌞 Daily Positivity", section=None)
st.page_link("Bubble_Game.py", label="🫧 Bubble Game", section=None)
