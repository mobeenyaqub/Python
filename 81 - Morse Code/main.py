from bs4 import BeautifulSoup
import requests

quote = input("Enter a string to convert: ").upper()

response = requests.get(url="https://en.wikipedia.org/wiki/Morse_code").text
soup = BeautifulSoup(response, "html.parser")


find_data = soup.select(".sortable td b")
data = [i.getText() for i in find_data]

clean_data = [i for i in data if len(i) > 2 or i.isdigit()]

for i in range(len(clean_data)):
    if ', ' in clean_data[i]:
        clean_data[i] = clean_data[i].split(', ')[0]
    elif '[' in clean_data[i]:
        clean_data[i] = clean_data[i].split('[')[-1].split(']')[0]
    if '\u200a' in clean_data[i]:
        clean_data[i] = clean_data[i].replace('\u200a', '')
        if ' ' in clean_data[i]:
            clean_data[i] = clean_data[i].replace(' ', '')

morse_code = ""

for i in clean_data:
    for j in quote:
        if j == i:
            morse_code += clean_data[clean_data.index(i)+1]

print(morse_code)
