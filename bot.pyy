import requests 

import telebot 

import threading 

import os

TOKEN = os.environ['TELEGRAM_BOT_TOKEN']

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start']) 

def start(message):

    bot.send_message(message.chat.id, "Привет, введи команду /help, чтобы узнать по подробнее") 

@bot.message_handler(commands=['help'])

def help(message):

    bot.send_message(message.chat.id, "Помощь:\n/check <Ваша ссылка>")

@bot.message_handler(commands=['check'])



def check(message):

    url = message.text[7:len(message.text)]

    user = message.chat.id
    while True:
        try:
            while True:
                url = requests.get(url)

                bot.send_message(user, "Сайт работает!")

        except:

        bot.send_message(user, "Сайт не работает!")



bot.polling()
