import os
import random
from telebot import types
import telebot
import pymongo
from flask import Flask, request
from pymongo import MongoClient

TOKEN = '5516529658:AAESAyHmYnapWVJdxxaSyMYYkx9a56hjbeI'
CONNECTION_STRING = "mongodb+srv://hikki_bd:Ares_0377@cluster0.yv7ke.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
client = MongoClient(CONNECTION_STRING)
db = client['db_for_roz'] # first_DB - название базы данных
collection = db['userDB'] # создаём коллекцию
bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)


bot.send_message(1895572923, 'работаю')

def getIds(message):
  return message.chat.id, message.from_user.id

@bot.message_handler(content_types=['text'])
def commands(message):
    chat, from_user = getIds(message)
    if message.text == '/start':
        bot.send_message(chat, 'Введи /commands и /rand_num')
    elif message.text == '/commands':
        bot.send_message(from_user, '/ready /stat')
    elif message.text == '/ready':
        user = {'id' : from_user}
        if collection.find_one(user) is None:
            bot.send_message(chat, 'Отлично, ты учавствуешь!')
            collection.insert_one(user)
        else:
            bot.send_message(chat, 'Ты уже участник')
            print(list(collection.find()))
    elif message.text == '/stat':
      all = list(collection.find())
      bot.send_message(chat, 100/len(all))
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
    bot.set_webhook(url='https://Rozbot.hikkicode.repl.co/' + TOKEN)
    return "!", 200
if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))