import telebot
import os

bot=telebot.TeleBot(os.environ.get('BOT_TOKEN'))

@bot.message_handler(commands=['start'])
def s(m):bot.reply_to(m,'DEC→HEX')

@bot.message_handler()
def c(m):
 try:
  n=int(m.text)
  bot.reply_to(m,f'{n}={hex(n)[2:].upper()}')
 except:bot.reply_to(m,'❌')

bot.infinity_polling()
            "• `1A3F` → 6847\n"
            "• `0xFF` → 255\n\n"
            "_Только цифры 0-9 и A-F_",
            parse_mode='Markdown'
        )

print("🚀 Hex-Dec Bot запущен!")
bot.infinity_polling()
