import calendar
import datetime
import numpy
import os

def first_task(lst_f):
    print(lst_f[0::len(lst_f) - 1])


def second_task(lst_t):
    print('[', lst_t[len(lst) - 2], ']')


def third_task(n):
    first_number = str(n)
    second_number = str(n + n)
    third_number = str(n + n + n)
    four_number = str(n + n + n + n)
    print(first_number,'+',second_number, '+', third_number, '+', four_number,'=',
          int(first_number) + int(second_number) - int(third_number) * int(four_number))


def four_task(year, month):
    c = calendar.TextCalendar(0)
    print(c.formatmonth(year, month))


def five_task(f_d, s_d):
    f_d = f_d.split('_')
    s_d = s_d.split('_')
    start_date = datetime.date(int(f_d[0]), int(f_d[1]), int(f_d[2]))
    end_date = datetime.date(int(s_d[0]), int(s_d[1]), int(s_d[2]) + 1)
    print('Рабочие дни с', start_date, 'по', end_date, 'включая эти дни ->', numpy.busday_count(start_date, end_date))


def six_task(number):
    print('Square root of', number, '=', number ** .5)


def seven_task(lst_svn):
    max_d = 0
    count = 0
    count_d = 0
    for i in range(0, len(lst_svn)):
        count = 0
        for item in lst_svn:
            if item == lst_svn[i]:
                count += 1
        if count > count_d:
            count_d = count
            max_d = lst_svn[i]
    print('Количество дубликатов =', count_d, ', числа', max_d, 'в списке ->', lst_svn)


def eight_task(lst_eight):
    str_lst = str()
    for i in lst_eight:
        str_lst += str(i)
    print(str_lst)


def nine_task(lst_n):
    for i in range(0, len(lst_n)):
        if lst_n[i] == 237:
            for item in lst_n[i:]:
                if int(item) % 2 == 0:
                    print(item, end=', ')
                else:
                    continue


def ten_task(lst_a, lst_b):
    flag_ind = None  # Флаг для того что бы определять истина или лож
    for i in range(0, len(lst_a)):  # Ищем первое совпадение в списке "А"
        # Сравниваем элементы списка "А" с первым элементом списка "B"
        if lst_a[i] != lst_b[0]:
            continue
        elif lst_a[i] == lst_b[0]:  # Если элементы равны переходим в этот блок
            ind = i
            for item in range(0, len(lst_b)):
                if lst_b[item] == lst_a[ind]:
                    ind += 1
                    flag_ind = True
                else:
                    flag_ind = False
                    break
        if flag_ind == True:
            print('Список {0}, является подмасивом списка {1}'.format(lst_b, lst_a))
            break
        elif flag_ind == False:
            print('Список {0}, не является подмасивом списка {1}'.format(lst_b[:], lst_a[:]))
            break
    print('Список {0}, не является подмасивом списка {1}'.format(lst_b[:], lst_a[:]))


lst = ['Email:', 'SSN:', 'Address:', 'Home Phone:', 'Mobile Phone: ', 'DOB:', 'Date of Surgery:', 'Date of Service:',
        'Facility of Service:', 'Clinic Number:', 'Employer:', 'Work Phone: ', 'Fax: ', 'Type:', 'IPA:', 'Health Plan:',
        'ID #:', 'Claims Address:', 'Group #:', 'Claim # / PO #:', 'Phone:', 'Fax:', 'Contact', 'Adjuster Email',
        'Util Review Phone', 'Util Review Fax', 'Doctor:', 'NPI #: ', 'Date of Injury: ', 'Body Parts:',
       'Body Part Side:', 'Gender:', 'Diagnosis:', 'Diagnosis 2:', 'Procedure:']


numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 918, 237,
           412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843,
           831, 445, 742, 717, 958, 743, 527]

flag = True
while(flag):
    os.system('clear')
    print('1. Программа выводит на консоль первый и последний элемент списка.')
    print('2. Программи выводит на консоль предпоследний элемент списка.')
    print('3. Программа выводит на консоль n + nn - nnn * nnnn, пример: \nчисло 5 \n5 + 55 - 555 * 5555 = -3082965')
    print('4. Программа выводит введенный месяц в виде календаря.')
    print('5. Программа возвращает количество рабочих дней между ними (пн, вт, ср, чт, пт - рабочие дни, сб, вс - '
          'выходные).')
    print('6. Программа считает квадратный корень переданного ей числа')
    print('7. Программа выводит число дубликатов в списке')
    print('8. Программа возвращает объединенное строковое представление чисел в списке в качестве результата.')
    print('9. Программа которая выводит список всех четных чисел, которые идут по списку после числа 237. '
          'Список - numbers')
    print('10*. Программа, которая принимает в качестве аргумента два списка и проверяет, является ли второй '
          'список "подмассивом" первого')
    print('0. Exit')
    try:
        value = int(input("Выберите пункт: "))
        if value == 1:
            first_task(lst)
            input()
        elif value == 2:
            second_task(lst)
            input()
        elif value == 3:
            third_task(input('Enter your number'))
            input()
        elif value == 4:
            four_task(int(input('Введите год: ')), int(input('Введите месяц: ')))
            input()
        elif value == 5:
            first_date = '2019_7_2'
            second_date = '2019_7_11'
            five_task(first_date, second_date)
            input()
        elif value == 6:
            six_task(int(input('Enter your number: ')))
            input()
        elif value == 7:
            v = [1, 1, 2, 1, 2]
            seven_task(v)
            input()
        elif value == 8:
            lst_e = [25, 6, 72, 4]
            eight_task(lst_e)
            input()
        elif value == 9:
            nine_task(numbers)
            input()
        elif value == 10:
            lst_1 = [1, 2, 3, 5, 8, 13, 42, 5, 8]
            lst_2 = [5, 8, 13, 42]
            ten_task(lst_1, lst_2)
            input()
        elif value == 0:
            print("Goodbye!")
            input()
            flag = False
    except ValueError as e:
        print("Exception,", e)
        input()