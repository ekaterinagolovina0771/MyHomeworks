"""
Home work 27.
классы для работы с различными типами файлов: JSON, TXT и CSV.
"""

import abc
import json
import csv

class AbstractFile(abc.ABC):
    """
    Абстрактный класс для работы с файлами.

    Attributes:
        file_path (str): Путь к файлу.
    """

    def __init__(self, file_path: str):
        """
        Конструктор класса.

        Args:
            file_path (str): Путь к файлу.
        """
        self.file_path = file_path

    @abc.abstractmethod
    def read(self) -> str:
        """
        Абстрактный метод для чтения данных из файла.

        Returns:
            str: Данные из файла.
        """
        pass

    @abc.abstractmethod
    def write(self, data: str) -> None:
        """
        Абстрактный метод для записи данных в файл.

        Args:
            data (str): Данные для записи в файл.
        """
        pass

    @abc.abstractmethod
    def append(self, data: str) -> None:
        """
        Абстрактный метод для добавления данных в файл.

        Args:
            data (str): Данные для добавления в файл.
        """
        pass

class JsonFile(AbstractFile):
    """
    Класс для работы с JSON-файлами.

    Attributes:
        file_path (str): Путь к файлу.
    """

    def read(self) -> dict:
        """
        Метод для чтения данных из JSON-файла.

        Returns:
            dict: Данные из JSON-файла.
        """
        with open(self.file_path, 'r') as file:
            return json.load(file)

    def write(self, data: dict) -> None:
        """
        Метод для записи данных в JSON-файл.

        Args:
            data (dict): Данные для записи в JSON-файл.
        """
        with open(self.file_path, 'w') as file:
            json.dump(data, file)

    def append(self, data: dict) -> None:
        """
        Метод для добавления данных в JSON-файл.

        Args:
            data (dict): Данные для добавления в JSON-файл.
        """
        with open(self.file_path, 'a+') as file:
            file.seek(0, 2)  # переместить указатель в конец файла
            json.dump(data, file)

class TxtFile(AbstractFile):
    """
    Класс для работы с текстовыми файлами.

    Attributes:
        file_path (str): Путь к файлу.
    """

    def read(self) -> str:
        """
        Метод для чтения данных из текстового файла.

        Returns:
            str: Данные из текстового файла.
        """
        with open(self.file_path, 'r') as file:
            return file.read()

    def write(self, data: str) -> None:
        """
        Метод для записи данных в текстовый файл.

        Args:
            data (str): Данные для записи в текстовый файл.
        """
        with open(self.file_path, 'w') as file:
            file.write(data)

    def append(self, data: str) -> None:
        """
        Метод для добавления данных в текстовый файл.

        Args:
            data (str): Данные для добавления в текстовый файл.
        """
        with open(self.file_path, 'a') as file:
            file.write(data)
