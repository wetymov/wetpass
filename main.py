import database.connect as con
import sqlite3
import telebot
from modules.config import Config
from modules.commands import commands_main
from modules.template import Template
# IMPORTS


database = con.DataBaseConnect(sqlite3.connect('database/wetpass.db', check_same_thread=False))
token = Config.get_token()
bot = telebot.TeleBot(token)

#base settings

@bot.message_handler(commands=['start'])
def start_message(message):
    try:
        bot.send_message(message.chat.id, Template("start").get())
        database.create_account(message.chat.id)
    except:
        bot.send_message(message.chat.id, Template("help").get())

@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, Template("help").get())

@bot.message_handler(commands=['about'])
def message_handler_auth_main(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(text= 'GitHub разработчика.', url='https://github.com/wetymov'))
    markup.add(telebot.types.InlineKeyboardButton(text= 'Habr Career разработчика.', url='https://career.habr.com/wetymov'))
    markup.add(telebot.types.InlineKeyboardButton(text= 'Telegram разработчика.', url='https://t.me/wetymov'))
    msg = bot.send_message(message.chat.id,
        '══════╣ Created by WETYMOV ╠══════\n'+
        'Btw by this guy: Denis Vasin\n'+
        'Start creating: 07.08.2024\n'+
        'End creating: __.__.____\n'+
        'Version: 0.0.1\n'+
        'Have a nice day\n'+
        '══════╣ Created by WETYMOV ╠══════\n',
        reply_markup=markup)



commands_main(bot, database)

bot.polling()
