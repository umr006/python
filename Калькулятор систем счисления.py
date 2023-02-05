def bin1(num):
    s = ''
    while num > 0:
        s += str(num % 2)
        num = num // 2
    return s[::-1]

def hex1(num):
    s = ''
    abc = '0ABCDEF'
    while num > 0:
        tmp = num % 16
        if tmp > 9:
            tmp = tmp - 9
            s += abc[tmp]
        else:
            s += str(tmp)
        num //= 16
    return s[::-1]

def oct1(num):
    s = ''
    while num > 0:
        s += str(num % 8)
        num = num // 8
    return s[::-1]

n = int(input('Введите число для преобразования'))
choice = input('В какую систему исчесления переводить: двоич., восмерич., шестнадцатерич.')
if choice == 'двоич':
    print(bin1(n))
elif choice == 'восмерич':
    print(oct1(n))
else:
    print(hex1(n))