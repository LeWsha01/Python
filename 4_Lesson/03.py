

def sum_of_digits_word(*args):
    su = 0
    digits = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8,
              'nine': 9, 'ten': 10}
    digits_string = str()
    for item in range(len(args)):
        if str(args[item]).lower() in digits:
            digits_string += str(digits[str(args[item]).lower()]) + ' '
    for digit in digits_string.split():
        su += int(digit)
    print('Sum of digits words =', su)


sum_of_digits_word('Zero', 'One', 'Two', 'THREE', 'four', 'fIvE', 'sIx', 'SeVen', 'EIGht', 'NIne', 'tEN')
