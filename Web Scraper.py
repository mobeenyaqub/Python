import bs4
import requests
import lxml

result = requests.get(input("Enter a URL : "))

soup = bs4.BeautifulSoup(result.text,'lxml')

links = []

for i in soup.select('a'):
    links.append(i)

count = 1

for i in links:
    print(f'{count} - {i}\n')
    count += 1

images = []

soup = soup.select('img')

for i in soup:
    images.append(i)

count = 1

for i in images:
    print(f'{count} - {i}\n')
    count += 1

len(images)