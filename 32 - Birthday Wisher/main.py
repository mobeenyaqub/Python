import smtplib
import datetime
import random


def send_email(quote):
    my_email = ""
    password = ""
    connection = smtplib.SMTP("smtp.gmail.com", 587)
    connection.starttls()

    message = "Subject: " + "Quote" + "\n" + quote
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="", msg=message)
    connection.close()
    print("Done")


current_day = datetime.datetime.today().weekday()

if current_day == 0:
    with open("quotes.txt") as quotes:
        quote = random.choice(quotes.readlines())
        send_email(quote)
