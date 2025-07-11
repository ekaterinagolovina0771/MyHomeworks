'''
Home work 19
Работа с набором данных о фильмах (словари) с использованием словарей и циклов в Python
'''
from marvel import small_dict
from pprint import pprint

# Задача 1: Поиск фильмов по названию
user_film = input('Введите название фильма или его часть: ')
new_film_list = []
for film in small_dict.keys():
    if user_film.lower() in film:
        print(film)
        new_film_list.append(film)
print(new_film_list)

# Задача 2: Фильтрация фильмов по году выхода
new_small_list = []
new_small_dict = {}
list_dict = []
for film, year in small_dict.items():
    if year is None:
        continue
    elif year > 2024:
        print(film, year) 
        new_small_list.append(film)
        new_small_dict[film] = year
        new_dict = {
            film: year
            }
        list_dict.append(new_dict)
print(new_small_list)
print(new_small_dict)
pprint(list_dict,sort_dicts=False)
