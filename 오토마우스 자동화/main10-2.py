import pyautogui # 마우스, 키보드 자동 제어를 위한 모듈
import pyperclip # 클립보드에 값을 복사 및 붙여넣기 위한 모듈
import time

pyautogui.moveTo(1241, 206, 0.2) # x=1241, y=206 좌표로 0.2초 동안 이동
pyautogui.click() # 마우스 좌클릭
time.sleep(0.5) # 0.5초 대기

pyperclip.copy("서울 날씨") # 클립보드에 문자열 저장
pyautogui.hotkey("ctrl", "v") # ctrt+v 실행하여 붙여넣기
time.sleep(0.5)

pyautogui.write(["enter"]) # 엔터 입력
time.sleep(1)