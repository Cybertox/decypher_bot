import Decypher
import telebot
import datetime
import pytz
import re
#import config
import os

#from config import TOKEN, TIMEZONE, TIMEZONE_COMMON_NAME
from telegram.ext import Updater



P_TIMEZONE = pytz.timezone(TIMEZONE)
TIMEZONE_COMMON_NAME = TIMEZONE_COMMON_NAME

TOKEN = "TOKEN"
PORT = int(os.environ.get('PORT', '8443'))
bot = telebot.TeleBot(TOKEN)

updater = Updater(TOKEN, use_context=True)

@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, "To decypher password send me  command /decypher XXX")

@bot.message_handler(content_types=['text'])
def decypher_code(message):
    txt = message.text.split(' ', 1)
    msg = Decypher.decypher(txt[1])
   # if re.match(r'/decypher', message):
     #   txt = re.split(r'/decypher', message)
    bot.send_message(message.chat.id, msg)


bot.remove_webhook()
updater.start_webhook(listen="0.0.0.0",
                      port=PORT,
                      url_path=TOKEN)

updater.bot.set_webhook("https://decypher-bot/herokuapp.com/" + TOKEN)
updater.idle()

#bot.polling(none_stop=True)

