"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход 
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите 
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите 
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging
import ephem
import datetime
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
)


PROXY = {
    'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {
        'username': 'learn', 
        'password': 'python'
    }
}


def greet_user(bot, update):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def get_planet(bot, update):
    
    text = update.message.text.split()
    planet = text[-1]
    time = str(datetime.datetime.now()).split()
    
    if planet == 'Mercury':
          searched_planet = ephem.Mercury(time[0])
          constellation = ephem.constellation(searched_planet)
          update.message.reply_text(constellation[1])
    elif planet == 'Venus':
          searched_planet = ephem.Venus(time[0])
          constellation = ephem.constellation(searched_planet)
          update.message.reply_text(constellation[1])
    elif planet == 'Mars':
          searched_planet = ephem.Mars(time[0])
          constellation = ephem.constellation(searched_planet)
          update.message.reply_text(constellation[1])
    elif planet == 'Jupiter':
          searched_planet = ephem.Jupiter(time[0])
          constellation = ephem.constellation(searched_planet)
          update.message.reply_text(constellation[1])
    elif planet == 'Saturn':
          searched_planet = ephem.Saturn(time[0])
          constellation = ephem.constellation(searched_planet)
          update.message.reply_text(constellation[1])
    elif planet == 'Uranus':
          searched_planet = ephem.Uranus(time[0])
          constellation = ephem.constellation(searched_planet)
          update.message.reply_text(constellation[1])
    elif planet == 'Neptune':
          searched_planet = ephem.Neptune(time[0])
          constellation = ephem.constellation(searched_planet)
          update.message.reply_text(constellation[1])
    elif planet == 'Earth':
          text = 'Please, choose another planet'
          update.message.reply_text(text)
    else:
         text = 'Sorry, this is not a planet. Anyway the time is ' + ', '.join(time)
         update.message.reply_text(text)
    

def talk_to_me(bot, update):
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text)
 

def main():
    mybot = Updater("Код от BotFather", request_kwargs=PROXY)
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler("planet", get_planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    
    mybot.start_polling()
    mybot.idle()
       

if __name__ == "__main__":
    main()
