import telebot
from telebot import types

import botconfig

bot = telebot.TeleBot(botconfig.TOKEN)

def open_file(path):                  # open file structure for open file like botconfig.py
    str = ''
    file = open(path, "r")

    for line in file:
        str += line
    
    return str


@bot.message_handler(commands=['start' , 'ping' , 'p'])
def send_message(message):
    bot.reply_to(message, open_file("ping.txt"))

bot.polling()

