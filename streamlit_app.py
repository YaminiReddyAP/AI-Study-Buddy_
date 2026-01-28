import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI-Powered Study Buddy",
    page_icon="🤖",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
/* Background */
.stApp {
    background: linear-gradient(180deg, #0b2d3a 0%, #163f52 100%);
    color: white;
}

/* Center container */
.container {
    max-width: 900px;
    margin: auto;
    padding-top: 60px;
}

/* Title */
.title {
    font-size: 42px;
    font-weight: 700;
    margin-bottom: 10px;
}

/* Subtitle */
.subtitle {
    font-size: 18px;
    opacity: 0.85;
    margin-bottom: 30px;
}

/* Text area */
textarea {
    border-radius: 14px !important;
    padding: 18px !important;
    font-size: 16px !important;
}

/* Button */
.stButton > button {
    background-color: #00aaff;
    color: white;
    font-size: 16px;
    padding: 10px 26px;
    border-radius: 10px;
    border: none;
    margin-top: 15px;
}

.stButton > button:hover {
    background-color: #0095dd;
}
</style>
""", unsafe_allow_html=True)

# ---------------- CONTENT ----------------
st.markdown("<div class='container'>", unsafe_allow_html=True)

st.markdown(
    "<div class='title'>🎓 AI-Powered Study Buddy</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='subtitle'>Upload notes, simplify concepts, and generate study materials instantly.</div>",
    unsafe_allow_html=True
)

user_text = st.text_area(
    "Enter your study text here...",
    height=220,
    placeholder="Enter your study text here..."
)

if st.button("Explain Simply"):
    if user_text.strip() == "":
        st.warning("Please enter some study text.")
    else:
        st.markdown("### 📘 Simplified Explanation")

        sentences = user_text.replace("?", ".").replace("!", ".").split(".")

        for s in sentences:
            s = s.strip()
            if s:
                simple = (
                    s.lower()
                    .replace("cybersecurity", "online safety")
                    .replace("enterprise level", "companies")
                    .replace("risk management strategy", "ways to reduce risk")
                )
                st.write("•", simple.capitalize())

st.markdown("</div>", unsafe_allow_html=True)