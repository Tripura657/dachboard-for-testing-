import streamlit as st  # <-- This line is super important!

# Initialize session state for page navigation
if "page" not in st.session_state:
    st.session_state.page = "dashboard"

# App title
st.title("💙 Mental Health Dashboard")

# Button grid
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("💬 Motivational Chatbot"):
        st.session_state.page = "motivation"

with col2:
    if st.button("🧠 Mental Health Chat"):
        st.session_state.page = "chatbot"

with col3:
    if st.button("🎭 Talk with a Character"):
        st.session_state.page = "character_chat"

col4, col5, col6 = st.columns(3)

with col4:
    if st.button("🤗 Take a Hug"):
        st.session_state.page = "hug"

with col5:
    if st.button("🌞 Daily Positivity"):
        st.session_state.page = "positivity"

with col6:
    if st.button("🫧 Bubble Game"):
        st.session_state.page = "bubble_game"

# Display which feature is selected
st.write(f"📌 You selected: `{st.session_state.page}`")
