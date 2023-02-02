import requests # url 접속을 위한 모듈
import re #IP 주소를 찾기 위해 정규식 표현 모듈 사용
import socket # 접속 정보와 관련된 정보를 가져오는 모듈

in_addr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
in_addr.connect(("www.google.co.kr", 443)) # url에 접속하여 정보 확인, https 포트 사용
print("내부 IP : ", in_addr.getsockname()[0])

req = requests.get("http://ipconfig.kr") # http://ipconfig.kr 접속

out_addr = re.search(r'IP Address : (\d{1,3}\.\d{1,3}.\d{1,3}.\d{1,3})', req.text)[1] # 정규식 표현을 사용하여 IP주소 할당
print("외부 IP : ", out_addr) # 외부 IP 출력