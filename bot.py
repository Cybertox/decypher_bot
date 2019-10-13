import Decypher
import telebot
import datetime
import pytz
import re
import config

P_TIMEZONE = pytz.timezone(config.TIMEZONE)
TIMEZONE_COMMON_NAME = config.TIMEZONE_COMMON_NAME

bot = telebot.TeleBot(config.TOKEN)

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



bot.polling(none_stop=True)

