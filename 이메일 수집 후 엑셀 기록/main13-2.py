import re

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

res = re.findall(r'[\w\.-]+@[\w\.-]+', test_string)

res = list(set(res)) # set으로 중복 제거 후 list화 시킴

print(res)