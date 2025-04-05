import streamlit as st
from streamlit import session_state as state

# Set page config
st.set_page_config(page_title="Mental Health Dashboard", layout="wide")

# Initialize session state
if "page" not in state:
    state.page = "dashboard"

# Custom CSS
st.markdown("""
    <style>
    .grid-container {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 20px;
        padding: 10px 0;
    }

    .big-box {
        display: block;
        padding: 30px;
        border-radius: 15px;
        background-color: #e6f2ff;
        color: #003366;
        text-align: center;
        font-size: 22px;
        font-weight: bold;
        text-decoration: none;
        transition: all 0.3s ease;
        border: 2px solid transparent;
    }

    .big-box:hover {
        background-color: #d1e7ff;
        border-color: #3399ff;
        transform: scale(1.03);
    }
    </style>
""", unsafe_allow_html=True)

# Page title
st.title("💙 Mental Health Dashboard")

# Features and their query page names
features = [
    ("💬 Motivational Chatbot", "motivation"),
    ("🧠 Mental Health Chat", "chatbot"),
    ("🎭 Talk with a Character", "character"),
    ("🤗 Take a Hug", "hug"),
    ("🌞 Daily Positivity", "positivity"),
    ("🫧 Bubble Game", "bubble"),
]

# Feature Grid
st.markdown('<div class="grid-container">', unsafe_allow_html=True)
for label, page in features:
    st.markdown(f'<a class="big-box" href="/?page={page}">{label}</a>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Update current page from URL query
query_params = st.query_params
if "page" in query_params:
    state.page = query_params["page"]

# Page Routing Logic
if state.page == "motivation":
    st.header("💬 Motivational Chatbot")
    st.write("Here goes your motivational chatbot logic.")

elif state.page == "chatbot":
    st.header("🧠 Mental Health Chat")
    st.write("Here goes your mental health chatbot logic.")

elif state.page == "character":
    st.header("🎭 Talk with a Character")
    st.write("Here goes your character interaction logic.")

elif state.page == "hug":
    st.header("🤗 Take a Hug")
    st.write("Here goes your virtual hug logic.")

elif state.page == "positivity":
    st.header("🌞 Daily Positivity")
    st.write("Here goes your daily positivity challenge logic.")

elif state.page == "bubble":
    st.header("🫧 Bubble Game")
    st.write("Here goes your bubble popping game logic.")

else:
    st.info("🔍 Select a feature from the dashboard above.")
