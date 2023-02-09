import googletrans # 구글 번역기 사용을 위한 모듈

translator = googletrans.Translator()

str1 = "행복하세요."
res1 = translator.translate(str1, dest='en', src='auto') # 영어로 번역
print(f"행복하세요. => {res1.text}")

str2 = "I am happy."
res2 = translator.translate(str2, dest='ko', src='en') # 한글로 번역 / src는 생략해도 됨
print(f"I am happy. => {res2.text}")