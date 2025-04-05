import streamlit as st

st.set_page_config(page_title="Mental Health Dashboard", layout="wide")

# Initialize session state
if "page" not in st.session_state:
    st.session_state.page = "dashboard"

# Page title
st.title("💙 Mental Health Dashboard")

# CSS for big, clean feature boxes
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

# Features and navigation
features = [
    ("💬 Motivational Chatbot", "motivation"),
    ("🧠 Mental Health Chat", "chatbot"),
    ("🎭 Talk with a Character", "character_chat"),
    ("🤗 Take a Hug", "hug"),
    ("🌞 Daily Positivity", "positivity"),
    
]

# Create big clickable boxes in a grid
st.markdown('<div class="grid-container">', unsafe_allow_html=True)
for label, value in features:
    st.markdown(f'<a class="big-box" href="?page={value}">{label}</a>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Read selected page from URL
query_params = st.query_params
if "page" in query_params:
    st.session_state.page = query_params["page"]

# Optional: Show what the user selected (for debugging or transition)
st.write(f"📌 You selected: `{st.session_state.page}`")
