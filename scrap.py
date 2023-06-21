import requests
from bs4 import BeautifulSoup
import urllib.request

url = "https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States"
headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}

r = requests.get(url=url, headers=headers)

soup = BeautifulSoup(r.content, 'html.parser')
caption = soup.find('caption')
table = caption.parent
rows = table.find_all('tr')

for row in rows[2:]:
    src = row.th.span.img['src']
    part = src.split('.svg')[0]
    cleaned = part.replace('thumb/', '')
    stripped = cleaned.strip('//')
    img = 'https://{}.svg'.format(stripped)
    filename = img.split('/')[-1]
    print(filename)
    flag = requests.get(img, headers=headers)
    if flag.status_code != 200:
        print('error {}'.format(filename))
    else:
        with open(filename, 'wb') as f:
            noop = f.write(flag.content)
            print('Save {}'.format(filename))