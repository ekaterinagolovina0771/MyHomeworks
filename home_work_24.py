"""
Home work 24.
"""

from pprint import pprint

# 1. Импортируйте `full_dict` из файла `Marvel.py`.
from marvel import full_dict

# 2. Реализуйте ввод от пользователя, который будет принимать цифры через пробел. Разбейте введённую строку на список и примените к каждому элементу `int`, заменяя нечисловые элементы на `None` с помощью `map`.
users_nums = input("Введите числа через пробел: ").split()

nums_list = list(map(lambda num: int(num) if num.isdigit() else None, users_nums))
pprint(f"Пользователь ввел: {nums_list}")

# 3. Перепакуйте `full_dict` в список словарей (с сохранением "id")
list_full_dict = [{"id": film_id, **film} for film_id, film in full_dict.items()]
pprint(f"Список словарей: {list_full_dict}")

# 4. Используйте `filter`, чтобы создать список, содержащий исходные `id` и другие ключи, но только для тех фильмов, `id` которых присутствуют в списке, полученном на предыдущем шаге.
new_list = list(filter(lambda film: film["id"] in nums_list, list_full_dict))
pprint(f"Отфильтрованный список: {new_list}")

# 5. Создайте множество с помощью `set comprehension`, собрав уникальные значения ключа `director` из словаря.
director_set = {
    film["director"] for film in full_dict.values() if film["director"] != "TBA"
}
pprint(f"Режиссёры: {director_set}")

# 6. С помощью `dict comprehension` создайте копию исходного словаря `full_dict`, преобразовав каждое значение `'year'` в строку. **(Опционально)**
full_dict_year_str = {film_id: {**film, "year": str(film["year"])} for film_id, film in full_dict.items()}
pprint(f"Словарь с годами в виде строк: {full_dict_year_str}")

# 7. Используйте `filter`, чтобы получить словари, содержащие только те фильмы, которые начинаются на букву `Ч`.
filtered_dict = list(filter(lambda film: isinstance(film['title'], str) and film["title"].startswith("Ч"), full_dict.values()))
pprint(f"Фильмы, начинающиеся на 'Ч': {filtered_dict}")

# 8. Отсортируйте словарь `full_dict` по одному параметру с использованием `lambda`, создавая аналогичный по структуре словарь.
# Сортировка производится по ключу 'title'.
sorted_dict_title = dict(sorted(full_dict.items(), key=lambda item: item[1].get("title") or ""))
pprint(f"Отсортированный словарь по названию: {sorted_dict_title}")

# 9. Отсортируйте словарь `full_dict` по двум параметрам с использованием `lambda`, создавая аналогичный по структуре словарь. Обязательно укажите, по каким параметрам вы производите сортировку.
sorted_dict_year_title = dict(sorted(full_dict.items(), key=lambda item: (int(item[1].get("year", 0)) if str(item[1].get("year", 0)).isdigit() else 0,item[1].get("title") or "")))
pprint(f"Отсортированный словарь по году и названию: {sorted_dict_year_title}")

# 10. Напишите однострочник, который отфильтрует и отсортирует `full_dict` с использованием `filter` и `sorted`.

sorted_2024 = sorted(filter(lambda film: (isinstance(film["year"], int) and film["year"] == 2024), full_dict.values()), key=lambda film: film["title"])
pprint(f"Фильмы 2024 года, отсортированные по названию: {sorted_2024}")
