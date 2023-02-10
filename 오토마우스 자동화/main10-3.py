import pyautogui # 마우스, 키보드 자동 제어를 위한 모듈
import pyperclip # 클립보드에 값을 복사 및 붙여넣기 위한 모듈
import time

while(True) :
    print(pyautogui.position()) # 이후 캡처를 위한 마우스 좌표 확인
    time.sleep(0.1)