import os
import random
from telebot import types
import telebot
import pymongo
from pymongo import MongoClient
from flask import Flask, request
#from file_with_def import in_competition,  statistic_about_user, every_user_chance, comp, get_all_commands

server = Flask(__name__)
TOKEN = '5424485104:AAGgOwaEL488DTeH6y3RLwxMEj70ziv6C5U' #AAEoPSXOGulJbu3xA4qwGgrDUPFyxxJ0V0I
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
    all = list(collection.find())
    winners = []
    if message.text == '/hi':
       bot.send_message(chat, 'Введи /commands')
    #if message.text == '/start':
     #   bot.send_message(chat, 'Введи /commands') #сделай нормальное приветствие
   # elif message.text == '/commands':
       # get_all_commands(bot, from_user)
   # elif message.text == '/ready':
       # in_competition(bot, from_user, chat, collection)
    #elif message.text == '/stat':
        #statistic_about_user(from_user, bot, chat, all)
  #  elif message.text == '/chance':
    #    every_user_chance(from_user, all, chat, bot)
    #elif message.text == '/end_roz':
    #    comp(from_user, bot, all, message, chat, winners)
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
    bot.set_webhook(url='https://dashboard.heroku.com/apps/test-roz-bot/' + TOKEN)
    return "!", 200
if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
