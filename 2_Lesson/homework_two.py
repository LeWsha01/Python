import calendar
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
    print(int(first_number) + int(second_number) - int(third_number) * int(four_number))


def four_task(year, month):
    c = calendar.TextCalendar(0)
    print(c.formatmonth(year, month))


def five_task():
    return None


def six_task(number):
    print('Square root of', number, '=', number ** .5)


def eight_task(lst_eght):
    str_lst = str()
    for i in lst_eght:
        str_lst += str(i)
    print(str_lst)



lst = ['Email:', 'SSN:', 'Address:', 'Home Phone:', 'Mobile Phone: ', 'DOB:', 'Date of Surgery:', 'Date of Service:',
        'Facility of Service:', 'Clinic Number:', 'Employer:', 'Work Phone: ', 'Fax: ', 'Type:', 'IPA:', 'Health Plan:',
        'ID #:', 'Claims Address:', 'Group #:', 'Claim # / PO #:', 'Phone:', 'Fax:', 'Contact', 'Adjuster Email',
        'Util Review Phone', 'Util Review Fax', 'Doctor:', 'NPI #: ', 'Date of Injury: ', 'Body Parts:',
       'Body Part Side:', 'Gender:', 'Diagnosis:', 'Diagnosis 2:', 'Procedure:']

numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 918, 237,
           412, 566, 826, 248, 866, 950, 626, 949, 687, 217,815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843,
           831, 445, 742, 717, 958,743, 527]

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
        flag = False
    elif value == 6:
        six_task(int(input('Enter your number: ')))
        input()
    elif value == 7:
        flag = False
    elif value == 8:
        lst_e = [25, 6, 72, 4]
        eight_task(lst_e)
        input()
    elif value == 9:
        flag = False
    elif value == 10:
        flag = False
    elif value == 0:
        print("Goodbye!")
        input()
        flag = False
