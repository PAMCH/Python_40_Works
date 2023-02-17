import telegram # 텔레그렘 봇 사용을 위한 모듈

token = '텔레그램 API token'
bot = telegram.Bot(token=token)
updates = bot.getUpdates()
for u in updates :
    print(u.message) # bot it 확인 가능