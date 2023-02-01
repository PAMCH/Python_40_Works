import random

random_number = random.randint(1,100) # 임의의 정수를 생성

#print(random_number)

game_count = 1 # 숫자 맞추기 시도 횟수 초기화

while True :
    try :
        my_number = int(input("1~100 사이 숫자를 입력하세요! : ")) # 숫자 맞추기 시도

        if my_number > random_number : # 입력된 값이 임의의 정수보다 작을 경우
            print("다운")
        elif my_number < random_number : # 입력된 값이 임의의 정수보다 클 경우
            print("업")
        elif my_number == random_number : # 입력된 값이 임의의 정수와 같을 경우
            print(f"축하합니다! {game_count}회 만에 맞췄습니다.")
            break

        game_count = game_count + 1 # 숫자 맞추기 시도를 실패할 때 마다 증가

    except :
        print("에러가 발생하였습니다. 숫자를 입력하시기 바랍니다.") # 문자열 입력시 예외 처리
