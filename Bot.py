import telebot
import time
import random

token = "6563887922:AAGSUQvRlodCLtOumSGHFoxWNAukFPDkatA"
bot = telebot.TeleBot(token)

welcome_text = """Привет, тебя приветствует бот техподдержки!
Чтоб оставить заявку жми /new_ticket
Чтоб зарегистрировать нового пользователя жми /reg
"""
help_text = """Доступные команды:
/start - Перезапускает бота
/reg - Регистрирует нового пользователя
/new_ticket - Создает новую заявку
"""

@bot.message_handler(commands=["start"])
def start(message):
    "Обработка команды start"
    bot.send_message(message.from_user.id, welcome_text)

@bot.message_handler(commands=["help"])
def start(message):
    "Обработка команды help"
    bot.send_message(message.from_user.id, help_text)

@bot.message_handler(content_types=["text"])
def read_text(message):
    "Функция присылает ответ на неизвестные команды"
    bot.send_message(message.from_user.id, "Я тебя не понимаю, жми /help")

@bot.message_handler(commands=["reg"])
def read_text(message):
    "Функция выполняет регистрацию пользователя"
    bot.send_message(message.from_user.id, "Введите свое имя:")









bot.polling()