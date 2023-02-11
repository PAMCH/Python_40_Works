import pyautogui
import pyperclip
import time
import threading
import os

os.chdir(os.path.dirname(os.path.abspath(__file__))) # 현재 디렉토리로 경로 이동

def send_message() :
    threading.Timer(10, send_message).start() # 재귀적으로 10초마다 실행

    picPos = pyautogui.locateOnScreen('pic1.png') # 미리 준비한 카카오톡 사진 할당
    print(picPos) # 사진과 같은 것을 찾아 좌표 출력

    if picPos is None :
        picPos = pyautogui.locateOnScreen('pic2.png') # 첫번째 사진을 찾지 못하면 두번째 할당
        print(picPos)

    if picPos is None :
        picPos = pyautogui.locateOnScreen('pic3.png') # 두번째 사진을 찾지 못하면 세번째 할당
        print(picPos)

    clickPos = pyautogui.center(picPos) # 중간 좌표 할당
    pyautogui.doubleClick(clickPos) # 바탕화면 속에서 사진과 같은 부분을 두번 클릭

    pyperclip.copy("이 메세지는 자동으로 보내지는 메세지 입니다.")
    pyautogui.hotkey("ctrl","v")
    time.sleep(1.0)

    pyautogui.write(["enter"])
    time.sleep(1.0)

    pyautogui.write(["escape"]) # 메세지 입력 후 esc
    time.sleep(1.0)

send_message()