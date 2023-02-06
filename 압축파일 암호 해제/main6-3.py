import itertools
import zipfile

def un_zip(passwd_string, min_len, max_len, zFile) :
    for len in range(min_len, max_len):
        to_attepmt = itertools.product(passwd_string, repeat = len)
        for attempt in to_attepmt :
            passwd = ''.join(attempt)
            print(passwd)
            try :
                zFile.extractall(pwd = passwd.encode())
                print(f'비밀번호는 {passwd} 입니다.')
                return 1 # 함수로 변환하고 break 대신 return을 넣어주서 종료
            except :
                pass

passwd_string = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

zFile = zipfile.ZipFile(r'암호1234.zip')

min_len = 1
max_len = 5

unzip_result = un_zip(passwd_string, min_len, max_len, zFile)

if unzip_result == 1 :
    print("암호 찾기에 성공하였습니다.")
else :
    print("암호 찾기에 실패하였습니다.")