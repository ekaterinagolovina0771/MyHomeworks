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

my_image = r"C:\Users\Катя\Downloads\FullSizeRender.jpg"

# Регистрируем форматы
register_heif_opener()

source_path = r"C:\Users\Катя\Desktop\Python"  # Путь к папке с изображениями

# # # Вариант 1: Простой обход через listdir
# # files = os.listdir(source_path)  # Получаем список файлов в директории
# # for file in files:
# #     full_path = os.path.join(source_path, file)  # Формируем полный путь
# #     if os.path.isfile(full_path):  # Проверяем что это файл
# #         print(f"Найден файл: {full_path}")

# # Вариант 2: Рекурсивный обход через walk
# for root, dirs, files in os.walk(source_path):  # root - текущая директория, dirs - папки, files - файлы
#     for file in files:
#         full_path = os.path.join(root, file)  # Формируем полный путь
#         print(f"Найден файл: {full_path}")

# # Исходное изображение
# source_image = Image.open(my_image)

# # Сжатие в WEBP
# source_image.save(
#     "output.webp", 
#     format="WEBP", 
#     quality=40
# )

# # Сжатие в HEIC 
# heif_file = heif_from_pillow(source_image)
# heif_file.save(
#     "output.heic", 
#     quality=40
# )

# # Сжатие в AVIF
# source_image.save(
#     "output.avif", 
#     quality=40
# )

def compress_image(image_path: str, output_format: str = 'AVIF', qality: int = 40) -> str:
    """
    Функция для сжатия изображения.
    :param image_path: Путь к изображению.
    :param output_format: Формат выходного изображения (WEBP, HEIC, AVIF).
    :param qality: Качество сжатия (от 0 до 100).
    :return: Путь к сжатому
    """
    # Поддерживаемые форматы
    supported_formats = ['WEBP', 'HEIC', 'AVIF']
    # Проверяем, что формат поддерживается
    if output_format not in supported_formats:
        raise ValueError(f"Формат {output_format} не поддерживается. Поддерживаемые форматы: {', '.join(supported_formats)}")
    # Проверяем, что изображение существует
    if not os.path.isfile(image_path):
        raise FileNotFoundError(f"Изображение {image_path} не найдено")
    
    # Открываем изображение
    image = Image.open(image_path)
    # Сохраняем изображение в выбранном формате
    image.save(f"output.{output_format}", quality=qality)

# Тестируем функцию на примере heic
compress_image(my_image, output_format='HEIC', qality=40)