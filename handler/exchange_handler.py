from telebot.apihelper import ApiTelegramException

from util.bot import bot
from util.config import directions, base_cur
from util.data import data
from keyboard.exit_menu import exit_menu
from util.validator import is_correct_number


@bot.callback_query_handler(func=lambda x: x.data in directions)
def exchange_callback_handler(call):
    src = call.data.split('_')[0]
    dest = call.data.split('_')[2]

    msg = bot.edit_message_text(chat_id=call.message.chat.id,
                                text=f'Введіть сумму в *{src.upper()}*:',
                                message_id=call.message.id,
                                parse_mode='markdown',
                                reply_markup=exit_menu)

    bot.register_next_step_handler(message=msg, callback=exchange_callback, src=src, dest=dest, msg_id=msg.id)


def exchange_callback(message, src, dest, msg_id):
    try:
        is_correct_number(message.text)
        src_amount = float(message.text)
        dest_amount = get_exchange(src_amount, src, dest)

        bot.edit_message_text(chat_id=message.chat.id,
                              message_id=msg_id,
                              text=f"За {round(src_amount, 2):,} {src.upper()} можна купити {dest_amount:,} {dest.upper()}")
    except ValueError:
        try:
            msg = bot.edit_message_text(chat_id=message.chat.id,
                                        text=f"Помилка значення, спробуйте ще раз:",
                                        message_id=msg_id,
                                        parse_mode='markdown',
                                        reply_markup=exit_menu)
            bot.register_next_step_handler(message=msg, callback=exchange_callback, src=src, dest=dest, msg_id=msg_id)
        except ApiTelegramException:
            bot.register_next_step_handler(message=message, callback=exchange_callback, src=src, dest=dest,
                                           msg_id=msg_id)
    finally:
        bot.delete_message(chat_id=message.chat.id, message_id=message.id)


def get_exchange(amount, src, dest):
    if dest == base_cur:
        return round(amount * float(data['buy'][src]), 2)
    else:
        return round(amount / float(data['sale'][dest]), 2)
