import streamlit as st

# Page setup
st.set_page_config(page_title="My Projects", page_icon="🎮", layout="centered")

# ---------- Custom Grey Background & Styling ----------
st.markdown("""
    <style>
        body {
            background-color: #e6e6e6;
        }
        .stApp {
            background-color: #e6e6e6;
        }
        .title {
            text-align: center;
            font-size: 40px;
            font-weight: bold;
            color: #333333;
            margin-bottom: 20px;
        }
        .stExpander {
            background-color: #ffffff;
            border-radius: 10px;
            border: 1px solid #cccccc;
        }
    </style>
""", unsafe_allow_html=True)

# ---------- Title ----------
st.markdown('<div class="title">🎯 My Creative Python Projects</div>', unsafe_allow_html=True)

# ---------- Projects ----------
projects = {
    "🏓 Ping-Pong Game": """
A fun 2-player arcade-style game inspired by table tennis.  
Includes smooth paddle controls, realistic ball movement, and live score tracking.
""",

    "🧠 Trivia Quiz Game": """
An engaging quiz application that challenges users with different questions.  
Tracks scores, gives instant feedback, and makes learning interactive.
""",

    "🏥 Clinic Management System": """
A digital system for managing patient records and appointments.  
Helps organize schedules, store treatments, and generate useful reports.
"""
}

# ---------- Display Projects ----------
for name, desc in projects.items():
    with st.expander(name):
        st.write(desc)