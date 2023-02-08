import threading # 멀티쓰레드 프로그래밍을 위한 모듈
import time

def thread_1() :
    while True :
        print("쓰레드 1 동작")
        time.sleep(1.0) # 1초마다 쓰레드 1 동작 출력

t1 = threading.Thread(target=thread_1) # 쓰레드 설정
t1.start() # 쓰레드 시작

while True :
    print("메인동작") # 메인코드
    time.sleep(2.0) # 2초마다 실행