import requests # 웹크롤링을 위한 모듈
import re

url = 'https://v.daum.net/v/20230213200007930' # 스크랩을 위한 뉴스기사 url

headers = {
    'User-Agent': 'Mozilla/5.0',
    'Content-Type': 'text/html; charset=utf-8'
}

response = requests.get(url,headers=headers)

res = re.findall(r'[\w\.-]+@[\w\.-]',response.text)

res = list(set(res))

print(res[0])