import json
import os
import random

from user_of_the_day_bot import settings
from user_of_the_day_bot.utils import get_cur_date, get_date, get_now


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
    random_user_id = random.choice(sorted(users))
    return random_user_id


def check_save_winner(context, chat_id, users):
    cur_winner = load_winner_info(chat_id)
    last_win_time = cur_winner.get('win_time', '2021-01-01T01:01:01.001')
    last_win_date = get_date(last_win_time)
    cur_date = get_cur_date()

    if cur_date > last_win_date:
        winner_id = get_random_winner(users)
        # TODO апдейт каунтов побед
        cur_winner = {
            'win_time': get_now(),
            'winner_id': winner_id
        }
        context.bot.send_message(
            chat_id=chat_id,
            text=f"и... выиграл(-а), {users[winner_id]['name']}!"  # TODO сюда смешные фразы
        )
        save_winner_info(chat_id, cur_winner)
    else:
        context.bot.send_message(
            chat_id=chat_id,
            text=f"про сегодня уже все понятно: победил(-а) {users[cur_winner['winner_id']]['name']}."
        )

