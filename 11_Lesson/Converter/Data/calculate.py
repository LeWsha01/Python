from converter.db.models import History, session


def calculation(first_cur, second_cur, how_m, currency, id):
    """
    Method for working with transferred data for currency calculation
    :param first_cur:  # first abbreviation
    :param second_cur: # second abbreviation
    :param how_m: # transfer amount
    :param currency: # list of currencies we work with
    :param currency: # Id of user
    :return: # get the answer
    """

    first_money = 0
    second_money = 0
    for_one = 0

    # Based on if the first currency BYN
    if first_cur.upper() == 'BYN':
        for key in currency:
            if key['Abbreviation'] == second_cur.upper():
                second_money = key['BYN']
        session.add(History(first_cur.upper(), how_m, second_cur.upper(), round(how_m / second_money, 4), id[0]))
        session.commit()
        return f'Conversion from {how_m} {first_cur.upper()} to {second_cur.upper()} completed: ' \
               f'{round(how_m / second_money, 4)} {second_cur.upper()}'

    # Based on if the second currency BYN
    elif second_cur.upper() == 'BYN':
        for key in currency:
            if key['Abbreviation'] == first_cur.upper():
                for_one = key['How many units']
                first_money = key['BYN']
        session.add(History(first_cur.upper(), how_m, second_cur.upper(), round(first_money * how_m, 4), id[0]))
        session.commit()
        return f'Conversion from {how_m} {first_cur.upper()} to {second_cur.upper()} completed: ' \
               f'{round(first_money / for_one * how_m, 4)} {second_cur.upper()}'

    else:
        for key in currency:
            if key['Abbreviation'] == first_cur.upper():
                for_one = key['How many units']
                first_money = key['BYN']
            elif key['Abbreviation'] == second_cur.upper():
                second_money = key['BYN']
        session.add(History(first_cur.upper(), how_m, second_cur.upper(),
                            round(first_money / for_one * how_m / second_money, 4), id[0]))
        session.commit()
        return f'Conversion from {how_m} {first_cur.upper()} to {second_cur.upper()} completed: ' \
               f'{round(first_money / for_one * how_m / second_money, 4)} {second_cur.upper()}'
