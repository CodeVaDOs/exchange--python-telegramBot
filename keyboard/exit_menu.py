from telebot import types

exit_menu = types.InlineKeyboardMarkup(row_width=3)

btn = types.InlineKeyboardButton('Скасувати', callback_data='exit')

exit_menu.add(btn)