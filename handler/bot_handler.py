from util.bot import bot
from keyboard.main_menu import main_menu
from keyboard.exchange_menu import exchange_menu


@bot.message_handler(commands=['start'])
def start_handler(message):
    bot.clear_step_handler_by_chat_id(message.chat.id)
    bot.send_message(chat_id=message.chat.id,
                     text=f'Вітаю, *{message.from_user.first_name}*!',
                     reply_markup=main_menu,
                     parse_mode='markdown')


@bot.message_handler(content_types=['text'])
def menu_handler(message):
    if message.text.lower() == 'обмін валют':
        bot.send_message(chat_id=message.chat.id,
                         text='Виберіть напрям обміну: ',
                         reply_markup=exchange_menu)


def exit_handler(message):
    bot.clear_step_handler_by_chat_id(message.chat.id)
    bot.send_message(chat_id=message.chat.id,
                     text=f'Дію скасовано',
                     reply_markup=main_menu)


@bot.callback_query_handler(func=lambda call: call.data == 'exit')
def call_exit(call):
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.id)
    bot.clear_step_handler_by_chat_id(call.message.chat.id)
    exit_handler(call.message)
