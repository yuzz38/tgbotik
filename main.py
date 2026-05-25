
import telebot
from telebot import types

# Инициализация бота
bot = telebot.TeleBot("8851926004:AAFhF4kH7VV-Z_5MaTSDFEIz9kcb_jZ2yJs")

# Реакция на команду /start
@bot.message_handler(commands=['start'])
def start_message(message):
    # Создаем удобные кнопки в меню
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Привет")
    btn2 = types.KeyboardButton("❓ Помощь")
    markup.add(btn1, btn2)
    
    bot.send_message(message.chat.id, f"Привет, {message.from_user.first_name}! Я твой личный бот без рекламы.", reply_markup=markup)

# Обработка текстовых сообщений и нажатий на кнопки
@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == "👋 Привет":
        bot.send_message(message.chat.id, "Рад тебя видеть! Чем могу помочь?")
    elif message.text == "❓ Помощь":
        bot.send_message(message.chat.id, "Тут можно описать функции твоего бота.")
    else:
        bot.send_message(message.chat.id, "Я получил твое сообщение, но пока не умею на него отвечать.")

# Запуск постоянной работы бота
bot.infinity_polling()
