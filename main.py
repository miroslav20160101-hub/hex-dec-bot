import os
import telebot

# Токен берём из переменных окружения (Bothost: BOT_TOKEN)
BOT_TOKEN = os.environ.get('BOT_TOKEN')

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def start(message):
    bot.reply_to(
        message,
        "Пришли десятичное число, я отвечу его значением в 16-й системе в формате 0x..."
    )

@bot.message_handler()
def dec_to_hex(message):
    try:
        n = int(message.text)          # пробуем преобразовать текст в целое число
        if n < 0:
            bot.reply_to(message, "❌")  # не принимаем отрицательные
            return

        hex_val = hex(n)[2:].upper()    # '0xff' -> 'ff'
        bot.reply_to(message, f"0x{hex_val}")
    except:
        bot.reply_to(message, "❌")      # если не число, отправляем ошибку

bot.infinity_polling()
