from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import ephem

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

PROXY = {
    'proxy_url': 'socks5://95.215.54.206:39880'}  # , 'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}


def greet_user(bot, update):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def talk_to_me(bot, update):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text('меня нет')


def start_planet(bot, update):
    text = 'Напечатайте планету на английском'
    print(text)
    update.message.reply_text(text)


def where_planet(bot, update):
    planet_text = update.message.text
    print(planet_text)
    if planet_text == 'Mercury':
        planet = ephem.Mercury()
    elif planet_text == 'Venus':
        planet = ephem.Venus()
    elif planet_text == 'Mars':
        planet = ephem.Mars()
    elif planet_text == 'Jupiter':
        planet = ephem.Jupiter()
    elif planet_text == 'Saturn':
        planet = ephem.Saturn()
    elif planet_text == 'Uranus':
        planet = ephem.Uranus()
    elif planet_text == 'Neptune':
        planet = ephem.Neptune()
    elif planet_text == 'Pluto':
        planet = ephem.Pluto()
    elif planet_text == 'Sun':
        planet = ephem.Sun()
    elif planet_text == 'Moon':
        planet = ephem.Moon()
    else:
        update.message.reply_text('Я не знаю такой планеты')
        return

    planet.compute()
    update.message.reply_text(ephem.constellation(planet))


def main():
    mybot = Updater("563596999:AAGv5xkz_OKmgXkPDLY9YRUyVsopsi6Pt2E", request_kwargs=PROXY)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", start_planet))
    dp.add_handler(MessageHandler(Filters.text, where_planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


main()
