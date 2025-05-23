# Переклад на українську мову
# ✅ Завдання: Анкета для респондентів + повідомлення про результати електронною поштою
# 🎯 Мета
# Створити програму, яка проводить анкетування на обрану тему, перевіряє відповіді, зберігає результати та надсилає повідомлення як респондентам, так і організатору анкети.
# 🟦 1. Питання та відповіді
#     Питання та правильні відповіді зчитуються з файлу kusimused_vastused.txt.
#     Кожен рядок містить одне питання та відповідь у форматі:
#     text
# Що таке Python?:програмна мова  
# Якого кольору сніг?:білий  
# Питання зчитуються в словник у форматі:
# python
#     kus_vas = {"питання1": "відповідь1", ...}
# 🟩 2. Проведення анкети
#     У користувача запитують ім’я.
#     Кожен користувач відповідає на N випадкових питань (N визначається в програмі, у файлі має бути більше питань).
#     Порядок питань для кожного респондента різний.
#     Під час відповідей програма звертається до користувача за ім’ям.
#     Якщо кількість правильних відповідей перевищує половину, тест вважається успішно пройденим.
# 🟨 3. Кількість респондентів
#     Програма опитує M людей (M визначається в програмі).
#     Якщо людина вже проходила тест, її не опитують повторно.
# 📁 4. Збереження у файли
# ✅ oiged.txt
#     Респонденти, які успішно пройшли тест.
#     Формат: Ім’я – X правильних відповідей.
#     Сортування за кількістю балів у порядку спадання.
# ❌ valed.txt
#     Респонденти, які відповіли правильно менш ніж на половину питань.
#     Сортування за алфавітом.
# 📋 koik.txt
#     Усі респонденти: ім’я, кількість правильних відповідей, електронна пошта.
#     Електронна пошта генерується автоматично за ім’ям у форматі: ім’я.прізвище@example.com.
# ✉️ 5. Надсилання електронних листів
# 📤 Респонденту:
# Після проходження анкети респонденту надсилається лист із результатами:
# ✅ Успішний респондент:
# text
# Відправлено: mari.tamm@example.com  
# Шановна Марі Тамм!  
# Ваша кількість правильних відповідей: 4.  
# Ви успішно пройшли тест.
# ❌ Невдалий респондент:
# text
# Відправлено: juri.saar@example.com  
# Шановний Юрі Саар!  
# Ваша кількість правильних відповідей: 2.  
# На жаль, тест не пройдено успішно.
# 🧾 Організатору:
# Наприкінці сесії організатору (на адресу tootaja@firma.ee) надсилається звіт:
# text
# Відправлено: tootaja@firma.ee  
# Шановний(а)!  
# Сьогоднішні результати анкети:  
# 1. Марі Тамм – 4 правильних – mari.tamm@example.com – ПІДХОДИТЬ  
# 2. Юрі Саар – 2 правильних – juri.saar@example.com – НЕ ПІДХОДИТЬ  
# 3. Каті Каск – 5 правильних – kati.kask@example.com – ПІДХОДИТЬ  
# Найкращий респондент: Каті Каск (5 правильних)  
# З повагою,  
# Автоматизована програма анкетування
# 🛠 6. Можливість додавати питання через програму
#     Програма має містити меню з опціями:
#         Розпочати анкету
#         Додати нове питання
#         Вийти
#     Якщо обрано «Додати нове питання»:
#         Користувач вводить:
#             Нове питання
#             Правильну відповідь
#         Дані додаються до файлу kusimused_vastused.txt у форматі:
#         text
#         нове питання:відповідь
# 🖥 7. Виведення на екран наприкінці роботи
#     Відображається список респондентів, які успішно пройшли тест, та їхні бали.
#     Показується повідомлення: «Результати надіслано на електронні адреси.»
# 📋 8. Підсумок функцій програми
# Функція	Опис
# Випадковий вибір питань	Кожен користувач отримує різні питання з файлу
# Окремі файли для успішних/невдалих	oiged.txt та valed.txt
# Електронна пошта респондентів	Генерується автоматично на основі імені
# Лист респонденту	Результат із повідомленням про успіх/невдачу
# Звіт організатору	Загальні результати та найкращий респондент
# Додавання питань через програму	Оновлення файлу kusimused_vastused.txt через інтерфейс
# Виведення результатів на екран	Список протестованих та успішних респондентів наприкінці
# Якщо потрібне додаткове пояснення чи приклад коду для реалізації, дайте знати!


import json
import random
import smtplib
import requests
from funktsioonid import *

# kus_vas = laadimine_failist('kusimused_vastused.txt')


while True:
    print("----------Menuu----------\n"
      "1. - Alusta küsimustikku\n"
    "2. - Lisa uus küsimus\n"
    "3. - Välju")
    v = input("Valige valik (1-3): ")

    if v == "1":
        questions = read_questions()
        if len(questions) < N:
            print(f"Недостатньо питань у файлі! Потрібно щонайменше {N}.")
            continue

        for _ in range(M):
            name = input("Введіть ваше ім’я: ").strip()
            if name in completed_surveys:
                print(f"{name}, ви вже проходили анкету!")
                continue
            score = conduct_survey(name, questions, N)
            if score is not None:
                email = generate_email(name)
                results[name] = (score, email)

        save_results(results)
        send_emails(results)
        display_results(results) 

    elif v == "2":
        lisa_kus()
    elif v == "3":
        break
    else:
        print("Невірний вибір, спробуйте ще раз.")
