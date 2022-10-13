import telebot
from telebot import types

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
        bot.send_message(message.chat.id, text=f"Пизда")


bot.polling(none_stop=True)