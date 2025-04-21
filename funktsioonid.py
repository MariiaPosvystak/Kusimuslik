# Випадковий вибір питань	Кожен користувач отримує різні питання з файлу
# Окремі файли для успішних/невдалих	oiged.txt та valed.txt
# Електронна пошта респондентів	Генерується автоматично на основі імені
# Лист респонденту	Результат із повідомленням про успіх/невдачу
# Звіт організатору	Загальні результати та найкращий респондент
# Додавання питань через програму	Оновлення файлу kusimused_vastused.txt через інтерфейс
# Виведення результатів на екран	Список протестованих та успішних респондентів наприкінці
def laadimine_failist(Sõnastik: str):
    d = {}
    try:
        with open(Sõnastik, 'r', encoding='utf-8-sig') as file:
            for line in file:
                parts = line.strip().split(' - ')
                if len(parts) == 2:
                    key, value = line.strip().split(' - ')
                    d[key] = value
    except FileNotFoundError:
        pass
    return d