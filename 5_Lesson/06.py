

def convert_spaces(string):
    print(string, '-> ', end='')
    for item in string:
        if str.isspace(item):
            print('-', end='')
        else:
            print(item, end='')


string_spaces = 'Hello World MFK!!'
convert_spaces(string_spaces)