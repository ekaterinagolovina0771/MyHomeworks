"""
Homework 15
Подсчет температуры в разных шкалах и остатка времени (целых часов, минут, секунд)
"""

# Задание №1: Конвертация секунд
user_seconds = int(input("Введите количество секунд: "))
hours = user_seconds // 3600
minutes = (user_seconds % 3600) // 60
seconds = user_seconds % 60
print(
    f"В указанно количестве секунд ({user_seconds}):\n Часов: {hours}\n Минут: {minutes}\n Секунд: {seconds}"
)

# Задание №2: Конвертация температуры
user_temperature = round(float(input("Введите температуру в градусах Цельсия: ")), 2)
print(
    f"Если температура в градусах Цельсия равна {user_temperature}°С, то:\n\n\t Кельвин: {user_temperature}°С + 273.15 = {round((user_temperature + 273.15), 2)} K\n\t Фаренгейт: ({user_temperature}°С * 9/5) + 32 = {round(((user_temperature * 9/5) + 32), 2)}°F\n\t Реомюр: {user_temperature}°С * 4/5 = {round((user_temperature * 4/5), 2)}°Re "
)
