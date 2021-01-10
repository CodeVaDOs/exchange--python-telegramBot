from telebot import types

exchange_menu = types.InlineKeyboardMarkup(row_width=2)


btn1 = types.InlineKeyboardButton(text="Гривні в долари", callback_data='uah_to_usd')
btn2 = types.InlineKeyboardButton(text="Долари в гривні", callback_data='usd_to_uah')

btn3 = types.InlineKeyboardButton(text="Гривні в євро", callback_data='uah_to_eur')
btn4 = types.InlineKeyboardButton(text="Євро в гривні", callback_data='eur_to_uah')

btn5 = types.InlineKeyboardButton(text="Гривні в рублі", callback_data='uah_to_rur')
btn6 = types.InlineKeyboardButton(text="Рублі в гривні", callback_data='rur_to_uah')

btn7 = types.InlineKeyboardButton(text="Гривні в біткоіни", callback_data='uah_to_btc')
btn8 = types.InlineKeyboardButton(text="Біткоіни в гривні", callback_data='btc_to_uah')

exchange_menu.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
