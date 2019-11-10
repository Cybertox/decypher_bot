import Decypher
import telebot
import os
from flask import Flask, request

from config import TOKEN

bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)

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


@server.route('/' + TOKEN, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200


@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://decypher-bot.herokuapp.com/' + TOKEN)
    return "!", 200


if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
