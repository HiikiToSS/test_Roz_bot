import random

def statistic_about_user(from_user, bot, chat, all):
    if from_user == 1895572923 or from_user == 1046080555 or from_user == 1028594384:
        bot.send_message(chat, 'Кол-во участников: ' + str(len(all)))
    else: 
        bot.send_message(chat, 'Ты не явлешься админом')

def in_competition(bot, from_user, chat, collection):
    user = {'id' : from_user}
    bot.send_message(1895572923, '+1')
    if collection.find_one(user) is None:
        bot.send_message(chat, 'Отлично, ты учавствуешь!\nЖди объявления результатов в @r34world')
        collection.insert_one(user)
    else:
        bot.send_message(chat, 'Ты уже участник')

def every_user_chance(from_user, all, chat, bot):
    if from_user == 1895572923 or from_user == 1046080555 or from_user == 1028594384:
        chance = 100/int(len(all))
        bot.send_message(chat, 'Шансы каждого участника = ' + str(round(chance, 1)) + '%')
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
            winners = random.sample(all, 2)
            for winner in winners:
                bot.send_message(winner["id"], 'Поздравляю, ты победил! Напиши @TheOutsider228 для получания награды \n' + str(winner["id"]))
    end_competition(input_message)

    
def get_all_commands(bot, from_user):
    if from_user == 1895572923 or from_user == 1046080555 or from_user == 1028594384:
        bot.send_message(from_user, 'Команды: \n /ready - для участия в розыгрыше \n /members - кол-во участников \n /chance - шанс каждого из участников \n /end_roz - окончание розыгрыша')
    else:
        bot.send_message(from_user, 'Команды: \n /ready - для участия в розыгрыше')
