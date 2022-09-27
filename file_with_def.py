import random

def statistic_about_user(from_user, bot, chat, all):
    if from_user == 1895572923 or from_user == 1046080555 or from_user == 1028594384:
        bot.send_message(chat, 'Кол-во участников: ' + str(len(all)))
    else: 
        bot.send_message(chat, 'Ты не явлешься админом')

def in_competition(bot, from_user, chat, collection):
    user = {'id' : from_user}
    if collection.find_one(user) is None:
        bot.send_message(chat, 'Отлично, ты учавствуешь!')
        collection.insert_one(user)
    else:
        bot.send_message(chat, 'Ты уже участник')

def every_user_chance(from_user, all, chat, bot):
    if from_user == 1895572923 or from_user ==1046080555 or from_user == 1028594384:
        chance = 100/int(len(all))
        bot.send_message(chat, 'Шансы каждого участника = ' + str(chance) + '%')
    else: 
        bot.send_message(chat, 'Ты не явлешься админом')

def comp(from_user, bot, all, input_message, chat, winners):
    def end_competition(message):
        if from_user == 1895572923 or from_user == 1046080555 or from_user == 1028594384:
            bot.send_message(chat, 'Ты уверен?')
            bot.register_next_step_handler(message, get_first_access)

    def get_first_access(message):
        if message.text == 'Да' or message.text == 'да':
            bot.send_message(chat, 'Точно?')
            bot.register_next_step_handler(message, get_second_access)
            
    def get_second_access(message):
        if message.text == 'Более чем' or message.text == 'более чем':
            winners = random.sample(all, 3)
            for winner in winners:
                bot.send_message(winner["id"], 'Поздравляю, ты победил! Напиши @TheOutsider228 для получания награды')
    end_competition(input_message)
    
def get_all_commands(bot, from_user):
    bot.send_message(from_user, 'Команды: \n /ready - для участия в розыгрыше \n /stat - кол-во участников \n /chance - шанс каждого из участников \n /end_roz - для окончания розыгрыша')
