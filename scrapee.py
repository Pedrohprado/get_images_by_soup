import requests
from bs4 import BeautifulSoup

url = "https://www.google.com/search?rlz=1C1CHZN_pt-BRBR1056BR1056&q=senta+a+pua&tbm=isch&sa=X&ved=2ahUKEwi3i_XhktL_AhWQrZUCHbBgA5sQ0pQJegQIDBAB&biw=620&bih=649&dpr=1"
headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}

r = requests.get(url=url, headers=headers)

soup = BeautifulSoup(r.content, 'html.parser')
result = soup.find('div', class_ = 'mJxzWe')
rows = result.find_all('img', class_ = 'rg_i Q4LuWd')

for row in rows:
    print(row)

# for i in result:
#     src = i.img['src']
#     print(src)
