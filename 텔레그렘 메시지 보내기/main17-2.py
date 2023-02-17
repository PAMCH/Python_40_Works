import telegram

token = '텔레그램 API token'
id = "bot ID"

bot = telegram.Bot(token)
bot.sendMeaage(chat_id=id, text="파이썬을 보내는 메시지 입니다.")