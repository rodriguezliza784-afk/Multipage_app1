import streamlit as st

st.set_page_config(page_title="About Me", page_icon="🧑‍💻", layout="centered")

# ---------- CSS (Grey Theme) ----------
st.markdown("""
<style>
.stApp {
    background-color: #e9ecef;
}

.card {
    background: white;
    padding: 25px;
    border-radius: 15px;
    box-shadow: 0 8px 20px rgba(0,0,0,0.1);
    margin-bottom: 20px;
}

.title {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
    color: #343a40;
}

.subtitle {
    text-align: center;
    color: #6c757d;
    margin-bottom: 20px;
}

.section-title {
    font-size: 22px;
    font-weight: bold;
    color: #343a40;
    margin-top: 15px;
}
</style>
""", unsafe_allow_html=True)

# ---------- Header ----------
st.markdown('<div class="title">🧑‍💻 About Me</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Computer Science Student | Future Developer</div>', unsafe_allow_html=True)

# ---------- Card ----------
st.markdown('<div class="card">', unsafe_allow_html=True)

st.write("""
As a Computer Science learner, I enjoy building software systems and applications that solve real-world problems.  
I focus on writing efficient code and designing intuitive user interfaces for better usability.
""")

st.markdown('<div class="section-title">🎓 Education</div>', unsafe_allow_html=True)
st.write("• Bachelor of Science in Computer Science")
st.write("• Trainings in Web Development & Software Development")

st.markdown('<div class="section-title">🎯 Goals</div>', unsafe_allow_html=True)
st.write("• Become a Full Stack Developer")
st.write("• Build impactful tech solutions that solve real-world problems")

st.markdown('</div>', unsafe_allow_html=True)