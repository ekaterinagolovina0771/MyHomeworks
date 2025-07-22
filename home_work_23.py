"""
Home work 23.
Декоратор для валидации пароля.
Декоратор с параметрами Два декоратора на функцию
"""

import csv
from typing import Callable


def password_validator(
    min_length: int = 8,
    min_uppercase: int = 1,
    min_lowercase: int = 2,
    min_special_chars: int = 2,
) -> Callable:
    def decorator(func: Callable[[str], str]) -> Callable[[str], str]:
        """
        Декоратор для валидации паролей.
        Параметры:
        length (int): Минимальная длина пароля (по умолчанию 8).
        uppercase (int): Минимальное количество букв верхнего регистра (по умолчанию 1).
        lowercase (int): Минимальное количество букв нижнего регистра (по умолчанию 1).
        special_chars (int): Минимальное количество спец-знаков (по умолчанию 1).
        """

        def wrapper(username: str, password: str):
            errors = []
            if len(password) < min_length:
                errors.append(
                    f"Длина пароля должна быть не менее {min_length} символов."
                )
            if sum(1 for char in password if char.isupper()) < min_uppercase:
                errors.append(
                    f"Пароль должен содержать не менее {min_uppercase} букв(ы) верхнего регистра."
                )
            if sum(1 for char in password if char.islower()) < min_lowercase:
                errors.append(
                    f"Пароль должен содержать не менее {min_lowercase} букв(ы) нижнего регистра."
                )
            if sum(1 for char in password if not char.isalnum()) < min_special_chars:
                errors.append(
                    f"Пароль должен содержать не менее {min_special_chars} спец-знаков."
                )
            if errors:
                raise ValueError(
                    "Пароль не соответствует заданным критериям:\n" + "\n".join(errors)
                )
            return func(username, password)

        return wrapper

    return decorator

def username_validator() -> Callable:
    def decorator(func: Callable[[str], str]) -> Callable[[str], str]:
        """
        Декоратор для валидации имени пользователя.
        """
        def wrapper(username: str, password: str):
            if ' ' in username:
                raise ValueError(f'Имя {username} содержит пробелы.')
            return func(username, password)
        return wrapper
    return decorator

@password_validator()
@username_validator()
def register_user(username: str, password: str):
    """
    Функция для регистрации нового пользователя.

    Параметры:
        username (str): Имя пользователя.
        password (str): Пароль пользователя.

    Raises:
        ValueError: Если пароль или имя пользователя не соответствуют заданным условиям.
    """
    with open('users.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([username, password])
        print(f'Пользователь {username} успешно зарегистрирован.')