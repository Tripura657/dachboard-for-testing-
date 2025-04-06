import streamlit as st
import google.generativeai as genai

# --- Page Config ---
st.set_page_config(page_title="Mental Health Support", layout="centered")

# --- Configure Gemini ---
genai.configure(api_key="YOUR_API_KEY")  # Replace with your actual key
model = genai.GenerativeModel("gemini-1.5-flash")

# --- Routing via query params ---
query_params = st.query_params
if "page" in query_params:
    st.session_state.page = query_params["page"]
elif "page" not in st.session_state:
    st.session_state.page = "home"

# --- HOME PAGE ---
if st.session_state.page == "home":
    st.title("💙 Mental Health Dashboard")

    st.markdown("""
        <style>
            .dashboard-grid {
                display: grid;
                grid-template-columns: repeat(3, 1fr);
                gap: 30px;
                justify-items: center;
            }
            .dashboard-item {
                text-align: center;
                transition: transform 0.3s ease, box-shadow 0.3s ease;
            }
            .dashboard-item:hover {
                transform: scale(1.05);
                box-shadow: 0 4px 20px rgba(0,0,0,0.3);
            }
            .dashboard-item img {
                border-radius: 20px;
                width: 200px;
                height: 200px;
                object-fit: cover;
            }
            .dashboard-item p {
                margin-top: 10px;
                font-weight: bold;
                color: white;
            }
        </style>

        <div class="dashboard-grid">
            <div class="dashboard-item">
                <a href="/?page=motivation">
                    <img src="https://i.ibb.co/XzTc1mF/motivation.png" />
                    <p>Motivational Chatbot</p>
                </a>
            </div>
            <div class="dashboard-item">
                <a href="/?page=chatbot">
                    <img src="https://i.ibb.co/4YsXM0x/mental-health-chat.png" />
                    <p>Mental Health Chat</p>
                </a>
            </div>
            <div class="dashboard-item">
                <a href="/?page=character_chat">
                    <img src="https://i.ibb.co/jv3B6QZ/character.png" />
                    <p>Talk with a Character</p>
                </a>
            </div>
            <div class="dashboard-item">
                <a href="/?page=hug">
                    <img src="https://i.ibb.co/qkFV1xq/hug.png" />
                    <p>Take a Hug</p>
                </a>
            </div>
            <div class="dashboard-item">
                <a href="/?page=positivity">
                    <img src="https://i.ibb.co/0jkpsZC/yoga.png" />
                    <p>Yoga
