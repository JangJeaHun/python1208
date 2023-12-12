import requests
import json
import os

client_id = "zrUBwL7RvLwF_vBtZsM5"
client_secret = "LZLyj2CA1G"

keyword = '뉴진스'

start = 1 # 검색시작 위치
display = 10 # 한 번에 표시할 검색 결과 개수 (기본 10, 최대값 100)
end = 15  #전체 사진의 수
n = 1

for i in range(start, end, display):
    url = f"https://openapi.naver.com/v1/search/image?query={keyword}&display={display}&start={i}"
    Headers = {"X-Naver-Client-Id": client_id,
               "X-Naver-Client-Secret": client_secret}
    request =  requests.get(url, headers=Headers)
    python_obj = json.loads(request.text)
    items = python_obj['items']

    for j in range(len(items)):
        img_url = items[j]['link']
        img_file = requests.get(img_url)
        file_path = f'{n}.{keyword}.jpg'

        with open(file_path, 'wb') as f:
            f.write(img_file.content)
            print(f'{n}번째 사진 다운로드..')
            n +=1