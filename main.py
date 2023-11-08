import telebot
from telebot import types
import sqlite3



bot = telebot.TeleBot("6511052905:AAGbp7Kk95gtOjnpqZN7qKPKk3NFDLcp3Fk", parse_mode='MARKDOWN')

@bot.message_handler(commands=['start'])
def handle_start(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Создать новую привычку', callback_data='new_habit')
    btn2 = types.InlineKeyboardButton('Просмотреть существующие', callback_data='show_existing')
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, "Hi, this bot allows to implement *Two Day Rule*. What do you want to do?",
                     reply_markup=markup)
    bot.send_message(message.chat.id, message)

@bot.callback_query_handler(func=lambda callback: True)
def callback_handler(callback):
    # here we write and read appropriate info from the database
    if callback.data == 'new_habit':
        bot.send_message(callback.message.chat.id, "Type the name of your habit")
    if callback.data == 'show_existing':
        pass

# scheduling messages for specific times
# https://stackoverflow.com/questions/48288124/how-to-send-message-in-specific-time-telegrambot

bot.infinity_polling()

