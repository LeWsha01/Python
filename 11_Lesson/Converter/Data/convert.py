import os


def calculation(first_cur, second_cur, how_m, currency):
    first_money = 0
    second_money = 0
    for_one = 0
    if first_cur.upper() == 'BYN':
        for key in currency:
            if key['Abbreviation'] == second_cur.upper():
                second_money = key['BYN']
        return f'Conversion from {how_m} {first_cur} to {second_cur} completed: ' \
               f'{round(how_m / second_money, 4)} {second_cur}'
    elif second_cur.upper() == 'BYN':
        for key in currency:
            if key['Abbreviation'] == first_cur.upper():
                first_money = key['BYN']
        return f'Conversion from {how_m} {first_cur} to {second_cur} completed: ' \
               f'{round(first_money * how_m, 4)} {second_cur}'
    else:
        for key in currency:
            if key['Abbreviation'] == first_cur.upper():
                for_one = key['How many units']
                first_money = key['BYN']
            elif key['Abbreviation'] == second_cur.upper():
                second_money = key['BYN']
        return f'Conversion from {how_m} {first_cur} to {second_cur} completed: ' \
               f'{round(first_money / for_one * how_m / second_money, 4)} {second_cur}'


def conv(cur):
    flag = True
    try:
        while flag:
            for key in cur:
                print(f"{key['Abbreviation']} - {key['Name']}")
            f_cur = input('\nChoose currency: ')
            s_cur = input('\nChoose the currency to which to transfer: ')
            for key in cur:
                if f_cur.upper() in key['Abbreviation'] or f_cur.upper() == 'BYN':
                    flag = True
                    break
                else:
                    print('Try one more')
                    flag = False
                    break
            if flag:
                for key in cur:
                    if s_cur.upper() in key['Abbreviation'] or s_cur.upper() == 'BYN':
                        flag = True
                        break
                    else:
                        print('Try one more')
                        flag = False
                        break
            if flag:
                money = int(input(f'How much to convert from {f_cur.upper()} to {s_cur.upper()}?\n'))
                print(calculation(f_cur, s_cur, money, cur))
                input('Press Enter')
                flag = False
    except ValueError:
        print('Try one more')
        os.system('clear')
