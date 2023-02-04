import qrcode # QR코드 생성을 위한 라이브러리

qr_data = 'www.naver.com' # QR코드에 연결될 주소
qr_img = qrcode.make(qr_data) # QR코드 이미지 생성 후 할당

save_path = 'QR코드 생성기\\' + qr_data + '.png' # 이미지 파일 생성
qr_img.save(save_path)