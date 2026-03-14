import telebot
import os

BOT_TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "DEC → HEX\nПришли число:")

@bot.message_handler()
def dec_to_hex(message):
    try:
        num = int(message.text)
        if num >= 0:
            hex_val = hex(num)[2:].upper()
            bot.reply_to(message, f"{num} = {hex_val}")
        else:
            bot.reply_to(message, "❌")
    except:
        bot.reply_to(message, "❌")

print("🚀 Dec-Hex Bot")
bot.infinity_polling()
            "• `6847` → `1A3F`\n"
            "• `10` → `A`\n\n"
            "_Целые числа ≥ 0_",
            parse_mode='Markdown'
        )

print("🚀 Dec → Hex Bot запущен!")
bot.infinity_polling()
            message,
            "❌ *Ошибка!*\n\n"
            "✅ Правильно:\n"
            "• `FF` → 255\n"
            "• `1A3F` → 6847\n"
            "• `0xFF` → 255\n\n"
            "_Только цифры 0-9 и A-F_",
            parse_mode='Markdown'
        )

print("🚀 Hex-Dec Bot запущен!")
bot.infinity_polling()
