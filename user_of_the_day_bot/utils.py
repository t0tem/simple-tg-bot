import datetime

from user_of_the_day_bot import settings


def get_now():
    return datetime.datetime.now(tz=settings.TIMEZONE).strftime(settings.TIME_FORMAT)


def get_date(time_str):
    return datetime.datetime.strptime(time_str, settings.TIME_FORMAT).date()


def get_cur_date():
    return get_date(get_now())
