import telebot

API_TOKEN = '8023969883:AAF2eqluMfaQrUdBWMYiOo3zM8Rs6gY1KVo'

# Створюємо екземпляр бота
bot = telebot.TeleBot(API_TOKEN)

# Обробка команди /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привіт! Я простий Telegram бот на Python.")

# Обробка звичайних повідомлень
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

# Запускаємо бота
bot.polling()
