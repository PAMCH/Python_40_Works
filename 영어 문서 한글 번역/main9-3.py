from os import linesep
import googletrans

translator = googletrans.Translator()

read_file_path = r"영어파일.txt" # 예제 파일 가져옴

with open(read_file_path , 'r') as f : # 예제 파일을 한줄씩 읽어서 할당함
    readLines = f.readline()

for lines in readLines : # 한줄 식 읽어와서 한글로 번역하고 출력
    res = translator.translate(lines, dest='ko')
    print(res.text)