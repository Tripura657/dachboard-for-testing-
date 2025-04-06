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

# --- Motivational Chatbot Logic ---
if st.session_state.page == "motivation":
    st.title("💬 Motivational Story Chatbot")
    st.write("Tell me what's on your mind, and I’ll share a story that might lift you up! 💙")
    situation = st.text_input("Describe your current situation:")
    if situation:
        try:
            story_response = model.generate_content(
                f"You are a motivational storyteller. The user is going through this: '{situation}'. Please respond with an inspiring short story that helps them feel strong and positive."
            )
            st.success(story_response.text)
        except Exception as e:
            st.error("Sorry, something went wrong. Please try again later.")
    st.button("🔙 Back to Home", on_click=lambda: st.session_state.update({"page": "home"}))

# --- Mental Health Chatbot Logic ---
elif st.session_state.page == "chatbot":
    st.title("🧠 Mental Health Chat")
    query = st.text_input("What's on your mind?")
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
                st.image(characters[character], use_container_width=True)
                st.markdown(f"**{character}**: {reply.text}")
            except:
                st.error("Oops! Something went wrong.")
    st.button("🔙 Back to Home", on_click=lambda: st.session_state.update({"page": "home"}))

# --- Hug Section ---
elif st.session_state.page == "hug":
    st.title("🤗 Virtual Hug")
    emotion = st.text_input("How are you feeling?")
    if emotion.lower() in ["sad", "depressed", "lonely", "anxious"]:
        st.image("https://media.giphy.com/media/l2JHRhAtnJSDNJ2py/giphy.gif", use_container_width=True)
        st.success("You’re not alone. Here’s a big warm hug for you 🤗")
    elif emotion:
        st.balloons()
        st.success("We're happy you're feeling good! Keep shining ✨")
    st.button("🔙 Back to Home", on_click=lambda: st.session_state.update({"page": "home"}))

# --- Daily Positivity ---
elif st.session_state.page == "positivity":
    st.title("🌞 Daily Positivity")
    try:
        quote = model.generate_content("Give me a short, cheerful positive quote for today.")
        st.success(quote.text)
    except:
        st.error("Oops! Couldn't fetch a quote.")
    st.button("🔙 Back to Home", on_click=lambda: st.session_state.update({"page": "home"}))

# --- Bubble Game Placeholder ---
elif st.session_state.page == "bubble_game":
    st.title("🫧 Bubble Game")
    feeling = st.text_input("Type how you're feeling:")
    if feeling.lower() in ["sad", "angry", "tired", "lonely"]:
        st.image("https://media.giphy.com/media/3o7abB06u9bNzA8lu8/giphy.gif", use_container_width=True)
        st.success("Pop! That feeling is fading. You're doing great ❤️")
    elif feeling:
        st.balloons()
        st.success("Yay! Celebrate your good mood 🎉")
    st.button("🔙 Back to Home", on_click=lambda: st.session_state.update({"page": "home"}))
