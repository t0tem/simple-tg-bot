from telegram.ext import Updater, CommandHandler

from telegram_bot1.images import (
    get_dog_image_url,
    get_cat_image_url,
    get_panda_image_url,
    get_red_panda_image_url,
    get_koala_image_url,
)


def gav(update, context):
    url = get_dog_image_url()
    chat_id = update.message.chat_id
    context.bot.send_photo(chat_id=chat_id, photo=url)


def meow(update, context):
    url = get_cat_image_url()
    chat_id = update.message.chat_id
    context.bot.send_photo(chat_id=chat_id, photo=url)


def random_panda(update, context):
    url = get_panda_image_url()
    chat_id = update.message.chat_id
    context.bot.send_photo(chat_id=chat_id, photo=url)


def random_red_panda(update, context):
    url = get_red_panda_image_url()
    chat_id = update.message.chat_id
    context.bot.send_photo(chat_id=chat_id, photo=url)


def random_koala(update, context):
    url = get_koala_image_url()
    chat_id = update.message.chat_id
    context.bot.send_photo(chat_id=chat_id, photo=url)


def main():
    with open('random_dog_bot.token', 'r') as f:
        token = f.read().strip()
    updater = Updater(token, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('random_dog', gav, run_async=True))
    dp.add_handler(CommandHandler('random_cat', meow, run_async=True))
    dp.add_handler(CommandHandler('random_panda', random_panda, run_async=True))
    dp.add_handler(CommandHandler('random_red_panda', random_red_panda, run_async=True))
    dp.add_handler(CommandHandler('random_koala', random_koala, run_async=True))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
