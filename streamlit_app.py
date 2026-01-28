import streamlit as st

# Page configuration
st.set_page_config(
    page_title="AI Study Buddy",
    page_icon="🤖",
    layout="centered"
)

# App title and description
st.title("🤖 AI Study Buddy")
st.write(
    "Upload notes, simplify concepts, generate summaries, and create quick quiz questions instantly."
)

# Input text area
user_text = st.text_area(
    "Enter your study text here...",
    height=180,
    placeholder="Paste your notes here...",
    key="study_input"
)

# Button logic
if st.button("Explain Simply"):
    if user_text.strip() == "":
        st.warning("Please enter some text to analyze.")
    else:
        # --- SIMPLE SENTENCE SPLIT (NO NLTK) ---
        sentences = user_text.replace("?", ".").replace("!", ".").split(".")

        st.success("📘 Simplified Explanation")

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

        # --- SUMMARY ---
        st.subheader("📝 Summary")
        st.write(user_text[:200] + ("..." if len(user_text) > 200 else ""))

        # --- QUIZ ---
        st.subheader("❓ Quick Quiz")
        words = user_text.split()[:5]
        for w in words:
            st.write(f"- What is related to **{w}**?")