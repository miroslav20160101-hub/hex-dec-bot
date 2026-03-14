import telebot
import os

BOT_TOKEN = os.environ.get('8745996091:AAHjc9Vq9Nw7VVoYlLuFXa19U5EnEFjwJOg')
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(
        message,
        "🔢 *Hex → Decimal Converter*\n\n"
        "Пришли число в 16‑ичной системе:\n"
        "• `FF`\n"
        "• `1A3F`\n"
        "• `0xABC`\n\n"
        "_Только 0-9, A-F_",
        parse_mode='Markdown'
    )

@bot.message_handler(func=lambda m: True)
def convert_hex(message):
    text = message.text.strip().upper()
    if text.startswith("0X"):
        text = text[2:]
    
    try:
        value = int(text, 16)
        bot.reply_to(
            message,
            f"**{text}₁₆** = **{value:,}₁₀**\n\n"
            f"_({value})_\n"
            f"`{hex(value)}`",
            parse_mode='Markdown'
        )
    except ValueError:
        bot.reply_to(
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
