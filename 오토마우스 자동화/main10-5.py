import pyautogui # 마우스, 키보드 자동 제어를 위한 모듈
import pyperclip # 클립보드에 값을 복사 및 붙여넣기 위한 모듈
import time

weather = ['서울 날씨', '시흥 날씨', '청주 날씨', '부산 날씨']

addr_x = 1145 # 검색창 임의 x좌표
addr_y = 53 # 검색창 임의 y좌표
start_x = 992
start_y = 220
end_x = 1656
end_y = 635

for local_weather in weather :
    pyautogui.moveTO(addr_x, addr_y)
    time.sleep(0.2)
    pyautogui.click()
    time.sleep(0.2)
    pyautogui.write("www.naver.com", interval=0.1)
    pyautogui.write(["enter"])
    time.sleep(1)

    pyperclip.copy(local_weather)
    pyautogui.hotkey("ctrl", "v")
    time.sleep(0.5)
    pyautogui.write(["enter"])
    time.sleep(1)
    save_path = '\\' + local_weather + '.png' 
    pyautogui.screenshot(save_path, region=(start_x, start_y, end_x-start_x, end_y-start_y))