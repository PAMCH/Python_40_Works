from os import linesep
import googletrans

translator = googletrans.Translator()

read_file_path = r"영어파일.txt" # 예제 파일 가져옴
write_file_path = r"한글파일.txt" # 번역한 파일 생성

with open(read_file_path , 'r') as f : # 예제 파일을 한줄씩 읽어서 할당함
    readLines = f.readline()

for lines in readLines : # 한줄 식 읽어와서 한글로 번역하고 출력하여 저장
    res = translator.translate(lines, dest='ko')
    print(res.text)
    with open(write_file_path, 'a', encoding='UTF8') as f : # a는 추가 쓰기 옵션이며 한글 사용을 위해 UTF8으로 인코딩
        f.write(res.text + '\n')