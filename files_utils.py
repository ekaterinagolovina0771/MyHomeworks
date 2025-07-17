"""
HOME WORK 22
Функции для работы с файлами различных форматов: JSON, CSV, TXT и YAML
"""

import json

# Функции для работы с JSON:

def read_json(file_path: str, encoding: str = "utf-8"):
    """
    Функция для чтения данных из JSON-файла.
    :param file_path: путь к файлу
    :param encoding: кодировка файла
    # :return: список словарей
    """
    with open(file_path, "r", encoding=encoding) as file:
        data = json.load(file)
        return data


def write_json(file_path: str, *data: dict, encoding: str = "utf-8") -> None:
    """
    Функция для записи данных в JSON-файл.
    :param file_path: путь к файлу
    :param data: данные для записи
    :param encoding: кодировка файла
    """
    with open(file_path, "w", encoding=encoding) as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def append_json(file_path: str, *new_data: dict, encoding: str = "utf-8") -> None:
    """
    Функция для добавления данных в JSON-файл.
    :param file_path: путь к файлу
    :param data: данные для записи
    :param encoding: кодировка файла
    """
    data_json = read_json(file_path)
    data_json.extend(new_data)
    write_json(file_path, *data_json)
