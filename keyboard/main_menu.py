from telebot import types

main_menu = types.ReplyKeyboardMarkup(resize_keyboard=True,
                                      one_time_keyboard=True,
                                      row_width=2)

# key1 = types.KeyboardButton("Курси валют")
key2 = types.KeyboardButton("Обмін валют")

main_menu.add(key2)