from my_token import TOKEN
from telegram.ext import Updater, MessageHandler, CallbackQueryHandler
from comands import *
updater = Updater(TOKEN)
updater.dispatcher.add_handler(MessageHandler(helloUser, hello))
updater.dispatcher.add_handler(MessageHandler(startGameForUser, start))
updater.dispatcher.add_handler(CallbackQueryHandler(button))
updater.dispatcher.add_handler(MessageHandler(userText, error))

print("Бот запущен.")
updater.start_polling()
updater.idle()