"""
HOME WORK 22
Функции для работы с файлами различных форматов: JSON, CSV, TXT и YAML
"""

import json
import csv

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


# Функции для работы с CSV:

def read_csv(
    file_path: str, delimiter: str = ";", encoding: str = "utf-8-sig"
) -> list[dict]:
    """
    Функция для чтения данных из CSV-файла.
    :param file_path: путь к файлу
    :param delimiter : разделитель
    :param encoding: кодировка файла
    :return: список словарей

    """
    with open(file_path, "r", encoding=encoding) as file:
        data = csv.DictReader(file, delimiter=delimiter)
        return list(data)


def write_csv(
    file_path: str, *data: dict, delimiter: str = ";", encoding: str = "utf-8-sig"
) -> None:
    """
    Функция для записи данных в CSV-файл.
    :param data: данные для записи
    :param file_path: путь к файлу
    :param delimiter : разделитель
    :param encoding: кодировка файла
    """
    with open(file_path, "w", encoding=encoding, newline="") as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys(), delimiter=";")
        writer.writeheader()
        writer.writerows(data)


def append_csv(*new_data: dict, file_path: str, encoding: str = "utf-8-sig") -> None:
    """
    Функция для добавления данных в конец CSV-файла.
    :param data: данные для записи
    :param file_path: путь к файлу
    :param encoding: кодировка файла
    """
    with open(file_path, "a", encoding=encoding, newline="") as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys(), delimiter=";")
        writer.writerows(new_data)

# Функции для работы с TXT:

def read_txt(file_path: str, encoding: str = "utf-8") -> list[str]:
    """
    Функция для чтения текстового документа.
    :param file_path: путь к файлу
    :param encoding: кодировка файла
    :return: список строк
    """
    with open(file_path, "r", encoding=encoding) as file:
        data = [line.rstrip() + '\n' for line in file.readlines()]
        return data

def write_txt(file_path: str, *data: str, encoding: str = "utf-8") -> None:
    """
    Функция для записи текстового документа.
    :param data: данные для записи
    :param file_path: путь к файлу
    :param encoding: кодировка файла
    """
    with open(file_path, "w", encoding=encoding) as file:
        ready_data = [line.rstrip() + '\n' for line in data]
        file.writelines(ready_data)

def append_txt(file_path: str, *new_data: str, encoding: str = "utf-8") -> None:
    """
    Функция для добавления данных в конец текстового документа.
    :param data: данные для записи
    :param file_path: путь к файлу
    :param encoding: кодировка файла
    """
    with open(file_path, "a", encoding=encoding) as file:
        ready_new_data = [line.rstrip() + '\n' for line in new_data]
        file.writelines(ready_new_data)