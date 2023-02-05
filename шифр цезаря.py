encrypt_or_decrypt = input('encrypt or decrypt?')
language = input('ru or en?')
key = int(input('key:'))
s = input('text:').lower()
eng_alpha = 'abcdefghijklmnopqrstuvwxyz'
ru_alpha = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'

def encrypt_en(s, key):
    result = ''
    for i in s:
      if not i.isalpha():
        result += i
      elif i == ' ':
        result += ' '
      else:
        seach = eng_alpha.find(i) + 1
        if seach + key > 26:
            result += eng_alpha[seach + key - 26 - 1]
        else:
            result += eng_alpha[seach + key - 1]
    return result


def decrypt_en(s, key):
    result = ''
    for i in s:
        if not i.isalpha():
            result += i
        elif i == ' ':
            result += ' '
        else:
            seach = eng_alpha.find(i)
            result += eng_alpha[seach - key]
    return result


def encrypt_ru(s, key):
    result = ''
    for i in s:
        if not i.isalpha():
            result += i
        elif i == ' ':
            result += ' '
        else:
            seach = ru_alpha.find(i) + 1
            if seach + key > 26:
                result += ru_alpha[seach + key - 32 - 1]
            else:
                result += ru_alpha[seach + key - 1]
    return result


def decrypt_ru(s, key):
    result = ''
    for i in s:
        if not i.isalpha():
            result += i
        elif i == ' ':
            result += ' '
        else:
            seach = ru_alpha.find(i)
            result += ru_alpha[seach - key]
    return result


if language == 'en':
    if encrypt_or_decrypt == 'encrypt':
        print(encrypt_en(s, key))
    else:
        print(decrypt_en(s, key))
elif language == 'ru':
    if encrypt_or_decrypt == 'encrypt':
        print(encrypt_ru(s, key))
    else:
        print(decrypt_ru(s, key))