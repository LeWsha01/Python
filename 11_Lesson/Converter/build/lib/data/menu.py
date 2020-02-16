import requests
import os
import pandas
from converter.data import convert
from converter.data import req

# We store in a constant variable a link to the exchange rates of the NBRB website
RESPONSE = requests.get('http://www.nbrb.by/API/ExRates/Rates?Periodicity=0')


def menu():
    """
    Interactive program menu for working with the user.
    """

    try:
        if RESPONSE.status_code == 200:
            main_menu = req.get_data_from_uri(RESPONSE)
            flag = True
            while flag:
                try:
                    value = int(input(f'\t\t\tWELCOME!!!\t\t\t\n'
                                      f'\tThis is a currency converter program\n'
                                      f'Select an action:\n'
                                      f'1: List of all currencies\n'
                                      f'2: Converter currencies\n'
                                      f'3: Exit\n'))
                    if value == 1:
                        print(pandas.DataFrame(main_menu))
                        input('Press Enter')
                        os.system('clear')
                    elif value == 2:
                        convert.convert_data(main_menu)
                        input()
                    elif value == 3:
                        print('Goodbye')
                        flag = False
                        os.system('clear')
                    else:
                        print('Repeat Entry')
                        print()
                        os.system('clear')
                except ValueError:
                    print('Repeat Entry')
                    os.system('clear')
    except Exception(f'Error connect') as ex:
        print(ex)


