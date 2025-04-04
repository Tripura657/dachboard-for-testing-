st.title("💙 Mental Health Dashboard")

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
