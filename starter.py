from util.bot import bot
import handler.bot_handler
import handler.exchange_handler

bot.enable_save_next_step_handlers(2)
bot.load_next_step_handlers()

bot.add_message_handler({handler.bot_handler})
bot.add_message_handler({handler.exchange_handler})

if __name__ == '__main__':
    bot.infinity_polling()
