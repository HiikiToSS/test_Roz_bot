import os
import random
from flask import Flask, request
from telebot import types
import telebot
import pymongo
from pymongo import MongoClient

TOKEN = '5575632184:AAF4Wg5tNyb1eivb3WvTKZSZm6-XMKgs16c'
CONNECTION_STRING = "mongodb+srv://hikki_bd:Ares_0377@cluster0.yv7ke.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
client = MongoClient(CONNECTION_STRING)

db = client['db_for_roz'] # first_DB - название базы данных
collection = db['userDB'] # создаём коллекцию

bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)

bot.send_message(1895572923, 'работаю')

def commands(message):
  message.chat.type == "channel"
  if message.text == '/start':
    bot.send_message(message.chat.id, 'Введи /commands и /rand_num')
    print(1)
  elif message.text == '/commands':
    bot.send_message(message.from_user.id, '/ready /stat')
  elif message.text == '/ready':
    user = {
      id : message.from_user.id
    }
    collection.insert_one(user)
    bot.send_message(message.chat.id, 'отправил в бд, чекай')
  else:
    bot.send_message(message.from_user.id, text = "Я ещё не нейронка чтобы отвечать на любые вопросы, введи /commands чтобы увидеть список команд")

  
@server.route('/' + TOKEN, methods=['POST'])
def getMessage():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200
@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://rozbot01.herokuapp.com/' + TOKEN)
    return "!", 200
if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))