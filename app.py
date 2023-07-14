# app.py
from flask import Flask, render_template
import random

max_score = 100
test_name = "Python Challenge"
students = [
    {"name": "Devyani",  "score": random.randint(0,100)},
    {"name": "Mia", "score": random.randint(0,100)},
    {"name": "Kian", "score": random.randint(0,100)},
    {"name": "Amit", "score": random.randint(0,100)},
    {"name": "Ketan", "score": random.randint(0,100)},
]

def names():
    file = "names.txt"
    file_list = []
    try:
        with open(file, 'r') as f:
            for line in f:
                file_list.append(line.strip())
    except FileNotFoundError:
        print(f"File '{file}' doesn't exist, will exit")
        exit()
    return file_list


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("base.html", title="Jinja and Flask")

@app.route("/results")
def results():
    context = {
        "title": "Results",
        "students": students,
        "test_name": test_name,
        "max_score": max_score,
    }
    return render_template("results.html", **context)

# ToDo get following function working, currently broken
# @app.route("/pickmaster")
# def pickmaster():
#     return render_template("master.html", title="Scrum Master")


if __name__ == "__main__":
    app.run(debug=True, port=8000)