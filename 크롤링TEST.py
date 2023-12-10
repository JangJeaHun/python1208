import requests
from bs4 import BeautifulSoup
import pandas as pd

resp = requests.get('https://finance.naver.com/')
html = resp.text
soup = BeautifulSoup(html,'html.parser')
news = soup.select('.tbl_home a')

title = []
number_1 = []
number_2 = []
number_3 = []
url = []

for n in news:
    title.append(n.text)
    url.append(n['href'])
    number_1.append(.tbl_home tbody td)

df = pd.DataFrame() 
df['제목'] = title
df['숫자1'] = number_1

df['URL'] = url

print(df)
