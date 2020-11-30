import config
import telebot
from telebot import types

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=["start"])
def first_command(message):
    bot.send_message(message.chat.id, "Добро пожаловать в RatHouse❗️\n\n◼️ Здесь ты можешь воспользоваться всеми возможными теневыми услугами\n\n◼️ Хочешь научиться работать по-черному, но у тебя нет нужных материалов - ты попал по адресу!\n\n◼️ В RatHouse присутствует доска объявлений о поиске сотрудников, а также реферальная система с помощью которых вы сможете заработать\n\n◼️ Огромный выбор услуг и товаров")
    start = telebot.types.ReplyKeyboardMarkup(True, False)
    start.row('🗂 Каталог товаров', '👤 Мой кабинет')
    start.row('🛍 Мои покупки', '💌 Отзывы')
    start.row('🏛 Новости', '💼 Контакты')
    start.row('🎁 Халява', '⚠️Скидки')
    start.add('Работа с RatHouse')
    bot.send_message(message.from_user.id, 'Выберите нужный раздел: ', reply_markup=start)


@bot.message_handler(commands=["help"])
def send_help(message):
    bot.send_message(message.chat.id, "Список доступных команд:\n\n/start - Для начала работы с ботом\n/help - Список доступных команд\n/info - Узнать информацию о боте\n\n⚙️Этот раздел пока находится в разработке")


@bot.message_handler(commands=["info"])
def send_help(message):
    bot.send_message(message.chat.id, "Мой создатель - @por0vos1k. Он гениальный программист и хакер, ведь уже в 5 лет взломал пентагон!")


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        if call.data == '🔑Софт':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выберите подкатегорию")
            keyboard = types.InlineKeyboardMarkup()
            but_1 = types.InlineKeyboardButton(text="Взлом VK", callback_data="Взлом VK")
            but_2 = types.InlineKeyboardButton(text="Софт Магнита", callback_data="Софт Магнита")
            but_3 = types.InlineKeyboardButton(text="Adobe Photoshop", callback_data="Adobe Photoshop")
            keyboard.row(but_1)
            keyboard.row(but_2)
            keyboard.row(but_3)
            bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, inline_message_id=call.inline_message_id, reply_markup=keyboard)
        elif call.data == '💳 Деньги':
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="🔨Этот раздел еще в разработке")
        elif call.data == '📚Схемы':
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="🔨Этот раздел еще в разработке")
        elif call.data == '🛒Услуги':
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="🔨Этот раздел еще в разработке")
        elif call.data == '🗂Обучение':
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="🔨Этот раздел еще в разработке")
        elif call.data == '🎮Аккаунты':
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="🔨Этот раздел еще в разработке")
        elif call.data == '🍔Еда за 40%':
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="🔨Этот раздел еще в разработке")
        elif call.data == '📎Товары':
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="🔨Этот раздел еще в разработке")
        else:
            bot.send_message(call.message.chat.id, "Ничего не понятно!\n\nСписок доступных команд /help")

@bot.message_handler(content_types=["text"])
def send_otziv(message):
    if message.text == '💌 Отзывы':
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Оставить первый отзыв", url="https://t.me/g5u675fvm")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "💌 Отзывы\n\nЧестные отзывы о нашем магазине, по ссылке ниже", reply_markup=keyboard)
    elif message.text == '🏛 Новости':
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Присоединиться", url="https://t.me/joinchat/AAAAAFj0WHiR5Eq-5KHWTg")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "❗️Наш новостной канал - https://t.me/joinchat/AAAAAFj0WHiR5Eq-5KHWTg", reply_markup=keyboard)
    elif message.text == '💼 Контакты':
        bot.send_message(message.chat.id, "📎Контакты:\n\n◼️ Если что-то случилось - @por0vos1k\n◼️ Наши другие проекты - @kykl0vod\n\nУслуги гаранта(5%) - @Kukol6 ✔️")
    elif message.text == '⚠️Скидки':
        bot.send_message(message.chat.id, "Скидок нет)")
    elif message.text == '🎁 Халява':
        bot.send_message(message.chat.id, "Халявы не бывает))))")
    elif message.text == 'Работа с RatHouse':
        bot.send_message(message.chat.id, "На данный момент работы нет...")
    elif message.text == '🗂 Каталог товаров':
        keyboard = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text="💳 Деньги", callback_data="💳Деньги")
        but_2 = types.InlineKeyboardButton(text="📚Схемы", callback_data="📚Схемы")
        but_3 = types.InlineKeyboardButton(text="🛒Услуги", callback_data="🛒Услуги")
        but_4 = types.InlineKeyboardButton(text="🗂Обучение", callback_data="🗂Обучение")
        but_5 = types.InlineKeyboardButton(text="🎮Аккаунты", callback_data="🎮Аккаунты")
        but_6 = types.InlineKeyboardButton(text="🍔Еда за 40%", callback_data="🍔Еда за 40%")
        but_7 = types.InlineKeyboardButton(text="📎Товары", callback_data="📎Товары")
        but_8 = types.InlineKeyboardButton(text="🔑Софт", callback_data="🔑Софт")
        keyboard.row(but_1)
        keyboard.row(but_2)
        keyboard.row(but_3)
        keyboard.row(but_4)
        keyboard.row(but_5)
        keyboard.row(but_6)
        keyboard.row(but_7)
        keyboard.row(but_8)
        bot.send_message(message.chat.id, "🗂 Каталог товаров\n\nВыберите категорию", reply_markup=keyboard)
    else:
        bot.send_message(message.chat.id, "Ничего не понятно!\n\nСписок доступных команд /help")




if __name__ == '__main__':
    bot.polling(none_stop=True)
