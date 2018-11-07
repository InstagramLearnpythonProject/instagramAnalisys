from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging


PROXY = {'proxy_url': 'socks5://t1.learn.python.ru:1080',

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
    bot.send_message(chat_id=update.message.chat_id, text = 'Введите хэштег')
    # Получаем вводные данные
    hashtag = input(getattr ("Введите хештег (без #): "))
    amount = int(input(getattr("Введите количество публикаций по хештегу: ")))
    print(' ')
    # Получаем список хештегов
    h = bot.get_total_hashtag_medias(hashtag, amount=amount, filtration=False)
    # Удаляем повторяющиеся елементы
    posts = list(set(h))

def main():
    mybot = Updater("650028034:AAH-dqfS_nkiSA7DTLzpSihJKRz8aX3eGJg", request_kwargs=PROXY)
   

    logging.info('Обожемой, бот кому-то понадобился!')

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


main()