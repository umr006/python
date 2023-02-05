import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_latter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''

sum_pass = int(input('Введите количество паролей'))
len_pass = int(input('Введите длину пароля'))
digits_on = input('Включить ли цифры? да - y, нет - n').lower()
char_low = input('включить ли быквы в нижнем регистре? да - y, нет - n').lower()
char_upp = input('Включить ли буквы в верхнем регистра? да - y, нет - n').lower()
special_char = input('Включать ли символы !#$%&*+-=?@^_ ? да - y, нет - n').lower()
exclude_char = input('Исключать ли неоднозначные символы? да - y, нет - n').lower()

if digits_on == 'y':
    chars += digits
if char_low == 'y':
    chars += lowercase_letters
if char_upp == 'y':
    chars += uppercase_latter
if special_char == 'y':
    chars += punctuation
if exclude_char == 'y':
    for c in 'il1Lo0O':
        chars = chars.replace(c, '')
#генерируем пароли
def generate_password(len_pwd, char):
    password = ''
    for _ in range(len_pwd):
        password += random.choice(char)
    return password
#задаем необходимое количтество паролей
for _ in range(sum_pass):
    print(generate_password(len_pass, chars))



