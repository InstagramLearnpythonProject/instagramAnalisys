# -*- coding: utf-8 -*-
import os 
import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from get_hashtag import get_comments_by_tag

PROXY = {#'proxy_url': 'socks5://t1.learn.python.ru:1080',

'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

teleg_log=logging.getLogger('telegram.ext.updater')

def greet_user(bot, update):
    text = 'Вызван /start'
    logging.info(text)
    update.message.reply_text(text)

def find_post(bot, update):    
    
    counter = get_comments_by_tag(update.message.text, 50)
    
    bot.send_message(chat_id=update.message.chat_id, text = 'Вы только что ввели хештег')
    bot.send_message(chat_id=update.message.chat_id, text = 'Количество постов по вашему хештегу = %s'%counter)

    bot.send_message(chat_id=update.message.chat_id, text = 'Файлы с описаниями постов:')        
    for one in os.listdir(update.message.text):        
        print(os.path.join(update.message.text, one))        
        document = open(os.path.join(update.message.text, one), 'r').read()              
        bot.send_message(chat_id=update.message.chat_id, text = document) 
    

def main():
    mybot = Updater("650028034:AAH-dqfS_nkiSA7DTLzpSihJKRz8aX3eGJg", request_kwargs=PROXY)
   
    logging.info('Обожемой, бот кому-то понадобился!')

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))    
    dp.add_handler(MessageHandler(Filters.text, find_post))    

    mybot.start_polling()
    mybot.idle()


main()
