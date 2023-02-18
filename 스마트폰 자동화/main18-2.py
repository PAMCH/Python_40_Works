from ppadb.client import Client # pure-python-adb 모듈을 통해 스마트폰을 제어할 수 있음
import time

def adb_connect() :
    client = Client(host="127.0.0.1",post=5037) # 루프백 주소와 포트 사용
    find_devices=client.devices()

    if len(find_devices) == 0:
        print("No devices")
        quit() # 디바이스를 찾지 못하면 종료

    device = find_devices[0]
    print(f'찾은 디바이스: {device}')

    return device,client

device, client = adb_connect()

device.shell('input keyevent 64') #명령어로 웹 브라우저 실행, 크롬이 실행됨.
time.sleep(3.0)