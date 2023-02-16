from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/post/<blog_id>')
def get_blog(blog_id):
    response = requests.get("https://api.npoint.io/4c7de63525b1e6b2c0a4").json()
    return render_template("post.html", data=response, id=int(blog_id))


@app.route('/')
def home():
    response = requests.get("https://api.npoint.io/4c7de63525b1e6b2c0a4").json()
    return render_template("index.html", data=response)


if __name__ == "__main__":
    app.run(debug=True)
