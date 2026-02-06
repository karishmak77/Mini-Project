from flask import Flask, jsonify, render_template
import random

app = Flask(__name__)

quotes = [
    {"text": "Believe you can and you're halfway there.", "author": "Theodore Roosevelt"},
    {"text": "Stay hungry, stay foolish.", "author": "Steve Jobs"},
    {"text": "Success is not final, failure is not fatal: It is the courage to continue that counts.", "author": "Winston Churchill"},
    {"text": "Code is like humor. When you have to explain it, it’s bad.", "author": "Cory House"},
    {"text": "First, solve the problem. Then, write the code.", "author": "John Johnson"},
    {"text": "Dream big. Start small. Act now.", "author": "Robin Sharma"},
    {"text": "The best way to predict the future is to invent it.", "author": "Alan Kay"},
    {"text": "Don’t watch the clock; do what it does. Keep going.", "author": "Sam Levenson"},
    {"text": "Simplicity is the soul of efficiency.", "author": "Austin Freeman"},
    {"text": "Your limitation—it’s only your imagination.", "author": "Unknown"},
    {"text": "Push yourself, because no one else is going to do it for you.", "author": "Unknown"},
    {"text": "Great things never come from comfort zones.", "author": "Unknown"}
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate")
def generate():
    return jsonify(random.choice(quotes))

if __name__ == "__main__":
    app.run(debug=True)

