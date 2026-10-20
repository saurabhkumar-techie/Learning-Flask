from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    marks = {
        "Saurabh": 99,
        "John": 45,
        "Mark": 45,
        "Jeff": 67,
        "Alexa": 90,
        "Lily": 100,
        "Harry": 1
    }
    return render_template("index.html", marks=marks)


app.run(debug=True)