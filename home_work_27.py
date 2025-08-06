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

