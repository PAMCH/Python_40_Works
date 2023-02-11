import pyautogui
import os

os.chdir(os.path.dirname(os.path.abspath(__file__))) # 현재 디렉토리로 경로 이동

picPos = pyautogui.locateOnScreen('pic1.png') # 미리 준비한 카카오톡 사진 할당
print(picPos) # 사진과 같은 것을 찾아 좌표 출력

if picPos is None :
    picPos = pyautogui.locateOnScreen('pic2.png') # 첫번째 사진을 찾지 못하면 두번째 할당
    print(picPos)

if picPos is None :
    picPos = pyautogui.locateOnScreen('pic3.png') # 두번째 사진을 찾지 못하면 세번째 할당
    print(picPos)