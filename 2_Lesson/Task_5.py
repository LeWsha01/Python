

lst = [2, 73, 43, 13, 23]

a, b = lst[0], lst[1]
if b < a:
    a, b = b, a
for index in range(2, len(lst) - 1):
    if lst[index] > b:
        a, b = b, lst[index]
    elif lst[index] > a:
        a = lst[index]

print(a, b)
