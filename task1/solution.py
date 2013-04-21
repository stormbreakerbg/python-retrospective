SIGNS = [
    ((1, 19), 'Козирог'),
    ((2, 18), 'Водолей'),
    ((3, 20), 'Риби'),
    ((4, 20), 'Овен'),
    ((5, 20), 'Телец'),
    ((6, 20), 'Близнаци'),
    ((7, 21), 'Рак'),
    ((8, 22), 'Лъв'),
    ((9, 22), 'Дева'),
    ((10, 22), 'Везни'),
    ((11, 21), 'Скорпион'),
    ((12, 21), 'Стрелец'),
    ((13, 0), 'Козирог'),
]


def what_is_my_sign(day, month):
    """ Return the horoscope sign according to the day and month. """
    for end_date, sign in SIGNS:
        if (month, day) <= end_date:
            return sign
