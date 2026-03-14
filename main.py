import telebot
import os
bot=telebot.TeleBot(os.environ.get('BOT_TOKEN'))
@bot.message_handler(commands=['start'])
def start(message):
 bot.reply_to(message,"DEC→HEX")
@bot.message_handler()
def convert(message):
 try:
  n=int(message.text)
  if n>=0:
   h=hex(n)[2:].upper()
   bot.reply_to(message,f"{n}={h}")
  else:
   bot.reply_to(message,"❌")
 except:
  bot.reply_to(message,"❌")
bot.infinity_polling()
