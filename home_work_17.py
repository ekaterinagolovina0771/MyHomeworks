"""
Homework 17
Шифр Цезаря в лексикографическом порядке.
"""

user_text = input('Введите текст на русском млм английском языке: ')
shift = input('Введите число, которое будет использоваться как сдвиг для шифрования: ')
newletter = []
if not shift.isdigit():
    print('Вы ввели не число!') 
else:
    for letter in user_text:
        if letter == ' ':
            newletter.append(' ')
        else:
            letter = chr(ord(letter) + int(shift))
            newletter.append(letter) 
    print(f'Результат: {''.join(newletter)}')
    