import telebot
import time
import random

token = "6563887922:AAGSUQvRlodCLtOumSGHFoxWNAukFPDkatA"
bot = telebot.TeleBot(token)
client_name = ""
organization = ""
role = ""
phone = ""
user_info = [client_name, organization, role, phone]
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


@bot.message_handler(commands=["reg"]) # Декоратор для регистрации пользователя
def get_name(message):
    "Функция запрашивает имя"
    bot.send_message(message.from_user.id, "Введите свое имя")
    bot.register_next_step_handler(message, get_organisation)

def get_organisation(message):
    "Функция запрашивает организацию у клиента"
    global client_name
    client_name = message.text
    bot.send_message(message.from_user.id, "От какой огранизации вы обращаетесь?")
    bot.register_next_step_handler(message, get_role)

def get_role(message):
    "Функция запрашивает должность"
    global organization
    organization = message.text
    bot.send_message(message.from_user.id, "Введите свою должность?")
    bot.register_next_step_handler(message, get_phone)

def get_phone(message):
    "Функция запрашивает номер телефона"
    global role
    role = message.text
    bot.send_message(message.from_user.id, "Введите номер телефона для связи")
    bot.register_next_step_handler(message, send_admin)

def send_admin(message):
    "Функция отправляет уведомляет пользователя о регистрации пользователя и отправляет данные админу"
    global phone
    global user_info_admin
    global user_info
    phone = message.text
    bot.send_message(message.from_user.id, "Регистрация завершена, теперь вы можете создавать заявки")
    bot.send_message(1362233196, f"{client_name}, {organization}, {role}, {phone}")
    bot.send_message(1362233196, message.from_user)


@bot.message_handler(content_types=["text"])
def read_text(message):
    "Функция присылает ответ на неизвестные команды"
    bot.send_message(message.from_user.id, "Я тебя не понимаю, жми /help")

bot.polling()