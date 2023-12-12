import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import time


Headers = {'User-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'}
url = 'https://www.riss.kr/search/Search.do?isDetailSearch=N&searchGubun=true&viewYn=OP&queryText=&strQuery=%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5&exQuery=&exQueryText=&order=%2FDESC&onHanja=false&strSort=RANK&p_year1=&p_year2=&iStartCount=0&orderBy=&mat_type=&mat_subtype=&fulltext_kind=&t_gubun=&learning_type=&ccl_code=&inside_outside=&fric_yn=&db_type=&image_yn=&gubun=&kdc=&ttsUseYn=&l_sub_code=&fsearchMethod=&sflag=1&isFDetailSearch=N&pageNumber=1&resultKeyword=%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5&fsearchSort=&fsearchOrder=&limiterList=&limiterListText=&facetList=&facetListText=&fsearchDB=&icate=re_a_kor&colName=re_a_kor&pageScale=300&isTab=Y&regnm=&dorg_storage=&language=&language_code=&clickKeyword=&relationKeyword=&query=%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5'

r = requests.get(url)
print(r.status_code)

soup = bs(r.text, 'html.parser')

contents = soup.find_all('div', class_='cont ml60')
print(len(contents))


for content in contents:
    title = content.find('p', class_='title').text
    # print(title)

title =[]
writer = []
publisher =[]
year =[]
journal =[]
link =[]
abstracts=[]

for cont in contents:
    title.append(cont.find('p', class_='title').text)
    writer.append(cont.find('span', class_='writer').text)
    publisher.append(cont.find('p', class_="etc").find_all('span')[1].text)
    year.append(cont.find('p', class_="etc").find_all('span')[2].text)
    journal.append(cont.find('p', class_="etc").find_all('span')[3].text)
    link.append('https://www.riss.kr'+ cont.find('p', class_='title').find('a')['href'])

    if cont.find('p', class_='preAbstract'):
        abstracts.append(cont.find('p', class_='preAbstract').text)
    else :
        abstracts.append('초록이 없습니다.')
        
df = pd.DataFrame(
    {
        '제목' : title,
        '작성자': writer,
        '출판사' : publisher,
        '제작년도': year,
        'journal': journal,
        'link': link,
        'abstracts': abstracts

    }
)

df.to_csv('riss10.csv', index=False)
df.to_excel('riss10.xlsx', index=False)