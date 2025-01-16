import logging
import os
from dotenv import load_dotenv
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Application, CommandHandler, ContextTypes
from telegram_bot1.images import (
    get_dog_image_url,
    get_cat_image_url,
    get_panda_image_url,
    get_red_panda_image_url,
    get_koala_image_url,
)


load_dotenv()

async def gav(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = get_dog_image_url()
    await update.message.reply_photo(url)

async def meow(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = get_cat_image_url()
    await update.message.reply_photo(url)

async def random_panda(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = get_panda_image_url()
    await update.message.reply_photo(url)

async def random_red_panda(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = get_red_panda_image_url()
    await update.message.reply_photo(url)

async def random_koala(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = get_koala_image_url()
    await update.message.reply_photo(url)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.args and context.args[0] == 'webapp':
        keyboard = [[InlineKeyboardButton("Open MiniApp", web_app={'url': os.getenv('MINIAPP_URL')})]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text("Welcome! Click the button to open the MiniApp:", reply_markup=reply_markup)
    else:
        await update.message.reply_text("Hello! Use the button to launch the MiniApp.")

def main():
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO
    )

    with open('random_dog_bot.token', 'r') as f:
        token = f.read().strip()

    application = Application.builder().token(token).build()

    application.add_handler(CommandHandler('random_dog', gav))
    application.add_handler(CommandHandler('random_cat', meow))
    application.add_handler(CommandHandler('random_panda', random_panda))
    application.add_handler(CommandHandler('random_red_panda', random_red_panda))
    application.add_handler(CommandHandler('random_koala', random_koala))
    application.add_handler(CommandHandler('start', start))

    logging.info("Starting bot...")
    application.run_polling()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        logging.info("Bot stopped by user (Ctrl+C)")