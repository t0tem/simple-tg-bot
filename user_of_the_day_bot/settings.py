import pytz

TIMEZONE = pytz.timezone('Europe/Moscow')
TIME_FORMAT = '%Y-%m-%dT%H:%M:%S.%f'

USERS_PATH = 'users_{}.json'
WINNER_PATH = 'winner_{}.json'

WINNER_ANNOUNCEMENTS = [
    [
        'Провожу опрос населения планеты...',
        '100% респондентов считают, что Красавчик Дня сегодня {}! \U0001f947'
    ],
    [
        'Ну очевидно же!',
        'Все конечно молодцы и все такое, но {} сегодня просто неподражаем(-а)! \U0001f451',
    ],
    [
        'Ого! Чтоб на одного человека за один день пришлось столько Красавчиковости - давно такого не было!',
        'Ну ты даёшь, {}! мое увожение! \U0001f929',
    ],
    [
        'Вселенский разум сообщает...',
        'Красавчик Дня сегодня {}! \U0001f52e',
    ],
    [
        'Мы ведём наш репортаж с церемонии вручения премии Оскар...',
        'Приз в номинации Красавчик Дня получает {}! \U0001f3c6',
    ],
    [
        'Колебание в силе чувствую я, новый Красавчик Дня во вселенной появился...',
        '{} это! \U0001f596',
    ],
    [
        'Созывайте старейшин! Духи явили шаману следующего Красавчика Дня...',
        'Все падают ниц перед {}! \U0001f647',
    ],
]
