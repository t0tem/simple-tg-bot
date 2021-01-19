import json
import os
import time

import numpy as np
from scipy.special import softmax

from user_of_the_day_bot import settings
from user_of_the_day_bot.utils import get_cur_date, get_date, get_now
from user_of_the_day_bot.users import save_users, get_long_name, get_short_name


def load_winner_info(chat_id):
    path_to_file = settings.WINNER_PATH.format(chat_id)
    if os.path.exists(path_to_file):
        with open(path_to_file, 'r') as f:
            cur_winner = json.load(f)
    else:
        cur_winner = {}
    return cur_winner


def save_winner_info(chat_id, cur_winner):
    path_to_file = settings.WINNER_PATH.format(chat_id)
    with open(path_to_file, 'w') as f:
        json.dump(cur_winner, f)


def get_random_winner(users):
    """
    не настоящий рандом, более _справедливый_. вероятности зависят от количества предыдущих побед.
    :param users:
    :return:
    """
    user_ids = []
    prev_win_cnts = []

    for k, v in users.items():
        user_ids.append(k)
        prev_win_cnts.append(-v['win_count'])  # добавляем отрицательный каунт на 'инвертированного' softmax

    probs = softmax(prev_win_cnts)
    winner_id = np.random.choice(user_ids, p=probs)

    return winner_id


def get_random_phrases():
    idx = np.random.choice(len(settings.WINNER_ANNOUNCEMENTS))
    return settings.WINNER_ANNOUNCEMENTS[idx]


def check_save_winner(context, chat_id, users):
    cur_winner = load_winner_info(chat_id)
    last_win_time = cur_winner.get('win_time', '2021-01-01T01:01:01.001')
    last_win_date = get_date(last_win_time)
    cur_date = get_cur_date()

    if cur_date > last_win_date:
        winner_id = get_random_winner(users)

        # сохраняем инфо и победителе
        cur_winner = {
            'win_time': get_now(),
            'winner_id': winner_id
        }
        save_winner_info(chat_id, cur_winner)

        # получаем строку с именем победителя
        winner_name = get_long_name(users, winner_id)

        # получаем 2 фразы
        phrase1, phrase2 = get_random_phrases()

        # отправляем
        context.bot.send_message(
            chat_id=chat_id,
            text=phrase1
        )
        time.sleep(2)
        context.bot.send_message(
            chat_id=chat_id,
            text=phrase2.format(winner_name)
        )

        # апдейтим каунты побед
        users[winner_id]['win_count'] += 1
        save_users(chat_id, users)

    else:
        old_winner = get_short_name(users, cur_winner['winner_id'])
        context.bot.send_message(
            chat_id=chat_id,
            text=f"Cегодня уже все понятно: победил(-а) {old_winner}. Возвращайся завтра \N{winking face}"
        )


def get_random_user(context, chat_id, users):
    """просто получить рандомного юзера, ничего не апдейтим"""

    winner_id = get_random_winner(users)
    winner_name = get_short_name(users, winner_id)

    context.bot.send_message(
        chat_id=chat_id,
        text=winner_name
    )
