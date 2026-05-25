import os
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

import telebot
from telebot import types

# Инициализация бота
bot = telebot.TeleBot(os.environ.get("BOT_TOKEN", ""))

# ── Minimal health-check HTTP server ─────────────────────────────────────────
class HealthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"OK")

    def log_message(self, format, *args):  # silence request logs
        pass

def run_health_server():
    port = int(os.environ.get("PORT", 8080))
    server = HTTPServer(("0.0.0.0", port), HealthHandler)
    server.serve_forever()

# Start the health server in a background thread
threading.Thread(target=run_health_server, daemon=True).start()
# ─────────────────────────────────────────────────────────────────────────────

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
