import socket # 접속 정보와 관련된 정보를 가져오는 모듈

in_addr = socket.gethostbyname(socket.gethostname()) # 연결된 소켓의 이름을 할당

print(in_addr) # 내부 IP 출력