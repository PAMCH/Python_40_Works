from currency_converter import CurrencyConverter # 환율 계산을 위한 모듈

cc = CurrencyConverter('http://www.ecb.europa.eu/status/eurofxref/eurofxrez.zip') # 최신 환율 정보 가져오기

print(cc.convert(1, 'USD', 'KRW')) # 1달러를 원화로 변경