from gtts import gTTS
from playsound import playsound # mp3파일 재생을 위한 모듈
import os # 경로 이동을 위한 모듈

os.chdir(os.path.dirname(os.path.abspath(__file__))) # 경로를 이동하기 위함

text = "안녕하세요. 파이썬과 40개의 작품들 입니다."

tts = gTTS(text=text, lang='ko')
tts.save("hi.mp3")

playsound("hi.mp3") # mp3 파일 재생