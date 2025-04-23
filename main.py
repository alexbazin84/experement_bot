import telebot

bot = telebot.TeleBot('8177017767:AAFsYhvkG6p8cs8-lpuOyxtETeibIpfTGeI')

@bot.message_handler(commands=['start'])
def text_handler(m):
    bot.send_message(m.chat.id, 'Привет я Телеграм-Бот.')

bot.polling(none_stop=True)
