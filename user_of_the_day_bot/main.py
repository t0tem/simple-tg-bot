from telegram.ext import Updater, CommandHandler

from user_of_the_day_bot.users import (
    check_reg_user,
    check_delete_user,
    list_users,
    load_users,
    get_top_users,
)
from user_of_the_day_bot.winners import check_save_winner


def user_reg(update, context):
    chat_id = update.message.chat_id
    effective_user = update.effective_user
    check_reg_user(context, chat_id, effective_user)


def user_del(update, context):
    chat_id = update.message.chat_id
    effective_user = update.effective_user
    check_delete_user(context, chat_id, effective_user)


def user_list(update, context):
    chat_id = update.message.chat_id
    list_users(context, chat_id)


def get_winner(update, context):
    chat_id = update.message.chat_id
    users = load_users(chat_id)
    check_save_winner(context, chat_id, users)


def user_stats(update, context):
    chat_id = update.message.chat_id
    get_top_users(context, chat_id)


def main():
    with open('user_of_the_day_bot.token', 'r') as f:
        token = f.read()
    updater = Updater(token, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('reg', user_reg))
    dp.add_handler(CommandHandler('delete_me', user_del))
    dp.add_handler(CommandHandler('players', user_list))
    dp.add_handler(CommandHandler('run', get_winner))
    dp.add_handler(CommandHandler('stats', user_stats))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
