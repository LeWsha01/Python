from collections import Counter
from operator import itemgetter
from random import choice
from string import ascii_letters
import bisect
import datetime
import itertools
import random
import string
import time





start_time = time.time()

# 1.
# year = int(input('Enter year'))
# month = int(input('Enter month'))
# day = int(input('Enter day'))
# date = datetime.datetime(year, month, day, 0, 0, 0)
# now = datetime.datetime.now()
# print(now - date)


# 2.0
# def lst_compil(lst_1):
#     new_lst = tuple(itertools.combinations(lst_1, 2))
#     print('This list {0} -> {1}'.format(lst_1, new_lst))
#
#
# lst = [72, 586, 12, 1]
# lst_compil(lst)


# 2.1
# lst = [72, 586, 12, 1]
# new_list = []
# new_list.append(72)
# new_list.append(586)
# new_list.append(12)
# print(tuple(new_list))


# 3
# n = int(input('How many lines will be?'))
# big_string = str()
# for i in range(1, n + 1):
#     big_string += str(input('Enter your {0} string'.format(i)))
# dict_of_chars = Counter(big_string).most_common(1)
# print(dict_of_chars)


# 4
# dig_of_seven = [value for value in range(0, 1000) if value % 7 == 0]
# print(dig_of_seven)


# 5
# sum_of_digit = 0
# for i in range(1, 20000):
#     if len(str(i)) == 3:
#         sum_of_digit += i
#     else:
#         continue
# print(sum_of_digit)


# 5.1
# digits = [i for i in range(1, 20000) if 99 < i < 1000]
# print(sum(digits))
# print("--- {0} seconds ---".format(time.time() - start_time))


# 6
# doc_text = open('/Users/user/Desktop/Python/text.txt', 'r')
# word_list = doc_text.read().split()
# words = []
# text = doc_text.read()
# lst = text.split()
# print(Counter(lst).most_common(10))


# 7
# lst_of_letters = []
# rnd = random.randint(1, 4)
# rng = int(input('Enter your size of list: '))
# for i in range(rng):
#     lst_of_letters.append(''.join(choice(ascii_letters) for ind in range(rnd)))
# print(lst_of_letters)


# 8
# second_lst_of_letters = []
# for item in lst_of_letters:
#     second_lst_of_letters.append(item[::-1])
# print((sorted(second_lst_of_letters, key=


# 9
# start = int(input('Enter start random: '))
# end = int(input('Enter End random: '))
# lst_of_digits = [random.randint(start, end) for i in range(5, 10)]
# lst_of_digits.sort()
# new_dig = [random.randint(start, end) for i in range(5)]
# for item in new_dig:
#     print('This digit {0} in this list -> {1}'.format(item, lst_of_digits))
#     bisect.insort(lst_of_digits, item)
# print('New list with all digit -> {0}'.format(lst_of_digits))


# 10
# lst_of_lst = [[2, 12], [23, 21], [5, 32], [14, 19], [31, 8]]
# lst_of_lst.sort(key=lambda x: sum(x), reverse=True)
# print(lst_of_lst)