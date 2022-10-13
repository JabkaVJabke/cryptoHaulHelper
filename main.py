import telebot
from telebot import types
from selenium import webdriver
import parsers
from logic import Calculate
#Сори за то, что написано ниже

options = webdriver.FirefoxOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
driver = webdriver.Firefox(options=options)
whitebit_parser = parsers.WhitebitParser(driver)

calculator = Calculate(whitebit_parser)

bot = telebot.TeleBot("5674369003:AAGMjRQM0GYBdFbzK-i6ObMRMK2ENmVqZow")

# @bot.message_handler(commands = ['help'])
# def start(message):
#     mess = f"Текущий курс USDT -> UAH - {whitebitUSDT}"
#     bot.send_message(message.chat.id, mess, parse_mode='html')

print("started")
@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("WHITEBIT")
    btn2 = types.KeyboardButton("BINANCE")
    btn3 = types.KeyboardButton("Ещё...")
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id,
                     text=f"Выберите вариант".format(
                         message.from_user), reply_markup=markup)


@bot.message_handler(content_types=["text"])
def func(message):
    if (message.text == "WHITEBIT"):
        bot.send_message(message.chat.id, text=f"Текущий курс USDT -> UAH - ")
    elif (message.text == "BINANCE"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("PrivatBank")
        btn2 = types.KeyboardButton("Monobank")
        btn3 = types.KeyboardButton("Pumb")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, btn3, back)
        bot.send_message(message.chat.id, text="хуй будешь?)", reply_markup=markup)


    elif (message.text == "PrivatBank"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id, text="Курс PrivatBank")
        bank = types.KeyboardButton("Расчитать PrivatBank")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(bank, back)

        bot.send_message(message.chat.id, text="Текущий курс - PrivatBank", reply_markup=markup)

    elif (message.text == "Расчитать PrivatBank"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.from_user.id, "Результаты: ")
        bot.send_message(message.from_user.id, f"{calculator.WtoBprivat(30000)} - 30000 UAH")

        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(back)
        bot.send_message(message.chat.id, text="" ,reply_markup=markup)

    elif (message.text == "Monobank"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id, text="Курс Monobank")
        bank = types.KeyboardButton("Расчитать Monobank")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(bank, back)

        bot.send_message(message.chat.id, text="Текущий курс Monobank -", reply_markup=markup)


    elif (message.text == "Расчитать Monobank"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.from_user.id, "Результаты: ")
        # bot.send_message(message.from_user.id, f"{resMono[0]} - 30000 UAH")
        # bot.send_message(message.from_user.id, f"{resMono[1]} - 25000 UAH")
        # bot.send_message(message.from_user.id, f"{resMono[2]} - 20000 UAH")
        # bot.send_message(message.from_user.id, f"{resMono[3]} - 15000 UAH")
        # bot.send_message(message.from_user.id, f"{resMono[4]} - 10000 UAH")
        # bot.send_message(message.from_user.id, f"{resMono[5]} - 50000 UAH")

        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(back)

        bot.send_message(message.chat.id, text="" ,reply_markup=markup)

    elif message.text == "Pumb":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id, text="Курс Pumb")
        bank = types.KeyboardButton("Расчитать Pumb")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(bank, back)

        bot.send_message(message.chat.id, text="Текущий курс Pumb -", reply_markup=markup)

    elif (message.text == "Расчитать Pumb"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.from_user.id, "Результаты: ")
        # bot.send_message(message.from_user.id, f"{resPumb[0]} - 30000 UAH")
        # bot.send_message(message.from_user.id, f"{resPumb[1]} - 25000 UAH")
        # bot.send_message(message.from_user.id, f"{resPumb[2]} - 20000 UAH")
        # bot.send_message(message.from_user.id, f"{resPumb[3]} - 15000 UAH")
        # bot.send_message(message.from_user.id, f"{resPumb[4]} - 10000 UAH")
        # bot.send_message(message.from_user.id, f"{resPumb[5]} - 50000 UAH")

        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(back)
        bot.send_message(message.chat.id, text="", reply_markup=markup)


    elif (message.text == "Ещё..."):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button2 = types.KeyboardButton("Обновить курс")
        back = types.KeyboardButton("Вернуться в главное меню")

        markup.add(button2, back)
        bot.send_message(message.chat.id, text="Задай мне вопрос", reply_markup=markup)

    elif (message.text == "Обновить курс"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        #Тут должны обновляться 4 парсера,после должно выбивать в главное меню

        bot.send_message(message.chat.id, text="Курс обновлён", reply_markup=markup)

    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("WHITEBIT")
        button2 = types.KeyboardButton("BINANCE")
        button3 = types.KeyboardButton("Ещё...")
        markup.add(button1, button2, button3)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, text="UNKNOWN COMMAND")
        bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEGELZjRo92kyFCdNuBEIgTFlbpim7JQAACXBUAAqgKyUt0AAHgi4b3gxYqBA")
    if (message.text == "STOP"):
        driver.quit()
bot.polling(none_stop=True)