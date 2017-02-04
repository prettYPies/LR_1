try:
    str = input('Введите число: ')
    print('Ваше число', str)
    if str.find("-") == 1:
        raise Exception('spam', 'eggs')
except Exception as inst:
    print('Некорректный формат!')
else:
    if str.find(".") == 1:
        k = str.rsplit('.')
        print(k[0], 'руб. ', k[1], 'коп.')
    else:
        print(str, 'руб.')
