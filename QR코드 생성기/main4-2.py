import qrcode

file_path = r'QR코드 생성기\qr코드모음.txt' # qr코드모음 텍스트 파일을 할당

with open(file_path, 'rt', encoding='UTF-8') as f : # qr코드모음 텍스트 파일을 읽음
    read_lines = f.readlines() # 텍스트 파일 값을 리스트 값으로 할당

    for line in read_lines :
        line = line.strip() # 문자열 별 개행문자 삭제
        print(line) # 문자열 출력