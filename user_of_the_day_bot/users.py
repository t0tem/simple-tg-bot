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


def get_name(users, user_id_str):
    fullname = users[user_id_str]['fullname']
    if users[user_id_str]['username']:
        username = users[user_id_str]['username']
        return f'{fullname} (@{username})'
    else:
        return fullname


def check_reg_user(context, chat_id, effective_user):

    # грузим список юзеров, зарегеных из этого чата
    users = load_users(chat_id)
    user_id_str = str(effective_user.id)

    # если юзер в списке
    if user_id_str in users:

        # отвечаем что уже есть
        context.bot.send_message(
            chat_id=chat_id,
            text=f'ты уже есть в списке игроков, {effective_user.full_name}!'
        )
    else:
        # инача добавляем и говорим что добавлен
        users[user_id_str] = {
            'id': effective_user.id,
            'fullname': effective_user.full_name,
            'username': effective_user.username,
            'win_count': 0,
        }
        context.bot.send_message(
            chat_id=chat_id,
            text=f'теперь ты в игре, {effective_user.full_name}!'
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
        context.bot.send_message(
            chat_id=chat_id,
            text=f'ты больше не играешь, {effective_user.full_name} \N{slightly frowning face} приходи еще!'
        )
        del users[user_id_str]
    else:
        # иначе говорим что и не было
        context.bot.send_message(
            chat_id=chat_id,
            text=f'хм, а тебя и так нет среди игроков, {effective_user.full_name}.'
        )

    # пересохраняем юзеров
    save_users(chat_id, users)


def list_users(context, chat_id):

    # грузим список юзеров, зарегеных из этого чата
    users = load_users(chat_id)

    # формируем строку с юзерами
    list_of_users_str = '\n'.join([get_name(users, user_id_str) for user_id_str in users])

    context.bot.send_message(
        chat_id=chat_id,
        text=f'Сейчас в игре {len(users)} человек(-а):\n{list_of_users_str}',
    )


def get_top_users(context, chat_id):
    # грузим список юзеров, зарегеных из этого чата
    users = load_users(chat_id)

    # получаем айдишники юзеров и кол-во побед по-убыванию
    top_users_tuples = sorted(
        [(id_, v['win_count']) for id_, v in users.items() if v['win_count'] > 0],
        key=lambda x: x[1],
        reverse=True,
    )
    top_users_stats = [f"{i+1}) {get_name(users, el[0])} - {el[1]} раз(-а)" for i, el in enumerate(top_users_tuples)]
    top_users_stats_str = '\n'.join(top_users_stats)
    context.bot.send_message(
        chat_id=chat_id,
        text=f'\U0001F389 Текущие результаты игры Красавчик Дня:\n{top_users_stats_str}',
    )
