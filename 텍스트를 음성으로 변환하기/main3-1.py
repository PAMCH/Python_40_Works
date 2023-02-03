from gtts import gTTS # gtts 라이브러리에서 gTTS 함수만 가져옴

text = "안녕하세요. 파이썬과 40개의 작품들 입니다."

tts = gTTS(text=text, lang='ko') # text의 문자열을 한글로 변환하여 할당
tts.save(r"텍스트를 음성으로 변환하기\hi.mp3") # 해당 폴더에 hi.mp3로 저장
#리눅스의 경우 tts.save(r"텍스트를 음성으로 변환하기/hi.mp3")