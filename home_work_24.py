"""
Home work 24.
"""
from pprint import pprint
# 1. Импортируйте `full_dict` из файла `Marvel.py`.
from marvel import full_dict

# 2. Реализуйте ввод от пользователя, который будет принимать цифры через пробел. Разбейте введённую строку на список и примените к каждому элементу `int`, заменяя нечисловые элементы на `None` с помощью `map`.
users_nums = input('Введите числа через пробел: ').split()

nums_list = list(map(lambda num: int(num) if num.isdigit() else None, users_nums))
pprint(f"Пользователь ввел: {nums_list}")

# 3. Перепакуйте `full_dict` в список словарей (с сохранением "id")
list_full_dict = [{"id": film_id, **film} for film_id, film in full_dict.items()]
pprint(f"Список словарей: {list_full_dict}")

# 4. Используйте `filter`, чтобы создать список, содержащий исходные `id` и другие ключи, но только для тех фильмов, `id` которых присутствуют в списке, полученном на предыдущем шаге.
new_list = list(filter(lambda film: film['id'] in nums_list, list_full_dict))
pprint(f"Отфильтрованный список: {new_list}")
