from flask import Flask, jsonify, render_template
import random

app = Flask(__name__)

subjects = [
    "A mysterious cat",
    "The Prime Minister",
    "A group of students",
    "An alien",
    "A famous actor",
    "A robot"
]

actions = [
    "was dancing",
    "was reading a book",
    "started singing",
    "was secretly practicing yoga",
    "was giving free advice",
    "was coding all night"
]

places = [
    "in Paris",
    "at the Red Fort",
    "inside a shopping mall",
    "on the moon",
    "in a classroom",
    "at a railway station"
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate")
def generate():
    headline = f"BREAKING NEWS: {random.choice(subjects)} {random.choice(actions)} {random.choice(places)}"
    return jsonify({"headline": headline})

if __name__ == "__main__":
    app.run(debug=True)
