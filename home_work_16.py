"""
Homework 16
Условные операторы и работа с пользовательским вводом в Python.
"""
student_name = input('Введите Ваше имя: ')
student_grade = input('Введите Вашу оценку: ')
if student_grade.isdigit():
    student_grade = int(student_grade)
    if 1 <= student_grade <= 3:
        student_level = 'Начальный'
        print(f'Имя студента: {student_name}. Уровень: {student_level}.')
    elif 4 <= student_grade <= 6:
        student_level = 'Средний'
        print(f'Имя студента: {student_name}. Уровень: {student_level}.')
    elif 7 <= student_grade <= 9:
        student_level = 'Достаточный'
        print(f'Имя студента: {student_name}. Уровень: {student_level}.')
    elif 10 <= student_grade <= 12:
        student_level = 'Высокий'
        print(f'Имя студента: {student_name}. Уровень: {student_level}.')
    else:
        print('Оценка должна быть числом от 1 до 12.')
else:
    print('Введено некорректное значение. Пожалуйста, введите число.')