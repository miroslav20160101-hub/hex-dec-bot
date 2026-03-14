import telebot
import os

# Токен из переменных Bothost (НИКОГДА не вставляйте сюда!)
BOT_TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def start(message):
    bot.reply_to(
        message,
        "🔄 *DEC → HEX Конвертер*\n\n"
        "Пришли число в **десятичной** системе:\n\n"
        "• `255` → `FF`\n"
        "• `6847` → `1A3F`\n"
        "• `175` → `AF`\n\n"
        "_Только целые неотрицательные числа_",
        parse_mode='Markdown'
    )

@bot.message_handler(func=lambda m: True)
def dec_to_hex(message):
    text = message.text.strip()
    
    try:
        # Преобразуем DEC в число
        decimal = int(text)
        
        if decimal < 0:
            raise ValueError("Отрицательное число")
            
        # Переводим в HEX (верхний регистр, без 0x)
        hex_value = hex(decimal)[2:].upper()
        
        bot.reply_to(
            message,
            f"**{decimal:,}₁₀** = **{hex_value}₁₆**\n\n"
            f"_Десятичное → Шестнадцатеричное_\n"
            f"`0x{hex_value}`",
            parse_mode='Markdown'
        )
        
    except ValueError:
        bot.reply_to(
            message,
            "❌ *Ошибка!*\n\n"
            "✅ Примеры:\n"
            "• `255` → `FF`\n"
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
