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
if st.session_state.page == "motivation":
    st.subheader("💬 Tell me what you're going through:")
    situation = st.text_input("Describe your current situation:")

    if situation:
        try:
            story_response = model.generate_content(
                f"You are a motivational storyteller. The user is going through this: '{situation}'. Please respond with an inspiring short story that helps them feel strong and positive."
            )
            st.success(story_response.text)
        except Exception as e:
            st.error("Sorry, something went wrong. Please try again later.")
