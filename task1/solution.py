SIGNS = (
    ('Козирог', range(0, 120)),
    ('Водолей', range(120, 218)),
    ('Риби', range(218, 321)),
    ('Овен', range(321, 421)),
    ('Телец', range(421, 521)),
    ('Близнаци', range(521, 621)),
    ('Рак', range(621, 722)),
    ('Лъв', range(722, 823)),
    ('Дева', range(823, 923)),
    ('Везни', range(923, 1023)),
    ('Скорпион', range(1023, 1122)),
    ('Стрелец', range(1122, 1222)),
    ('Козирог', range(1222, 1300)),
)


def what_is_my_sign(day, month):
    """ Return the horoscope sign according to the day and month. """
    date_code = month * 100 + day

    for sign, date_range in SIGNS:
        if date_code in date_range:
            return sign
