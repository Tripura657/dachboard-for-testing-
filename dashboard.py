import streamlit as st
import google.generativeai as genai

# --- Page Config ---
st.set_page_config(page_title="Mental Health Support", layout="centered")

# --- Configure Gemini ---
genai.configure(api_key="AIzaSyCX5TKAFYkpT3JLnEa0_alXNjwYpe_-S2E")  # Replace with your actual key

# --- Load model ---
model = genai.GenerativeModel("gemini-1.5-flash")

# --- Session state to track page ---
if "page" not in st.session_state:
    st.session_state.page = "home"

# --- Home Dashboard Layout ---
if st.session_state.page == "home":
    st.title("💙 Mental Health Dashboard")

    col1, col2, col3 = st.columns(3)
    with col1:
        if  st.button("💬 Motivational Chatbot"):
            st.session_state.page = "motivation"

    with col2:
        if st.button("🧠 Mental Health Chat"):
            st.session_state.page = "chatbot"

    with col3:
        if st.button("🎭 Talk with a Character"):
            st.session_state.page = "character_chat"

    col4, col5 = st.columns(2)
    with col4:
        if st.button("🤗 Take a Hug"):
            st.session_state.page = "hug"

    with col5:
        if st.button("🧘 Yoga Asanas "):
            st.session_state.page = "positivity"

    

# --- Motivational Chatbot Logic ---
if st.session_state.page == "motivation":
    st.title("💬 Motivational Story Chatbot")
    st.write("Tell me what's on your mind, and I’ll share a story that might lift you up! 💙")
    situation = st.text_input("🌱 Describe your current situation:")
    if situation:
        try:
            story_response = model.generate_content(
                f"You are a motivational storyteller. The user is going through this: '{situation}'. Please respond with an inspiring short story that helps them feel strong and positive."
            )
            story = story_response.text
            st.subheader("📖 Here's a story for you:")
            st.success(story)
        except Exception as e:
            st.error("Sorry, something went wrong. Please try again later.")
    st.button("🔙 Back to Home", on_click=lambda: st.session_state.update({"page": "home"}))

# --- Mental Health Chatbot Logic ---
elif st.session_state.page == "chatbot":
    st.title("💙 Mental Health Support Chatbot")
    query = st.text_input("Hello! I'm here to listen and support you. Feel free to share your thoughts, and I'll try my best to help. Remember, you're not alone! 💙")
    if query:
        try:
            response = model.generate_content(
                f"You are a mental health chatbot trained to provide comforting and understanding responses. The user says: '{query}'"
            )
            st.success(response.text)
        except:
            st.error("Oops! Something went wrong.")
    st.button("🔙 Back to Home", on_click=lambda: st.session_state.update({"page": "home"}))

# --- Character Chat Logic ---
elif st.session_state.page == "character_chat":
    st.title("🎭 Talk with Your Favorite Character")
    characters = {
        "Harry Potter": "https://media.giphy.com/media/xT0GqeSlGSRQutAOcw/giphy.gif",
        "Iron Man": "https://media.giphy.com/media/l0MYt5jPR6QX5pnqM/giphy.gif",
        "Doraemon": "https://media.giphy.com/media/Sr7jKkY8Yx3AA/giphy.gif",
        "Naruto": "https://media.giphy.com/media/xT9DPqdgyD78dA77Ha/giphy.gif",
        "Elsa": "https://media.giphy.com/media/l0MYC0LajbaPoEADu/giphy.gif"
    }
    character = st.selectbox("Choose a character:", list(characters.keys()))
    prompt = st.chat_input(f"What do you want to tell {character}?")
    if prompt:
        with st.spinner("Summoning your character..."):
            try:
                reply = model.generate_content(
                    f"You are roleplaying as {character}. Reply in the tone and style of this character. The user says: '{prompt}'"
                )
                
                st.markdown(f"**{character}**: {reply.text}")
            except:
                st.error("Oops! Something went wrong.")
    st.button("🔙 Back to Home", on_click=lambda: st.session_state.update({"page": "home"}))

# --- Hug Section ---
elif st.session_state.page == "hug":
    st.title("🤗 Virtual Hug Station")
    st.write("Sometimes, all we need is a warm hug. 💙")
    st.image("virtual hug.gif", width=900)
    st.markdown("**You're not alone. We're here with you.** 💙")
    st.button("🔙 Back to Home", on_click=lambda: st.session_state.update({"page": "home"}))

# --- Daily Positivity ---
elif st.session_state.page == "positivity":
    st.title("🧘 Yoga Asanas ")
    st.write("🌞 Daily Positivity")

    # Step 1: Show a positive quote
    try:
        quote = model.generate_content("Give me a short, cheerful positive quote for today.")
        st.success(quote.text)
    except:
        st.error("Oops! Couldn't fetch a quote.")

    st.divider()

    # Step 2: Ask for user's feeling
    feeling = st.text_input("How are you feeling right now? (e.g., anxious, tired, happy, sad)")

    if feeling:
        try:
            prompt = (
                f"The user is feeling '{feeling}'. Suggest 2 or 3 simple yoga asanas (postures) "
                "suitable for their current mood, along with a 1-line reason why each helps."
            )
            response = model.generate_content(prompt)
            st.subheader("🧘 Yoga Asanas Just for You:")
            st.info(response.text)
        except:
            st.error("Couldn't fetch yoga suggestions at the moment. Try again later.")

    st.button("🔙 Back to Home", on_click=lambda: st.session_state.update({"page": "home"}))


# --- Bubble Game Placeholder ---

