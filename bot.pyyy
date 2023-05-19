import os
token = os.environ['TELEGRAM_BOT_TOKEN']
print("Intsalling modules...")
os.system("pip install requests")
os.system("pip install telebot")
os.system("pip install threading")
import requests as r
import telebot
import threading as t
bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,"Привет введи /help,чтобы узнать все команды")
@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, "Список команд:\n/check <ваша ссылка> - чекает, сайт ли работает или нет\n/activehost <ваша ссылка> - делает сайт активным, чтобы сайт спал, если запросы 0 в сек и сайт спит")
@bot.message_handler(commands=['check'])
def checks():
    global link
    def check(message):
        bot.send_message(message.chat.id, "Ссылка чекается...")
        link = message.text[7:len(message.text)]
        url = r.get(link)
        if url.status_code == 200:
            bot.send_message(message.chat.id, f"Ссылка работает! Код {r.status_code}")
        else:
            bot.send_message(message.chat.id, f"Ссылка работает! Код {r.status_code}")
    start = t.Thread(target=check)
start = t.Thread(target=check)
@bot.message_handler(commands=['activehost'])
def active():
   global h
   def activehost(message):
       h = message.text[12:len(message.text)]
       bot.send_message(message.chat.id, "Ссылка в активе!")
       while True:
           try:
               r.get(h)
           except:
               print("Error host")
