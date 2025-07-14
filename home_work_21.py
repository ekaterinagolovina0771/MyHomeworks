'''
Home work 21
Оптимизатор изображений
Pillow==10.0.0
pillow-heif==0.13.0
pillow-avif==1.3.1
'''
from PIL import Image
from pillow_heif import register_heif_opener, from_pillow as heif_from_pillow
import pillow_avif
import os

# my_image = r"C:\Users\Катя\Downloads\FullSizeRender.jpg"

# Регистрируем форматы
register_heif_opener()

ALLOWED_EXTENSIONS: list[str] = ['jpg', 'jpeg', 'png', 'JPG', 'JPEG']
def compress_image(file_path: str, format: str = 'avif', quality: int = 40) -> str:
    """
    Функция для сжатия изображения.
    :param image_path: Путь к изображению.
    :param output_format: Формат выходного изображения (webp, heic, avif).
    :param quality: Качество сжатия (от 0 до 100).
    :return: Путь к сжатому
    """
    # Поддерживаемые форматы
    supported_formats = ['webp', 'heic', 'avif']
    # Проверяем, что формат поддерживается
    if format not in supported_formats:
        raise ValueError(f"Формат {format} не поддерживается. Поддерживаемые форматы: {', '.join(supported_formats)}")
    # Открываем изображение
    image = Image.open(file_path)
    # Отрезаем от  file_path расширение и добавляем расширение выходного формата
    file_path = file_path.split('.')[-2]
    # Сохраняем изображение в выбранном формате
    if format in ['webp', 'avif']:
        image.save(f"{file_path}.{format}", format=format, quality=quality)
        return
    if format == 'heic':
        heif_file = heif_from_pillow(image)
        heif_file.save(f"{file_path}.heic", quality=quality)
        return
    
def get_image_paths(source_path: str, allowed_extensions: list[str]) -> list[str]:
    """
    Функция для получения путей к изображениям в директории.
    :param source_path: Путь к директории с изображениями.
    :return: Список путей к изображениям.
    """
    # Проверяем, что путь существует
    if not os.path.isdir(source_path):
        raise ValueError(f"Путь {source_path} не найден")
    # Проверяем папка или файл
    if os.path.isfile(source_path):
        return[source_path]
    # Если это папка, получаем список файлов в ней
    images =  []
    for root, dirs, files in os.walk(source_path):
        for file in files:
            full_path = os.path.join(root, file)
            if os.path.isfile(full_path):
                if file.lower().endswith(tuple(allowed_extensions)):
                    images.append(full_path)
    return images

def main() -> None:
    """
    Функция управления процессом обработки изображения и выводом прогресса
    """
    # Получаем пути к изображениям
    user_path = input("Введите путь к папке с изображениями: ").replace('"', '')
    # Собираем список изображений
    images = get_image_paths(user_path, ALLOWED_EXTENSIONS)
    # Проходимся по списку изображений
    for image in images:
        # Сжимаем изображение
        compress_image(image)
        # Выводим прогресс
        print(f"Обработано: {image}")
        # Выводим сообщение об окончании обработки
        print("Обработка завершена")

if __name__ == "__main__":
    main()


