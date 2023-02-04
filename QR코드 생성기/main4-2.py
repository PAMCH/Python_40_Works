import qrcode

file_path = r'QR코드 생성기\qr코드모음.txt'

with open(file_path, 'rt', encoding='UTF-8') as f :
    read_lines = f.readlines()

    for line in read_lines :
        line = line.strip()
        print(line)