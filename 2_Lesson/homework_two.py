

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


lst = ['Email:', 'SSN:', 'Address:', 'Home Phone:', 'Mobile Phone: ', 'DOB:', 'Date of Surgery:', 'Date of Service:',
        'Facility of Service:', 'Clinic Number:', 'Employer:', 'Work Phone: ', 'Fax: ', 'Type:', 'IPA:', 'Health Plan:',
        'ID #:', 'Claims Address:', 'Group #:', 'Claim # / PO #:', 'Phone:', 'Fax:', 'Contact', 'Adjuster Email',
        'Util Review Phone', 'Util Review Fax', 'Doctor:', 'NPI #: ', 'Date of Injury: ', 'Body Parts:',
       'Body Part Side:', 'Gender:', 'Diagnosis:', 'Diagnosis 2:', 'Procedure:']


first_task(lst)
second_task(lst)
third_task(input('Enter your number'))