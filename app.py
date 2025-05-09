from flask import Flask, render_template, request
from model import get_answer  # Import the get_answer function from model.py

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/result", methods=["POST"])
def result():
    video_id = request.form["video_id"]
    question = request.form["question"]
    print(f"Video ID: {video_id}, Question: {question}")  # Debug line
    answer = get_answer(video_id, question)
    print(f"Answer: {answer}")  # Debug line
    return render_template("result.html", answer=answer)  # Return the result to result.html

if __name__ == "__main__":
    app.run(debug=True)
