from telegram.ext import Updater, CommandHandler


def hello(update, context):
    chat_id = update.message.chat_id

    context.bot.send_message(
        chat_id=chat_id,
        text='привет'
    )


def main():
    token = ''
    updater = Updater(token, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('hello', hello))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
