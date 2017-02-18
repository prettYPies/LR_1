num = input("Введите номер дебетовой карты (16 цифр): ")
if (len(num) != 16) or (num.isdigit()==False):
    print("Ошибка! Введите 16 цифр.")
else:
    s = num[0:4]
    s += ' **** **** '
    s+= num[12:165]
    print(s)
