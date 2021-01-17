import json
import os

from user_of_the_day_bot import settings


def load_users(chat_id):
    path_to_file = settings.USERS_PATH.format(chat_id)
    if os.path.exists(path_to_file):
        with open(path_to_file, 'r') as f:
            users = json.load(f)
    else:
        users = {}
    return users


def save_users(chat_id, users):
    path_to_file = settings.USERS_PATH.format(chat_id)
    with open(path_to_file, 'w') as f:
        json.dump(users, f)


def check_reg_user(context, chat_id, effective_user):

    # грузим список юзеров, зарегеных из этого чата
    users = load_users(chat_id)
    user_id_str = str(effective_user.id)

    # если юзер в списке
    if user_id_str in users:

        # отвечаем что уже есть
        context.bot.send_message(
            chat_id=chat_id,
            text=f'так ты уже зареген(-а), {effective_user.name}!'
        )
    else:
        # инача добавляем и говорим что добавлен
        users[user_id_str] = {
            'id': effective_user.id,
            'fullname': effective_user.full_name,
            'name': effective_user.name,
            'win_count': 0,
        }
        context.bot.send_message(
            chat_id=chat_id,
            text=f'теперь ты в игре, {effective_user.name}!'
        )

    # пересохраняем юзеров
    save_users(chat_id, users)


def check_delete_user(context, chat_id, effective_user):

    # грузим список юзеров, зарегеных из этого чата
    users = load_users(chat_id)
    user_id_str = str(effective_user.id)

    # если юзер в списке
    if user_id_str in users:

        # удаляем и говорим что удален
        del users[user_id_str]

        context.bot.send_message(
            chat_id=chat_id,
            text=f'ты больше не играешь, {effective_user.name} :( приходи еще!'
        )
    else:
        # иначе говорим что и не было
        context.bot.send_message(
            chat_id=chat_id,
            text=f'так ты и не играл(-а), {effective_user.name}!'
        )

    # пересохраняем юзеров
    save_users(chat_id, users)


def list_users(context, chat_id):

    # грузим список юзеров, зарегеных из этого чата
    users = load_users(chat_id)

    # формируем строку с юзерами
    list_of_users_str = '\n'.join([f"{v['fullname']} ({v['name']})" for k, v in users.items()])

    context.bot.send_message(
        chat_id=chat_id,
        text=f'Сейчас в игре {len(users)} человек(-а):\n{list_of_users_str}',
    )

