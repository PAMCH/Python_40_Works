from gtts import gTTS
from playsound import playsound # mp3파일 재생을 위한 모듈
import os # 경로 이동을 위한 모듈

os.chdir(os.path.dirname(os.path.abspath(__file__))) # 경로를 이동하기 위함

file_path = '나의 텍스트.txt' # 예제 파일을 할당
with open(file_path, 'rt', encoding='UTF-8') as f : # f 로 파일을 오픈함
    read_file = f.read() # 파일 내용 전체를 읽어서 할당

tts = gTTS(text=read_file, lang='ko')

tts.save("myText.mp3")

playsound("myText.mp3")