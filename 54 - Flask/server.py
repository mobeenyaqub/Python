from flask import Flask
import random

app = Flask(__name__)
random_number = str(random.randint(0, 9))


@app.route('/')
def home():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='https://media0.giphy.com/media/vVegyymxA90fkY8jkE/200w.webp?cid" \
           "=ecf05e47w7rxncmzl81zh34t2etlgklnqiyvapd4ru3yh6x2&rid=200w.webp&ct=g'>"


@app.route('/<number>')
def guess(number):
    if number == random_number:
        return "<h1>Bingo!!!!</h1>" + "<img src='https://media1.giphy.com/media/2SYc7mttUnWWaqvWz8/200.webp?cid" \
                                      "=ecf05e47ahrar5795e5cdrzodrxwd8mdvo0g5l08oebknypo&rid=200.webp&ct=g'>"
    else:
        message = "<img src='https://media0.giphy.com/media/3OhXBaoR1tVPW/200w.webp?cid" \
                  "=ecf05e47yje92tqo0frz8dmnxjmrsrgf3jpjizj66i8snib1&rid=200w.webp&ct=g'> "
        if number > random_number:
            return f"<h1>{number} is too high</h1>" + message
        else:
            return f"<h1>{number} is too low</h1>" + message


if __name__ == "__main__":
    app.run(debug=True)
