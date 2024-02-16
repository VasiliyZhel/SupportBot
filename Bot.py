import telebot
import time
import random
# for bot
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
# for users
list = {}
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
    """
    Обработка команды start
    Если пользователь есть в списке, приветствует по имени
    """
    global list
    if message.from_user.id in list:
        name_for_start = ""
        for i in list[message.from_user.id]:
            if i != ",":
                name_for_start += i
            else:
                break
        bot.send_message(message.from_user.id, f"""Привет {name_for_start}!
Чтоб оставить заявку жми /new_ticket
""")
    else:
        bot.send_message(message.from_user.id, welcome_text)


@bot.message_handler(commands=["help"])
def start(message):
    "Обработка команды help"
    bot.send_message(message.from_user.id, help_text)


@bot.message_handler(commands=["reg"]) # Декоратор для регистрации пользователя
def get_name(message):
    "Функция запрашивает имя, если айди пользователя есть в списке, то выходит уведомляет об этом"
    global list
    if message.from_user.id in list:
        bot.send_message(message.from_user.id, "Вы уже зарегистрированны")
    else:
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
    "Функция отправляет уведомляет пользователя о регистрации пользователя и отправляет данные админу, выводит в лог, так же добавляет пользователя в файл"
    global phone
    phone = message.text
    bot.send_message(message.from_user.id, "Регистрация завершена, теперь вы можете создавать заявки. Чтоб создать заявку жми /new_ticket ;")
    # Создали переменную айди и переменную с информацией о пользователе, добавили в словарь
    a = message.from_user.id
    b = f"{client_name}, {organization}, {role}, {phone}"
    global list
    list[a] = b
    user_table = open('Users.txt', 'w', encoding="utf8")
    for key, value in list.items():
        user_table.write(f'{key}, {value}\n')
    user_table.close()
    bot.send_message(1362233196, list.get(message.from_user.id))
    bot.send_message(1362233196, message.from_user)
    print(list)


@bot.message_handler(commands=["new_ticket"]) # Декоратор для создания заявок
def get_ticket(message):
    "Функция запрашивает описание заявки и отправляет на регистрацию, если пользователя нет в базе"
    global list
    if message.from_user.id not in list:
        bot.send_message(message.from_user.id, "Чтоб создавать заявки требуется пройти регистрацию, жми /reg")
    else:
        bot.send_message(message.from_user.id, "Введите название заявки")
        bot.register_next_step_handler(message, get_full_ticket)

def get_full_ticket(message):
    "Функция запрашивает полное описание заявки"
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