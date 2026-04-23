import streamlit as st

st.set_page_config(page_title="Skills", page_icon="🛠", layout="wide")

# ---------- Custom CSS ----------
st.markdown("""
<style>
.stApp {
    background-color: #e9ecef;
}

.skill-card {
    background-color: #ffffff;
    padding: 25px;
    border-radius: 15px;
    box-shadow: 0 6px 18px rgba(0,0,0,0.08);
    margin-bottom: 25px;
}

.skill-title {
    font-size: 26px;
    font-weight: bold;
    color: #2c3e50;
    margin-bottom: 15px;
}

.skill-label {
    font-weight: 600;
    margin-top: 10px;
    color: #495057;
}
</style>
""", unsafe_allow_html=True)

st.title("🛠 My Skills")

# ---------- Programming Card ----------
st.markdown('<div class="skill-card">', unsafe_allow_html=True)
st.markdown('<div class="skill-title">💻 Programming</div>', unsafe_allow_html=True)

st.markdown('<div class="skill-label">Adobe Editing — 80%</div>', unsafe_allow_html=True)
st.progress(80)

st.markdown('<div class="skill-label">Python — 70%</div>', unsafe_allow_html=True)
st.progress(70)

st.markdown('<div class="skill-label">PHP — 75%</div>', unsafe_allow_html=True)
st.progress(55)

st.markdown('</div>', unsafe_allow_html=True)

# ---------- Design Card ----------
st.markdown('<div class="skill-card">', unsafe_allow_html=True)
st.markdown('<div class="skill-title">🎨 Design</div>', unsafe_allow_html=True)

st.markdown('<div class="skill-label">Adobe / UI Design — 45%</div>', unsafe_allow_html=True)
st.progress(50)

st.markdown('</div>', unsafe_allow_html=True)

# ---------- Tools Card ----------
st.markdown('<div class="skill-card">', unsafe_allow_html=True)
st.markdown('<div class="skill-title">🧰 Tools</div>', unsafe_allow_html=True)

st.write("✔ GitHub")
st.write("✔ VS Code")
st.write("✔ Streamlit")

st.markdown('</div>', unsafe_allow_html=True)