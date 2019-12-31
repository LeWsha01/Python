

def split_word_with_method(str_m):
    str_m = ''.join([symbol for symbol in str_m if symbol not in ('!', '?', ',', '.', '-')])
    for i in str_m.split():
        if len(i) < 3:
            if len(i) == 2:
                print(i + ' ', end=' ')
            elif len(i) == 1:
                print(i + '  ', end=' ')
        else:
            print(i[:3], end=' ')


def split_word_with_regular(str_re):
    \b\w{3}
srt_me = input('Enter string: ')
split_word_with_method(srt_me)
