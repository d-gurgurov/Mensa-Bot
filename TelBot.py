from bs4 import BeautifulSoup  # BeautifulSoup is used for scrapping the web
from urllib.request import urlopen
import telegram.ext  # telegram.ext is used for creating bots
from googletrans import Translator  # google translate API

# My Telegram API
API_KEY = "5626079247:AAEQTf3qV-inlYruqLjVGcmBLUbSiw-N5zY"

# creating an instance of the translator
translator = Translator()
updater = telegram.ext.Updater(API_KEY, use_context=True)
dispatcher = updater.dispatcher

# scraping the website and retrieving the information
menu_page = urlopen("https://www.imensa.de/saarbruecken/mensa-saarbruecken/index.html")
artist_html = menu_page.read().decode("utf-8")
menu_soup = BeautifulSoup(artist_html, "html.parser")


# scraping dishes names from the website
def dishes_scrape(num):
    dish_all_html = menu_soup.find_all("p", {"class": "aw-meal-description"})
    dishes = []

    for element in dish_all_html:
        dishes.append(element)

    if num == 1:
        dish_1 = []
        for sub in dishes[0]:
            sub = str(sub)
            if sub != "<br/>":
                dish_1.append(sub)
        return dish_1

    if num == 2:
        dish_2 = []
        for sub in dishes[1]:
            sub = str(sub)
            if sub != "<br/>":
                dish_2.append(sub)
        return dish_2

    if num == 3:
        dish_3 = []
        for sub in dishes[2]:
            sub = str(sub)
            if sub != "<br/>":
                dish_3.append(sub)
        for sub in dishes[3]:
            sub = str(sub)
            if sub != "<br/>":
                dish_3.append(sub)
        return dish_3

    if num == 4:
        dish_4 = []
        for sub in dishes[4]:
            sub = str(sub)
            if sub != "<br/>":
                dish_4.append(sub)
        for sub in dishes[5]:
            sub = str(sub)
            if sub != "<br/>":
                dish_4.append(sub)
        return dish_4


# translating dishes names with googletrans
def dishes_translate(num):
    if num == 1:
        dish1_translation = []
        dish1 = dishes_scrape(1)
        for dish in dish1:
            translation = translator.translate(dish, src="de", dist="en")
            dish1_translation.append(translation.text)
        return dish1_translation
    if num == 2:
        dish2_translation = []
        dish2 = dishes_scrape(2)
        for dish in dish2:
            translation = translator.translate(dish, src="de", dist="en")
            dish2_translation.append(translation.text)
        return dish2_translation
    if num == 3:
        dish3_translation = []
        dish3 = dishes_scrape(3)
        for dish in dish3:
            translation = translator.translate(dish, src="de", dist="en")
            dish3_translation.append(translation.text)
        return dish3_translation
    if num == 4:
        dish4_translation = []
        dish4 = dishes_scrape(4)
        for dish in dish4:
            translation = translator.translate(dish, src="de", dist="en")
            dish4_translation.append(translation.text)
        return dish4_translation


print(dishes_translate(1))
print(dishes_translate(2))
print(dishes_translate(3))
print(dishes_translate(4))


# functions for the telegram bot
def start(update, context):
    update.message.reply_text("hey, wanna eat? write '/help' for more")


def help(update, context):
    update.message.reply_text(
        """
        /start -> welcome
        /content -> about
        /menu_a -> mensa menu A
        /menu_b -> mensa menu B
        /menu_c -> mensa menu C
        /menu_cafe -> mensa cafe
        /contact -> contact
        """
    )


def content(update, context):
    update.message.reply_text("Food options for today")


def menu_a(update, context):
    for part in dishes_translate(1):
        update.message.reply_text("- " + part)
    update.message.reply_text("Enjoy your meal!")


def menu_b(update, context):
    for part in dishes_translate(2):
        update.message.reply_text("- " + part)
    update.message.reply_text("Enjoy your meal!")


def menu_c(update, context):
    for part in dishes_translate(3):
        update.message.reply_text("- " + part)
    update.message.reply_text("Enjoy your meal!")


def menu_cafe(update, context):
    for part in dishes_translate("- " + 4):
        update.message.reply_text(part)
    update.message.reply_text("Enjoy your meal!")


def contact(update, context):
    update.message.reply_text("contact me - @d_gurgurov")


def menu(update, context):
    update.message.reply_text("menu link - https://www.imensa.de/saarbruecken/mensa-saarbruecken/index.html")


# adding the functions to the bot interface
dispatcher.add_handler(telegram.ext.CommandHandler("start", start))
dispatcher.add_handler(telegram.ext.CommandHandler("help", help))
dispatcher.add_handler(telegram.ext.CommandHandler("content", content))
dispatcher.add_handler(telegram.ext.CommandHandler("menu_a", menu_a))
dispatcher.add_handler(telegram.ext.CommandHandler("menu_b", menu_b))
dispatcher.add_handler(telegram.ext.CommandHandler("menu_c", menu_c))
dispatcher.add_handler(telegram.ext.CommandHandler("menu_cafe", menu_cafe))
dispatcher.add_handler(telegram.ext.CommandHandler("contact", contact))
dispatcher.add_handler(telegram.ext.CommandHandler("menu_a", menu))


# starting the bot
updater.start_polling()
updater.idle()
