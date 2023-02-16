from flask import Flask, render_template
import random
import requests
from datetime import datetime

from jinja2 import UndefinedError

app = Flask(__name__)


# templating language
@app.route('/')
def home():
    year = datetime.today().year
    random_number = random.randint(1, 10)
    return render_template("index.html", num=random_number, year=year)


@app.route('/blog/<num>')
def get_blog(num):
    response = requests.get("https://api.npoint.io/4c7de63525b1e6b2c0a4").json()
    return render_template("blog.html", posts=response)


@app.route('/guess/<name>')
def guess(name):
    try:
        gender = requests.get(f"https://api.genderize.io?name={name}").json()
        age = requests.get(f"https://api.agify.io?name={name}").json()
    except UndefinedError:
        print("Missing")
    else:
        return render_template("index.html", name=name, age=age, gender=gender)


if __name__ == "__main__":
    app.run(debug=True)
