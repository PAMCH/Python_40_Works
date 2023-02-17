import telegram
from telegram.ext import Updater
from telegram.ext import MessageHandler, Filters

token = '텔레그램 API token'
id = "bot ID"

bot = telegram.Bot(token)
bot.sendMeaage(chat_id=id, text="자동응답 테스트, 안녕 또는 뭐해 를 입력해주세요.")

updater = Updater(token=token, use_context=True)
dispatcher = updater.dispather
updater.start_polling()

def handler(update, context) :
    user_text = update.message.text
    if user_text == '안녕' :
        bot.send_message(chat_id=id, text="어 그래 안녕") # 안녕 에 대한 응답
    elif user_text == "뭐해" :
        bot.send_message(chat_id=id, text="그냥 있어") # 뭐해 에 대한 응답

echo_handler = MessageHandler(Filters.text, handler)
dispatcher.add_handler(echo_handler)