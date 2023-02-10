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

start_x = 992 # 캡처를 하기 위한 시작 x좌표
start_y = 220 # 캡처를 하기 위한 시작 y좌표
end_x = 1656 # 대각선 끝 x좌표
end_y = 635 # 대각선 끝 y좌표

pyautogui.screenshot(r'서울날씨.png', regin(start_x, start_y, end_x-start_x, end_y-start_y))