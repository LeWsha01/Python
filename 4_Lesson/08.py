

def palindrom_string(str_pal):
    if str_pal == str_pal[::-1]:
        return True
    else:
        return False


str_palin = input('Enter your string: ')
print(palindrom_string(str_palin))
