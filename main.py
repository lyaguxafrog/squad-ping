import telebot

import botconfig

bot = telebot.TeleBot(botconfig.TOKEN)

def open_file(path):                  # open file structure for open file like botconfig.py
    str = ''
    file = open(path, "r")

    for line in file:
        str += line
    
    return str


bot.polling()

