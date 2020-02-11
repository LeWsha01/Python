import requests
import os
import pandas
from Converter.Data.req import uri_link, ErrorConnect
from Converter.Data.convert import conv

if __name__ == '__main__':
    try:
        response = requests.get('http://www.nbrb.by/API/ExRates/Rates?Periodicity=0')
        if response.status_code < 400:
            menu = uri_link(response)
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
                        print(pandas.DataFrame(menu))
                        input('Press Enter')
                        os.system('clear')
                    elif value == 2:
                        conv(menu)
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
        else:
            raise ErrorConnect(f'Error: {response.status_code}')
    except ErrorConnect as ex:
        print(ex)