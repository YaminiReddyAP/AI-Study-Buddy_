from flask import Flask, render_template, request
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# NLTK downloads
nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)

app = Flask(__name__)

def study_buddy(text):
    explanation = "Simple explanation: " + text
    summary = "Summary: " + text[:150]
    quiz = [f"What is related to '{w}'?" for w in text.split()[:5]]
    return explanation, summary, quiz

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_input = request.form.get("user_input")
        explanation, summary, quiz = study_buddy(user_input)
        return render_template(
            "index.html",
            explanation=explanation,
            summary=summary,
            quiz=quiz
        )
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
