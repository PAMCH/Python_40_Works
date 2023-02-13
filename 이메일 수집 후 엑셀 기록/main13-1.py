import re # 정규표현식 사용을 위한 모듈
# 많은 문자열을 할당하기 위해 """을 사용함 '''도 가능
test_string = """
aaa@bbb.com
123@abc.co.kr
test@hello.kr
ok@ok.co.kr
ok@ok.co.kr
ok@ok.co.kr
no.co.kr
no.kr
"""

res = re.findall(r'[\w\.-]+@[\w\.-]+', test_string) # 문자열을 정규표현식에 맞는 형식을 찾아와 할당

print(res)