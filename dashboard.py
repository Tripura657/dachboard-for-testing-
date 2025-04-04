import streamlit as st

st.set_page_config(page_title="Mental Health Dashboard", layout="wide")

# Initialize session state
if "page" not in st.session_state:
    st.session_state.page = "dashboard"

# Title
st.title("💙 Mental Health Dashboard")

# Custom CSS for big clickable boxes
st.markdown("""
    <style>
    .big-box {
        display: block;
        padding: 30px;
        margin: 10px;
        border-radius: 15px;
        background-color: #e6f2ff;
        color: #003366;
        text-align: center;
        font-size: 20px;
        font-weight: bold;
        cursor: pointer;
        transition: 0.3s;
        border: 2px solid transparent;
    }
    .big-box:hover {
        background-color: #d1e7ff;
        border-color: #3399ff;
    }
    a {
        text-decoration: none;
    }
    </style>
""", unsafe_allow_html=True)

# Create layout with 2 rows of 3 boxes
cols1 = st.columns(3)
features = [
    ("💬 Motivational Chatbot", "motivation"),
    ("🧠 Mental Health Chat", "chatbot"),
    ("🎭 Talk with a Character", "character_chat"),
    ("🤗 Take a Hug", "hug"),
    ("🌞 Daily Positivity", "positivity"),
    ("🫧 Bubble Game", "bubble_game"),
]

# Create feature boxes
for i, (label, value) in enumerate(features):
    col = cols1[i % 3] if i < 3 else st.columns(3)[i % 3]
    with col:
        if st.markdown(f'<a class="big-box" href="?page={value}">{label}</a>', unsafe_allow_html=True):
            st.session_state.page = value

# Show which one is clicked (for now)
query_params = st.experimental_get_query_params()
if "page" in query_params:
    st.session_state.page = query_params["page"][0]
    st.write(f"📌 You selected: `{st.session_state.page}`")
