from argparse import ONE_OR_MORE
import logging
import config as c
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

move='XO'
playerSymbol = CrossesOrToe[random.randint(0, 1)]
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

def clear():
    global gameGround
    gameGround = [" ", " ", " ",
                  " ", " ", " ",
                  " ", " ", " ", ]
def start(update, _):
  #  global markup
  item=[]
   # 
  for i in range(0,3):
    for x in  range(0,3):
        item.append(InlineKeyboardButton("q", callback_data='q'))
  #      i+=1
    
    bot_keyboard = [[InlineKeyboardButton(" ",callback_data='1'),
                InlineKeyboardButton(" ",callback_data='1'),   
                InlineKeyboardButton(" ",callback_data='1')],

                ]
    reply_markup = InlineKeyboardMarkup(bot_keyboard)
    update.message.reply_text('Пожалуйста, выберите:', reply_markup=reply_markup)


updater = Updater(c.TOKEN)
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.start_polling()
updater.idle()