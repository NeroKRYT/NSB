import telebot
from telebot import types
token = ""
bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("Хочу", "/help")
    bot.send_message(message.chat.id, 'Привет! Хочешь узнать свежую информацию о МТУСИ?', reply_markup=keyboard)
@bot.message_handler(commands=['help'])
def message2(message):
    bot.send_message(message.chat.id, 'Я умею отвечать на команды: /News, /Weather, /Cars, а также отвечать на сообщения: Привет,Пока,Что посмотреть?, Хочу.')


@bot.message_handler(commands=['News'])
def message(message):
    bot.send_message(message.chat.id, 'Вот вам новости: https://ria.ru/ 📰')


@bot.message_handler(commands=['Weather'])
def message1(message):
    bot.send_message(message.chat.id, 'Вот вам погода: https://yandex.ru/pogoda/moscow?lat=55.753215&lon=37.622504 ⛅')

@bot.message_handler(commands=['Cars'])
def start_message(message):
    bot.send_message(message.chat.id, 'Держите: https://bipbap.ru/krasivye-kartinki/kartinki-krasivyh-mashin-35-foto.html 🚙')


@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == "хочу":
        bot.send_message(message.chat.id, 'Тогда тебе сюда – https://mtuci.ru/')
    elif message.text.lower() == "привет":
        bot.send_message(message.chat.id, 'Привет👹')
    elif message.text.lower() == "пока":
        bot.send_message(message.chat.id, 'Покеда🤠')
    elif message.text.lower() == "что посмотреть?":
        bot.send_message(message.chat.id, 'Посмотрите фильм😉')
bot.infinity_polling()
