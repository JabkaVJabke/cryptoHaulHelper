import telebot
from telebot import types
import parsers
import driver_creation

drivers = driver_creation.create_drivers(1)
whitebit_parser = parsers.WhitebitParser(drivers[0])
bot = telebot.TeleBot("5434784333:AAFMh6K5WBVp_b6Pm8MvjfKV8qCiI2JjZTg")

print("started")


@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Да")
    markup.add(btn1)
    bot.send_message(message.chat.id,
                     text=f"Нажми".format(
                         message.from_user), reply_markup=markup)


@bot.message_handler(content_types=["text"])
def func(message):
    if (message.text == "Да"):
        bot.send_message(message.chat.id, text=whitebit_parser.get_exchange_rate_on_whitebit("USDT", "UAH"))


bot.polling(none_stop=True)
