# -*- coding: utf-8 -*-

import telebot
from telebot import types

import config


bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['start'])
def first_command(message):
    bot.send_message(message.chat.id, "Welcome!")
    start = telebot.types.ReplyKeyboardMarkup(True, False)
    start.row('🗂 Product catalog', '👤 My account')
    start.row('🛍 My orders', '💌 Reviews')
    start.row('🏛 News', '💼 Contacts')
    start.row('🎁 Presents', '⚠️Sale')
    start.add('Job openings')
    bot.send_message(message.from_user.id, 'Select the desired section: ', reply_markup=start)


@bot.message_handler(commands=['help'])
def send_help(message):
    bot.send_message(message.chat.id, "List of available commands:\n\n/start - To start working with the bot\n/help - List of available commands\n/info - Find out information about the shop")


@bot.message_handler(commands=['info'])
def send_help(message):
    bot.send_message(message.chat.id, "My creator is @por0vos1k.\n\nThis project is on github: https://github.com/famaxth/FirstProject")


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        if call.data == '🔑Software':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Select a subcategory")
            keyboard = types.InlineKeyboardMarkup()
            but_1 = types.InlineKeyboardButton(text="Adobe Photoshop", callback_data="Adobe Photoshop")
            keyboard.row(but_1)
            bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, inline_message_id=call.inline_message_id, reply_markup=keyboard)
        elif call.data == '💳 Money':
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="🔨This section is still in development")
        elif call.data == '📚Schemes':
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="🔨This section is still in development")
        elif call.data == '🛒Services':
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="🔨This section is still in development")
        elif call.data == '🗂Courses':
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="🔨This section is still in development")
        elif call.data == '🎮Accounts':
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="🔨This section is still in development")
        elif call.data == '📎Products':
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="🔨This section is still in development")
        else:
            bot.send_message(call.message.chat.id, "Nothing is clear!\n\nList of available commands /help")


@bot.message_handler(content_types=['text'])
def send_otziv(message):
    if message.text == '💌 Reviews':
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Оставить первый отзыв", url="https://t.me/famaxth")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "💌 Отзывы\n\nЧестные отзывы о нашем магазине, по ссылке ниже", reply_markup=keyboard)
    elif message.text == '🏛 News':
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Присоединиться", url="https://t.me/famaxth")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "❗️Our channel for news. - https://t.me/famaxth", reply_markup=keyboard)
    elif message.text == '💼 Contacts':
        bot.send_message(message.chat.id, "◼️ If something happened - @por0vos1k")
    elif message.text == '⚠️Sale':
        bot.send_message(message.chat.id, "Oops... At the moment, all the shares have ended.")
    elif message.text == '🎁 Presents':
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Follow the link", url="https://habr.com/ru/company/vertdider/blog/403823/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "🎁 We have a small gift for you - the Harvard CS50 course in Russian.")
    elif message.text == 'Job openings':
        bot.send_message(message.chat.id, "Oops... At the moment there is no work.")
    elif message.text == '🗂 Product catalog':
        keyboard = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text="💳 Money", callback_data="💳Money")
        but_2 = types.InlineKeyboardButton(text="📚Schemes", callback_data="📚Schemes")
        but_3 = types.InlineKeyboardButton(text="🛒Services", callback_data="🛒Services")
        but_4 = types.InlineKeyboardButton(text="🗂Courses", callback_data="🗂Courses")
        but_5 = types.InlineKeyboardButton(text="🎮Accounts", callback_data="🎮Accounts")
        but_6 = types.InlineKeyboardButton(text="📎Products", callback_data="📎Products")
        but_7 = types.InlineKeyboardButton(text="🔑Software", callback_data="🔑Software")
        keyboard.row(but_1)
        keyboard.row(but_2)
        keyboard.row(but_3)
        keyboard.row(but_4)
        keyboard.row(but_5)
        keyboard.row(but_6)
        keyboard.row(but_7)
        bot.send_message(message.chat.id, "🗂 Product catalog\n\nSelect a category:", reply_markup=keyboard)
    else:
        bot.send_message(message.chat.id, "Nothing is clear!\n\nList of available commands /help")


if __name__ == '__main__':
    bot.polling(none_stop=True)
