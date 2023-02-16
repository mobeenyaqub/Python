from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def home():
    return "hello"


@app.route('/guess/<name>')
def guess(name):
    gender = requests.get(f"https://api.genderize.io?name={name}").json()
    age = requests.get(f"https://api.agify.io?name={name}").json()
    print(f"Name: {name}")
    print(f"Gender: {gender}")
    print(f"Age: {age}")
    return render_template("index.html", name=name, age=age, gender=gender)


if __name__ == "__main__":
    app.run(debug=True)