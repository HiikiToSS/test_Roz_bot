from flask import Flask, request
import os
import random
from telebot import types
import telebot
import pymongo
from pymongo import MongoClient

server = Flask(__name__)
TOKEN = '5146045260:AAEoPSXOGulJbu3xA4qwGgrDUPFyxxJ0V0I'
CONNECTION_STRING = "mongodb+srv://hikki_bd:Ares_0377@cluster0.yv7ke.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
client = MongoClient(CONNECTION_STRING)
db = client['db_for_roz'] # first_DB - название базы данных
collection = db['userDB'] # создаём коллекцию
bot = telebot.TeleBot(TOKEN)

bot.send_message(1895572923, 'работаю')

def getIds(message):
  return message.chat.id, message.from_user.id

@bot.message_handler(content_types=['text'])
def commands(message):
    chat, from_user = getIds(message)
    if message.text == '/start':
        bot.send_message(chat, 'Введи /commands и /rand_num')
    elif message.text == '/commands':
        bot.send_message(from_user, 'Команды: \n /ready - для участия в розыгрыше \n /stat - кол-во участников')
    elif message.text == '/ready':
        user = {'id' : from_user}
        if collection.find_one(user) is None:
            bot.send_message(chat, 'Отлично, ты учавствуешь!')
            collection.insert_one(user)
        else:
            bot.send_message(chat, 'Ты уже участник')
    elif message.text == '/stat':
      all = list(collection.find())
      bot.send_message(chat, 'Кол-во участников: ' + str(len(all)))
    else:
        bot.send_message(from_user, text = "Я ещё не нейронка чтобы отвечать на любые вопросы, введи /commands чтобы увидеть список команд")


@server.route('/' + TOKEN, methods=['POST'])
def getMessage():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200
@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://test-sth01.heroku.com/' + TOKEN)
    return "!", 200
if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
