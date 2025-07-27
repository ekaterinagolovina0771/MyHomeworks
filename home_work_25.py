"""
Home work 25.
Реализация классов для работы с TXT, CSV и JSON файлами в стиле ООП.
"""
import csv


class TxtFileHandler:
    '''
    Класс для работы с текстовыми файлами (TXT).
    Методы:
        - read_file(filepath: str) -> str: Читает данные из TXT файла.
        - write_file(filepath: str, *data: str) -> None: Записывает переданные данные в файл, перезаписывая его, если он существует.
        - append_file(filepath: str, *data: str) -> None: Добавляет данные в конец файла. Если файл не существует, он создается.
    Exceptions:
        - FileNotFoundError: если файл не найден
        - PermissionError: если нет прав на доступ к файлу
    '''
    def __init__(self, filepath: str) -> None:
        self.filepath = filepath
    
    def read_file(self) -> str:   
        """
        Читает данные из TXT файла.
        :return: Cтроки, прочитанные из файла.
        :raises FileNotFoundError: если файл не найден.
        :raises PermissionError: если нет прав на доступ к файлу.
        """
        try:
            with open(self.filepath, 'r', encoding='utf-8') as file:
                row_data = file.readlines()
                return [line.strip() for line in row_data]
        except FileNotFoundError as e:
            raise FileNotFoundError(f'Файл {self.filepath} не найден.') from e
        except PermissionError as e:
            raise PermissionError(f'Нет прав на доступ к файлу {self.filepath}.') from e

    def write_file(self, *data: str) -> None:
        """
        Записывает переданные данные в файл, перезаписывая его, если он существует.
        :param data: Данные для записи в файл.
        :raises PermissionError: если нет прав на запись в файл.
        """
        prepared_data = [line + '\n' for line in data]
        try:
            with open(self.filepath, 'w', encoding='utf-8') as file:
                file.writelines(prepared_data)
        except PermissionError as e:
            raise PermissionError(f'Нет прав на запись в файл {self.filepath}.') from e
        
    def append_file(self, *data: str) -> None:
        """
        Добавляет данные в конец файла. Если файл не существует, он создается.
        :param data: Данные для добавления в файл.
        :raises PermissionError: если нет прав на запись в файл.
        """
        prepared_data = [line + '\n' for line in data]
        try:
            with open(self.filepath, 'a', encoding='utf-8') as file:
                file.writelines(prepared_data)
        except PermissionError as e:
            raise PermissionError(f'Нет прав на запись в файл {self.filepath}.') from e
        
class CSVFileHandler:
    """
    Класс для работы с CSV файлами.
    Методы:
        - read_file(filepath: str) -> list[dict]: Чтение CSV файла и возврат списка словарей, соответствующих записям файла.
        - write_file(filepath: str, *data: list[dict]) -> None: Запись списка словарей в CSV файл с использованием заголовков из ключей данных.
        - append_file(filepath: str, *data: list[dict]) -> None: Дописывание новых строк в CSV файл. Если файла нет – создать его.
    Exceptions:
        - FileNotFoundError: если файл не найден
        - PermissionError: если нет прав на доступ к файлу
    """
    def __init__(self, filepath: str) -> None:
        self.filepath = filepath

    def read_file(self, delimiter: str = ";", encoding: str = "utf-8-sig"
) -> list[dict]:
        """
        Читает данные из CSV-файла.
        :param delimiter : разделитель
        :param encoding: кодировка файла
        :return: список словарей
        :raises FileNotFoundError: если файл не найден.
        :raises PermissionError: если нет прав на доступ к файлу.
        """
        try:
            with open(self.filepath, "r", encoding=encoding) as file:
                data = csv.DictReader(file, delimiter=delimiter)
                return list(data)
        except FileNotFoundError as e:
            raise FileNotFoundError(f'Файл {self.filepath} не найден.') from e
        except PermissionError as e:
            raise PermissionError(f'Нет прав на доступ к файлу {self.filepath}.') from e


    def write_file(self, *data: dict, delimiter: str = ";", encoding: str = "utf-8-sig") -> None:
        """
        Записывает данные в CSV-файл.
        :param data: данные для записи
        :param delimiter : разделитель
        :param encoding: кодировка файла
        :raises PermissionError: если нет прав на запись в файл.
        """
        try:
            with open(self.filepath, "w", encoding=encoding, newline="") as file:
                writer = csv.DictWriter(file, fieldnames=data[0].keys(), delimiter=";")
                writer.writeheader()
                writer.writerows(data)
        except PermissionError as e:
            raise PermissionError(f'Нет прав на запись в файл {self.filepath}.') from e

    def append_file(self, *new_data: dict, encoding: str = "utf-8-sig") -> None:
        """
        Добавляет данные в конец файла. Если файл не существует, он создается.
        :param data: данные для записи
        :param encoding: кодировка файла
        :raises PermissionError: если нет прав на запись в файл.
        """
        try:
            with open(self.filepath, "a", encoding=encoding, newline="") as file:
                writer = csv.DictWriter(file, fieldnames=new_data[0].keys(), delimiter=";")
                writer.writerows(new_data)
        except PermissionError as e:
            raise PermissionError(f'Нет прав на запись в файл {self.filepath}.') from e

# Пример использования

# Работа с TXT файлами
txt_handler = TxtFileHandler("example.txt")
txt_handler.write_file("Начало файла.\n")
txt_handler.append_file("Добавляем строку.\n")
content_txt = txt_handler.read_file()
print("Содержимое TXT:\n", content_txt)

# Работа с CSV файлами
csv_handler = CSVFileHandler("example.csv")
data_csv = [
    {
        'name': 'Alice',
        'age': '30'
    },
    {
        'name': 'Bob',
        'age': '25'
    }
]
new_data_csv = [
    {
        'name': 'Charlie',
        'age': '35'
    }
]
csv_handler.write_file(*data_csv)
csv_handler.append_file(*new_data_csv)
content_csv = csv_handler.read_file()
print("Содержимое CSV:\n", content_csv)