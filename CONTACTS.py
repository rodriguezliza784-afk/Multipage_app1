import streamlit as st

st.set_page_config(page_title="Contact", page_icon="📞", layout="centered")

# ---------- CSS (Grey Background) ----------
st.markdown("""
<style>
/* Whole page background */
.stApp {
    background-color: #dcdfe3;
}

/* Center card */
.contact-card {
    background: #ffffff;
    padding: 30px;
    border-radius: 15px;
    box-shadow: 0 10px 25px rgba(0,0,0,0.08);
}

/* Titles */
.title {
    text-align: center;
    font-size: 40px;
    font-weight: bold;
    color: #343a40;
    margin-bottom: 10px;
}

.subtitle {
    text-align: center;
    color: #495057;
    margin-bottom: 25px;
}

/* Social box */
.social {
    margin-top: 25px;
    padding: 15px;
    background: #e9ecef;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

# ---------- Header ----------
st.markdown('<div class="title">📞 Get In Touch</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Feel free to send get to know what you need message anytime!</div>', unsafe_allow_html=True)

# ---------- Card ----------
st.markdown('<div class="contact-card">', unsafe_allow_html=True)

name = st.text_input("👤 Your Name")
email = st.text_input("📧 Your Email")
message = st.text_area("💬 Your Message")

if st.button("Send Message"):
    if name and email and message:
        st.success("Message sent successfully! ✅")
    else:
        st.error("Please fill all fields.")

# ---------- Social Links ----------
st.markdown('<div class="social">', unsafe_allow_html=True)
st.markdown("### 🌐 Social Links")
st.write("📧 **Gmail:** rodriguezliza784@gmail.com")
st.write("📘 **Facebook:** https://www.facebook.com/liza.rodriguez.521854")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)