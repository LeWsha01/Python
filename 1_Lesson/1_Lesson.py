# Операторы ветвления

import this

lst_a = []

'''a = input('Input number: ')
#a = 5
#a = None'''
a = 5.0

if isinstance(a, int):
    print(a + 10)
elif isinstance(a, str):
    lst_a.append(a)
    print(lst_a)
elif a is None:
    print('None')
else:
    print(a, type(a))


lst = list(range(100))
for i in range(len(lst) - 1):
    print(lst[i])


for i in range(1, 15):
    if i == 5:
        continue
    print(i)


for i in range(1, 15):
    if i == 5:
        break
    print(i)


a = []
b = 5
try:
    print(a + b) # TypeError
except TypeError as e:
    print('Exception, ', e)
print('Hello World')

