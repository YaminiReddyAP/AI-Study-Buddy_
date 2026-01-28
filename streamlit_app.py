import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Study Buddy",
    page_icon="🤖",
    layout="centered"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
.main {
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
    color: white;
}
.card {
    background-color: #1f2933;
    padding: 20px;
    border-radius: 15px;
    margin-top: 20px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.4);
}
.highlight {
    color: #38bdf8;
    font-weight: bold;
}
hr {
    border: 1px solid #374151;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown("""
<div class="card">
    <h1>🤖 AI Study Buddy</h1>
    <p class="highlight">
        Upload notes, simplify concepts, generate summaries, and create quick quiz questions instantly.
    </p>
</div>
""", unsafe_allow_html=True)

# ---------------- INPUT ----------------
st.markdown("<div class='card'>", unsafe_allow_html=True)

user_text = st.text_area(
    "📘 Enter your study text here",
    height=180,
    placeholder="Paste your notes here...",
    key="study_input"
)

st.markdown("</div>", unsafe_allow_html=True)

# ---------------- BUTTON ACTION ----------------
if st.button("✨ Explain Simply"):
    if user_text.strip() == "":
        st.warning("⚠️ Please enter some study text.")
    else:
        # Sentence split (simple & safe)
        sentences = user_text.replace("?", ".").replace("!", ".").split(".")

        # ---------------- SIMPLIFIED EXPLANATION ----------------
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.subheader("📘 Simplified Explanation")

        for s in sentences:
            s = s.strip()
            if s:
                simple = (
                    s.lower()
                    .replace("cybersecurity", "online safety")
                    .replace("enterprise level", "companies")
                    .replace("risk management strategy", "ways to reduce risk")
                )
                st.write("🔹", simple.capitalize())

        st.markdown("</div>", unsafe_allow_html=True)

        # ---------------- SUMMARY ----------------
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.subheader("📝 Summary")

        summary = user_text[:250] + ("..." if len(user_text) > 250 else "")
        st.write(summary)

        st.markdown("</div>", unsafe_allow_html=True)

        # ---------------- QUIZ ----------------
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.subheader("❓ Quick Quiz")

        words = user_text.split()[:5]
        for i, w in enumerate(words, start=1):
            st.write(f"{i}. What is related to **{w}**?")

        st.markdown("</div>", unsafe_allow_html=True)

# ---------------- FOOTER ----------------
st.markdown("""
<hr>
<p style="text-align:center; font-size:14px; color:#9ca3af;">
Built with ❤️ using Streamlit | AI Study Buddy Project
</p>
""", unsafe_allow_html=True)
