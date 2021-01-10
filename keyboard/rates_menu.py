from telebot import types

rates_menu = types.InlineKeyboardMarkup(row_width=1)

button1 = types.InlineKeyboardButton(text='Долар', callback_data='usd')
button2 = types.InlineKeyboardButton(text='Євро', callback_data='eur')
button3 = types.InlineKeyboardButton(text='Рубль', callback_data='rur')

rates_menu.add(button1, button2, button3)
