import telebot
import time
import random

token = "6563887922:AAGSUQvRlodCLtOumSGHFoxWNAukFPDkatA"
bot = telebot.TeleBot(token)

hello = ["Hi", "Hello", "Привет", "Have a good day",]

@bot.message_handler(commands=["start"])
def start(message):
    "Обработка команды start"
    bot.send_message(message.from_user.id, random.choice(hello))

@bot.message_handler(content_types=["text"])
def read_text(message):
    "Функция присылает ответ на неизвестные команды"
    bot.send_message(message.from_user.id, "Я тебя не понимаю, введи /start")


bot.polling()