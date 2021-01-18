from telegram.ext import Updater, CommandHandler
import requests
import re


def get_dog_url():
    contents = requests.get('https://random.dog/woof.json').json()
    url = contents['url']
    return url


def get_dog_image_url():
    allowed_extension = ['jpg', 'jpeg', 'png']
    file_extension = ''
    while file_extension not in allowed_extension:
        url = get_dog_url()
        file_extension = re.search("([^.]*)$", url).group(1).lower()
    return url


def get_cat_image_url():
    contents = requests.get('http://aws.random.cat/meow').json()
    url = contents['file']
    return url


def gav(update, context):
    url = get_dog_image_url()
    chat_id = update.message.chat_id
    context.bot.send_photo(chat_id=chat_id, photo=url)


def meow(update, context):
    url = get_cat_image_url()
    chat_id = update.message.chat_id
    context.bot.send_photo(chat_id=chat_id, photo=url)


def main():
    with open('random_dog_bot.token', 'r') as f:
        token = f.read().strip()
    updater = Updater(token, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('random_dog', gav, run_async=True))
    dp.add_handler(CommandHandler('random_cat', meow, run_async=True))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
