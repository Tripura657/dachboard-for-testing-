import streamlit as st

st.set_page_config(page_title="Mental Health Dashboard", layout="wide")

# Page title
st.markdown("<h1 style='text-align: center;'>💙 Mental Health Dashboard</h1>", unsafe_allow_html=True)

# CSS for grid layout
st.markdown("""
    <style>
    .grid-container {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 20px;
        padding: 20px;
    }
    .grid-item {
        background-color: #e6f2ff;
        color: #003366;
        padding: 30px;
        text-align: center;
        border-radius: 15px;
        font-size: 22px;
        font-weight: bold;
        transition: all 0.3s ease;
        border: 2px solid transparent;
        text-decoration: none;
    }
    .grid-item:hover {
        background-color: #d1e7ff;
        border-color: #3399ff;
        transform: scale(1.05);
    }
    </style>
""", unsafe_allow_html=True)

# Grid layout with internal links to pages
st.markdown("""
<div class="grid-container">
    <a href="./Motivational_Chatbot" class="grid-item">💬 Motivational Chatbot</a>
    <a href="./Mental_Health_Chat" class="grid-item">🧠 Mental Health Chat</a>
    <a href="./Talk_with_a_Character" class="grid-item">🎭 Talk with a Character</a>
    <a href="./Take_a_Hug" class="grid-item">🤗 Take a Hug</a>
    <a href="./Daily_Positivity" class="grid-item">🌞 Daily Positivity</a>
    <a href="./Bubble_Game" class="grid-item">🫧 Bubble Game</a>
</div>
""", unsafe_allow_html=True)
