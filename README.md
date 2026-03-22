import streamlit as st
import os
import json
from dotenv import load_dotenv
from groq import Groq

# 1. Force a page title to see if it's working
st.set_page_config(page_title="Hindsight Mentor")

# 2. Load the secrets
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

# --- STEP 4: AUTHENTICATION ---
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.title("🔐 Hindsight Mentor Login")
    user_pass = st.text_input("Enter Secret Key", type="password")
    if st.button("Unlock Mentor"):
        if user_pass == "pushkarni2026": # Your secret key
            st.session_state.logged_in = True
            st.rerun()
        else:
            st.error("Access Denied")
    st.stop() # Prevents the rest of the app from loading
    # --- AT THE BOTTOM OF YOUR SIDEBAR SECTION ---
with st.sidebar:
    st.markdown("---") # This adds a clean separation line
    
    # ADD THESE LINES HERE:
    if st.button("🔒 Logout and Lock Memory"):
        st.session_state.logged_in = False
        st.success("Logged out successfully!")
        time.sleep(1) # Gives the user a second to see the message
        st.rerun()

# 3. Simple UI Elements
st.title("🤖 My AI Coding Mentor")
st.write("If you see this, the 'Face' is working!")

# 4. Check if Memory exists
try:
    with open('memory.json', 'r') as file:
        data = json.load(file)
    st.sidebar.success(f"Connected to {data['student_name']}'s Memory")
except Exception as e:
    st.sidebar.error("Could not find memory.json")

# 5. Simple Chat Input
user_input = st.chat_input("Say hello to your mentor...")

if user_input:
    st.write(f"You said: {user_input}")
    # This will show the AI is thinking
    with st.spinner("Thinking..."):
        client = Groq(api_key=api_key)
        chat_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": user_input}],
            model="llama-3.1-8b-instant",
        )
        st.info(chat_completion.choices[0].message.content)
        # Create a button to 'Save a Lesson'
with st.sidebar:
    st.subheader("Add New Hindsight")
    new_lesson = st.text_input("What did you learn today?")
    if st.button("Save Lesson"):
        # This code updates your JSON file
        memory_data['lessons_learned'].append(new_lesson)
        with open('memory.json', 'w') as f:
            json.dump(memory_data, f)
        st.success("Hindsight Saved!")
        st.rerun()
        # Create an 'Auto-Summarize' feature in the sidebar
with st.sidebar:
    st.divider()
    st.header("🧠 AI Auto-Hindsight")
    if st.button("Analyze my Progress"):
        # We ask the AI to summarize the current chat session
        summary_prompt = "Based on our current chat, what is the #1 technical lesson the student learned? Summarize it in 1 short sentence."
        
        # Simple AI call
        summary_resp = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": summary_prompt}]
        )
        lesson = summary_resp.choices[0].message.content
        st.info(f"Suggested Lesson: {lesson}")
        
        # Save button for the suggestion
        if st.button("Confirm & Save to Memory"):
            memory_data['lessons_learned'].append(lesson)
            with open('memory.json', 'w') as f:
                json.dump(memory_data, f)
            st.success("Memory Updated!")
            # Add this near the top of app.py
# Copy and paste this to replace the broken styling section
import streamlit as st

# This function injects CSS into your app
def local_css():
    st.markdown("""
        <style>
        /* This changes the main background to a clean professional grey */
        .stApp {
            background-color: #f0f2f6;
        }

        /* This makes the chat bubbles look like modern rounded cards */
        [data-testid="stChatMessage"] {
            background-color: white !important;
            border-radius: 15px !important;
            padding: 15px !important;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1) !important;
            border: 1px solid #e1e4e8 !important;
            margin-bottom: 10px !important;
        }

        /* This styles the sidebar to look distinct */
        section[data-testid="stSidebar"] {
            background-color: #ffffff !important;
            border-right: 2px solid #4CAF50;
        }
        </style>
    """, unsafe_allow_html=True)

# Call the function to apply the styles
local_css()
st.markdown("""
<style>
    /* 1. Frosted Glass Background */
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        background-attachment: fixed;
    }

    /* 2. Chat Bubbles with Glass Effect */
    [data-testid="stChatMessage"] {
        background: rgba(255, 255, 255, 0.2) !important;
        backdrop-filter: blur(10px) !important;
        -webkit-backdrop-filter: blur(10px) !important;
        border-radius: 20px !important;
        border: 1px solid rgba(255, 255, 255, 0.3) !important;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37) !important;
        color: white !important;
        margin-bottom: 15px !important;
    }

    /* 3. Make User & Assistant text readable on dark background */
    .stMarkdown p { color: white !important; font-size: 1.1rem; }
    
    /* 4. Sidebar Professional Look */
    section[data-testid="stSidebar"] {
        background-color: rgba(255, 255, 255, 0.05) !important;
        backdrop-filter: blur(5px);
    }
</style>
""", unsafe_allow_html=True)
# Inside your sidebar in app.py
with st.sidebar:
    st.header("⚙️ Mentor Settings")
    
    # Let the user choose the 'Vibe' of the mentor
    mentor_vibe = st.select_slider(
        "Select Mentor Tone:",
        options=["Strict", "Balanced", "Friendly", "Motivational"]
    )
    
    # A progress bar for the student's journey
    st.write("---")
    st.write("📈 **Your Progress**")
    progress = st.progress(65) # You can link this to memory.json later
    st.caption("65% of Python Basics completed!")
    
    # Button to clear history
    if st.button("🗑️ Reset Memory"):
        st.warning("Are you sure?")
       
# 1. First, make sure you are inside a markdown block
st.markdown("""
<style>
    /* Paste your animation code HERE */
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    [data-testid="stChatMessage"] {
        animation: fadeInUp 0.5s ease-out forwards;
    }
</style>
""", unsafe_allow_html=True)
st.markdown("""
<style>
    /* 1. Main Background: Deep Slate */
    .stApp {
        background-color: #0f172a;
        color: #f8fafc;
    }

    /* 2. Sidebar: Darker & Cleaner */
    section[data-testid="stSidebar"] {
        background-color: #1e293b !important;
        border-right: 1px solid #334155;
    }

    /* 3. Elegant Chat Bubbles (Glassmorphism) */
    [data-testid="stChatMessage"] {
        background-color: rgba(30, 41, 59, 0.7) !important;
        border: 1px solid #334155 !important;
        border-radius: 15px !important;
        padding: 20px !important;
        margin-bottom: 10px !important;
        backdrop-filter: blur(8px);
        animation: fadeInUp 0.5s ease-out; /* Your micro-animation! */
    }

    /* 4. Text & Titles */
    h1, h2, h3, p {
        color: #f8fafc !important;
        font-family: 'Inter', sans-serif;
    }

    /* 5. Custom "Save" Button Styling */
    div.stButton > button {
        background-color: #10b981 !important; /* Emerald Green */
        color: white !important;
        border-radius: 10px !important;
        border: none !important;
        transition: 0.3s;
    }
    div.stButton > button:hover {
        background-color: #059669 !important;
        transform: scale(1.05);
    }

    /* Animation Keyframes */
    @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }
</style>
""", unsafe_allow_html=True)
import time

def typewriter(text, delay=0.02):
    # This creates a placeholder that we update in a loop
    container = st.empty()
    displayed_text = ""
    for char in text:
        displayed_text += char
        container.markdown(displayed_text)
        time.sleep(delay)
        st.markdown("""
<style>
    /* 1. The Main Frame */
    .stApp {
        background: radial-gradient(circle at top right, #1e293b, #0f172a);
        color: #e2e8f0;
    }

    /* 2. Chat Bubbles: Frosted Glass */
    [data-testid="stChatMessage"] {
        background: rgba(30, 41, 59, 0.5) !important;
        backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 20px !important;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3) !important;
        animation: slideUp 0.6s ease-out;
    }

    /* 3. The "Save Lesson" Button */
    div.stButton > button {
        background: linear-gradient(90deg, #10b981 0%, #059669 100%) !important;
        color: white !important;
        border: none !important;
        padding: 10px 24px !important;
        font-weight: bold !important;
        border-radius: 12px !important;
        transition: 0.3s all ease;
    }
    div.stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(16, 185, 129, 0.4);
    }

    /* 4. Animations */
    @keyframes slideUp {
        from { opacity: 0; transform: translateY(30px); }
        to { opacity: 1; transform: translateY(0); }
    }
</style>
""", unsafe_allow_html=True)
        # When the AI gives a response
if prompt := st.chat_input("Ask your mentor..."):
    # ... (Your logic to get the 'response' from mentor.py) ...
    
    with st.chat_message("assistant"):
        typewriter(response) # This triggers the typing animation
        # --- STEP 6: PROGRESS DASHBOARD ---
from mentor import get_stats, get_recent_lessons

lessons_count, student_name = get_stats()

st.subheader(f"🚀 {student_name}'s Learning Journey")
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Lessons Learned", lessons_count, "+1 Today")
with col2:
    st.metric("Mentor Status", "Expert" if lessons_count > 5 else "Beginner")
with col3:
    st.metric("AI Model", "Llama-3.1")

st.write("---")
# --- STEP 7: LESSON HISTORY ---
with st.expander("📚 View your Recent Coding Lessons"):
    recent = get_recent_lessons()
    for i, lesson in enumerate(reversed(recent)):
        st.write(f"{i+1}. {lesson}")
        # --- INSIDE YOUR SIDEBAR ---
with st.sidebar:
    st.success("💡 **Tip of the Day**")
    st.caption("Always use Virtual Environments (venv) to keep your project libraries organized and avoid version conflicts!")
        
