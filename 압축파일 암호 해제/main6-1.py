import itertools # 반복 데이터를 처리하기 위한 모듈

passwd_string = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

for len in range(1,4):
    to_attepmt = itertools.product(passwd_string, repeat = len) # 문자열을 길이(1~3)로 정렬
    for attempt in to_attepmt : # 정렬된 문자 수 만큼 반복
        passwd = ''.join(attempt) # 리스트 값을 문자열로 변환
        print(passwd) # 값 출력 ex) ZZY, ZZZ 등