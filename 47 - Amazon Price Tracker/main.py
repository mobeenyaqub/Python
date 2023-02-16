import requests
from bs4 import BeautifulSoup
import smtplib

header = {
"Request Line": "GET / HTTP/1.1",
"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
"Accept-Language":"en-US,en;q=0.9,ur;q=0.8,pt;q=0.7"
}


def price_alert():
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        my_email = ""
        password = ""
        connection.login(my_email, password)
        message = "Subject: Price Drop\nPrice has dropped below $120"
        connection.sendmail(my_email, "", message)


response = requests.get("https://www.amazon.com/Instant-Pot-Ultra-Programmable-Sterilizer/dp"
                        "/B06Y1MP2PY/?_encoding=UTF8&pd_rd_w=4yxLA&content-id=amzn1.sym"
                        ".03bef33a-a357-4fe3-9505-7fd4d6236957&pf_rd_p=03bef33a-a357-4fe3"
                        "-9505-7fd4d6236957&pf_rd_r=QGVRHRNXJEGSQWZ3PGQ2&pd_rd_wg=Ibg1o&pd"
                        "_rd_r=2a923264-cb9a-48b6-8574-02c7739c3b1c&ref_=pd_gw_ci_mcx_mr_hp_d", headers=header).text

soup = BeautifulSoup(response, "lxml")
price = float(soup.select_one("span .a-offscreen").getText().split("$")[1])

if price < 120:
    price_alert()


