from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"

    return wrapper


def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"

    return wrapper


def make_underlined(function):
    def wrapper():
        return "<u>" + function() + "</u>"

    return wrapper


@app.route('/bye')
@make_bold
@make_emphasis
@make_underlined
def bye():
    return "Bye!"


@app.route('/')
def hello_world():
    return '<h1 style="color:red; text-align:center">Hello, World!</h1>' \
           '<p>This is a test paragraph</p>' \
           '<div style="width:480px"><iframe allow="fullscreen" frameBorder="0" height="270" ' \
           'src="https://giphy.com/embed/IsDjNQPc4weWPEwhWm/video" width="480"></iframe></div>'


@app.route("/<name>/<age>")
def greet(name, age):
    return f'Hello {name} age {age}.'


if __name__ == "__main__":
    app.run(debug=True)
