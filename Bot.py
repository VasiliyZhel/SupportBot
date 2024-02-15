import telebot
import time
import random

token = "6563887922:AAGSUQvRlodCLtOumSGHFoxWNAukFPDkatA"
bot = telebot.TeleBot(token)
# for reg
client_name = ""
organization = ""
role = ""
phone = ""
# fot ticket
topic = ""
full_topic = ""
prioritet = ""

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
    bot.register_next_step_handler(message, send_admin_reg)

def send_admin_reg(message):
    "Функция отправляет уведомляет пользователя о регистрации пользователя и отправляет данные админу"
    global phone
    global user_info_admin
    global user_info
    phone = message.text
    bot.send_message(message.from_user.id, "Регистрация завершена, теперь вы можете создавать заявки. Чтоб создать заявку жми /new_ticket ;")
    bot.send_message(1362233196, f"{client_name}, {organization}, {role}, {phone}")
    bot.send_message(1362233196, message.from_user)


@bot.message_handler(commands=["new_ticket"]) # Декоратор для создания заявок
def get_ticket(message):
    "Функция запрашивает описание заявки"
    bot.send_message(message.from_user.id, "Введите название заявки")
    bot.register_next_step_handler(message, get_full_ticket)

def get_full_ticket(message):
    "Функция запривает полдное описание заявки"
    global topic
    topic = message.text
    bot.send_message(message.from_user.id, "Опишите проблему")
    bot.register_next_step_handler(message, get_status)

def get_status(message):
    "Функция запрашивает приоритет"
    global full_topic
    full_topic = message.text
    bot.send_message(message.from_user.id, "Введите приоритет заявки")
    bot.register_next_step_handler(message, send_admin_ticket)

def send_admin_ticket(message):
    global prioritet
    prioritet = message.text
    bot.send_message(message.from_user.id, "Заявка создана, свяжемся с вами в ближайшее время")
    bot.send_message(1362233196, f"{client_name}, {organization}, {role}, {phone}")
    bot.send_message(1362233196, f"{topic}, {full_topic}, {prioritet}")













@bot.message_handler(content_types=["text"])
def read_text(message):
    "Функция присылает ответ на неизвестные команды"
    bot.send_message(message.from_user.id, "Я тебя не понимаю, жми /help")

bot.polling()