import socket # 접속 정보와 관련된 정보를 가져오는 모듈

in_addr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
in_addr.connect(("www.google.co.kr", 443)) # url에 접속하여 정보 확인, https 포트 사용

print(in_addr.getsockname()[0])