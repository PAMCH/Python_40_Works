import requests # url 접속을 위한 모듈
import re #IP 주소를 찾기 위해 정규식 표현 모듈 사용

req = requests.get("http://ipconfig.kr") # http://ipconfig.kr 접속

out_addr = re.search(r'IP Address : (\d{1,3}\.\d{1,3}.\d{1,3}.\d{1,3})', req.text)[1] # 정규식 표현을 사용하여 IP주소 할당
print(out_addr) # 외부 IP 출력