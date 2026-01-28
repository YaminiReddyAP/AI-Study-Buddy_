import streamlit as st
import nltk
from nltk.tokenize import sent_tokenize

# Download once (safe even if already downloaded)
nltk.download("punkt")
nltk.download("punkt_tab")

st.set_page_config(page_title="AI Study Buddy")

st.title("🤖 AI Study Buddy")
st.write("Upload notes, simplify concepts, and generate study materials instantly.")

# INPUT TEXT AREA (UNIQUE KEY)
user_text = st.text_area(
    "Enter your study text here...",
    height=150,
    key="study_input"
)

# BUTTON (LOGIC IS HERE 👇)
if st.button("Explain Simply"):
    sentences = sent_tokenize(user_text)

    st.success("Simplified Explanation:")

    for s in sentences:
        simple = s.replace("cybersecurity", "online safety") \
                  .replace("enterprise level", "companies") \
                  .replace("risk management strategy", "ways to reduce risk")

        st.write("🔹", simple)
