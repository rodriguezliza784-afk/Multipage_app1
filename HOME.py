import streamlit as st

st.set_page_config(page_title="My Portfolio", page_icon="🌐", layout="wide")

# ---------- Dark Mode Toggle ----------
dark_mode = st.toggle("🌙 Dark Mode")

# ---------- Theme Colors ----------
if dark_mode:
    bg = "#121212"
    text = "#f1f1f1"
    card_text = "#ffffff"
    shadow = "rgba(255,255,255,0.1)"
else:
    bg = "#e9ecef"
    text = "#2c3e50"
    card_text = "white"
    shadow = "rgba(0,0,0,0.1)"

# ---------- Custom CSS ----------
st.markdown(f"""
<style>
.stApp {{
    background-color: {bg};
}}

.main-title {{
    font-size: 52px;
    font-weight: bold;
    color: {text};
    text-align: center;
}}

.subtitle {{
    font-size: 22px;
    text-align: center;
    color: {text};
    margin-bottom: 30px;
}}

.card {{
    padding: 25px;
    border-radius: 15px;
    box-shadow: 0 8px 20px {shadow};
    margin-bottom: 25px;
    color: {card_text};
}}

.card1 {{ background: #6c757d; }}
.card2 {{ background: #495057; }}
.card3 {{ background: #343a40; }}
.card4 {{ background: #adb5bd; color: #2c3e50; }}
.card5 {{ background: #868e96; }}

.card-title {{
    font-size: 24px;
    font-weight: bold;
    margin-bottom: 10px;
}}
</style>
""", unsafe_allow_html=True)

# ---------- Header ----------
st.markdown('<div class="main-title">🎇 Welcome to My Personal Portfolio</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Hello! I’m Liza Rodriguez 👋</div>', unsafe_allow_html=True)

# ---------- Profile Picture ----------
col1, col2, col3 = st.columns([1,2,1])
with col2:
    st.image("IMAGE.jpg", caption="My Profile", width=200)

st.write("")

# ---------- Cards Layout ----------
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="card card1">
        <div class="card-title">🏠 Home</div>
        Welcome to my portfolio. Explore and enjoy!
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card card3">
        <div class="card-title">🛠 Skills</div>
        Discover the technologies and tools I use.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card card5">
        <div class="card-title">📞 Contact</div>
        You need something? Let’s connect for collaboration and ideas.
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card card2">
        <div class="card-title">👩‍💻 About Me</div>
        Learn more about my background and passion.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card card4">
        <div class="card-title">🚀 Projects</div>
        Check out the projects that I’ve built.
    </div>
    """, unsafe_allow_html=True)