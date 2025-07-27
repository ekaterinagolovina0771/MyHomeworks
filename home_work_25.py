"""
Home work 25.
Реализация классов для работы с TXT, CSV и JSON файлами в стиле ООП.
"""

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
        
# Пример использования

# Работа с TXT файлами
txt_handler = TxtFileHandler("example.txt")
txt_handler.write_file("Начало файла.\n")
txt_handler.append_file("Добавляем строку.\n")
content_txt = txt_handler.read_file()
print("Содержимое TXT:\n", content_txt)