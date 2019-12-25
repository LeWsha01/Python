

def func(a_2, b_2):
    flag = False
    for values in b_2:
        if a_2 == b_2[values]:
            flag = True
            break
    if flag:
        print('True')
    else:
        print('False')


a = 5
b = {'foo': 5, 'bar': 8}
func(a, b)
