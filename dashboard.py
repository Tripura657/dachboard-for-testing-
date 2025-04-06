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

# Optional: Check query params to switch pages via link
query_params = st.experimental_get_query_params()
if "page" in query_params:
    st.session_state.page = query_params["page"][0]

# --- Home Dashboard Layout ---
if st.session_state.page == "home":
    st.title("\U0001F499 Mental Health Dashboard")

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
        </style>

        <div class="dashboard-grid">
            <div class="dashboard-item">
                <a href="/?page=motivation">
                    <img src="https://i.ibb.co/XzTc1mF/motivation.png" alt="Motivational Chatbot" />
                    <p>Motivational Chatbot</p>
                </a>
            </div>
            <div class="dashboard-item">
                <a href="/?page=chatbot">
                    <img src="https://i.ibb.co/4YsXM0x/mental-health-chat.png" alt="Mental Health Chat" />
                    <p>Mental Health Chat</p>
                </a>
            </div>
            <div class="dashboard-item">
                <a href="/?page=character_chat">
                    <img src="https://i.ibb.co/jv3B6QZ/character.png" alt="Talk with Character" />
                    <p>Talk with a Character</p>
                </a>
            </div>
            <div class="dashboard-item">
                <a href="/?page=hug">
                    <img src="https://i.ibb.co/qkFV1xq/hug.png" alt="Take a Hug" />
                    <p>Take a Hug</p>
                </a>
            </div>
            <div class="dashboard-item">
                <a href="/?page=positivity">
                    <img src="https://i.ibb.co/0jkpsZC/yoga.png" alt="Yoga Asanas" />
                    <p>Yoga Asanas</p>
                </a>
            </div>
        </div>
    """, unsafe_allow_html=True)

# --- Motivational Chatbot Logic ---
if st.session_state.page == "motivation":
    st.title("\U0001F4AC Motivational Story Chatbot")
    st.write("Tell me what's on your mind, and I’ll share a story that might lift you up! \U0001F499")
    situation = st.text_input("\U0001F331 Describe your current situation:")
    if situation:
        try:
            story_response = model.generate_content(
                f"You are a motivational storyteller. The user is going through this: '{situation}'. Please respond with an inspiring short story that helps them feel strong and positive."
            )
            story = story_response.text
            st.subheader("\U0001F4D6 Here's a story for you:")
            st.success(story)
        except Exception as e:
            st.error("Sorry, something went wrong. Please try again later.")
    st.button("\U0001F519 Back to Home", on_click=lambda: st.session_state.update({"page": "home"}))

# --- Mental Health Chatbot Logic ---
elif st.session_state.page == "chatbot":
    st.title("\U0001F499 Mental Health Support Chatbot")
    query = st.text_input("Hello! I'm here to listen and support you. Feel free to share your thoughts, and I'll try my best to help. Remember, you're not alone! \U0001F499")
    if query:
        try:
            response = model.generate_content(
                f"You are a mental health chatbot trained to provide comforting and understanding responses. The user says: '{query}'"
            )
            st.success(response.text)
        except:
            st.error("Oops! Something went wrong.")
    st.button("\U0001F519 Back to Home", on_click=lambda: st.session_state.update({"page": "home"}))

# --- Character Chat Logic ---
elif st.session_state.page == "character_chat":
    st.title("\U0001F3AD Talk with Your Favorite Character")
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
    st.button("\U0001F519 Back to Home", on_click=lambda: st.session_state.update({"page": "home"}))

# --- Hug Section ---
elif st.session_state.page == "hug":
    st.title("\U0001F917 Virtual Hug Station")
    st.write("Sometimes, all we need is a warm hug. \U0001F499")
    st.image("virtual hug.gif", width=900)
    st.markdown("**You're not alone. We're here with you.** \U0001F499")
    st.button("\U0001F519 Back to Home", on_click=lambda: st.session_state.update({"page": "home"}))

# --- Daily Positivity ---
elif st.session_state.page == "positivity":
    st.title("\U0001F9D8 Yoga Asanas ")
    st.write("\U0001F31E Daily Positivity")

    try:
        quote = model.generate_content("Give me a short, cheerful positive quote for today.")
        st.success(quote.text)
    except:
        st.error("Oops! Couldn't fetch a quote.")

    st.divider()

    feeling = st.text_input("How are you feeling right now? (e.g., anxious, tired, happy, sad)")
    if feeling:
        try:
            prompt = (
                f"The user is feeling '{feeling}'. Suggest 2 or 3 simple yoga asanas (postures) "
                "suitable for their current mood, along with a 1-line reason why each helps."
            )
            response = model.generate_content(prompt)
            st.subheader("\U0001F9D8 Yoga Asanas Just for You:")
            st.info(response.text)
        except:
            st.error("Couldn't fetch yoga suggestions at the moment. Try again later.")

    st.button("\U0001F519 Back to Home", on_click=lambda: st.session_state.update({"page": "home"}))
