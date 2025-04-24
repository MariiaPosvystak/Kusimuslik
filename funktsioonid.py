# Випадковий вибір питань	Кожен користувач отримує різні питання з файлу
# Окремі файли для успішних/невдалих	oiged.txt та valed.txt
# Електронна пошта респондентів	Генерується автоматично на основі імені
# Лист респонденту	Результат із повідомленням про успіх/невдачу
# Звіт організатору	Загальні результати та найкращий респондент
# Додавання питань через програму	Оновлення файлу kusimused_vastused.txt через інтерфейс
# Виведення результатів на екран	Список протестованих та успішних респондентів наприкінці
import random
import smtplib
import ssl
from email.message import EmailMessage
from tkinter import filedialog

#Добавление вопроса
def lisa_kus():
    kus=input("Sisesta uus küsimus: ")
    vas =input("Sisestage õige vastus: ")
    with open ('kusimused_vastused.txt', 'a', encoding='utf-8-sig') as f:
        f.write(f"\n{kus}:{vas}\n")
    print("Küsimus lisatud")

#-------------------------------------------------------------------------------------

#Введение имени
nimi=input("Sisesta oma nimi: ")
pnimi=input("Sisesta oma perekonnanimi: ")
r=f"{nimi} {pnimi}"
email=f"{nimi}.{pnimi}@gmail.com"

#Количество вопросов на которые хотят ответить (Вопросы задаються с помощъю рандома)
N=input("На сколько вопросов вы хотите ответить: ")
random

#
M=input("Сколько человек опросить: ")















#Письмо
def saada_kiri():
    kellele=input("Kellele saata: ")
    teema=input("Teema: ")
    sisu=input("Sisu: ")
    smtp_server="smtp.gmail.com"
    smtp_port=587
    kellelt="posvystakmariia@gmail.com"
    salasõna=input("Salasõna: ") #"fgtg wert wert sdfg"
    msg=EmailMessage()
    msg['Subject']=teema
    msg['From']=kellelt
    msg['To']=kellele
    teema="""
    <!DOCTYPE html>
    <head>
    </head>
        <body>
            <h1>Küsimustik</h1>
        </body>
    </html>
    """
    sisu="""
    <!DOCTYPE html>
    <head>
    </head>
        <body>
            <p>Tere</p>
            <a href="https://thk.edupage.org/timetable/">Minu tunniplaan</a>
        </body>
    </html>
    """
    msg.set_content(sisu, subtype='html')
    fail=filedialog.askopenfilename(title="Vali fail", filetypes=[("All files","*.*")])
    with open(fail,'rb') as f:
        faili_sisu=f.read()
        faili_nimi=fail.split("/")[-1]
        msg.add_attachment(faili_sisu,maintype="application",subtype="octet-stream",filename="")
    try:
        with smtplib.SMTP(smtp_server,smtp_port) as server:
            server.starttls(context=ssl.create_default_context())
            server.login(kellelt,salasõna)
            server.send_message(msg)
        print("kiri saadetud")
    except Exception as e:
        print ("Viga:", e)











# def ava_faili():
#     kus_vas = {}
#     try:
#         with open('kusimused_vastused.txt', 'r', encoding='utf-8-sig') as f:
#             for line in f:
#                 if 'i' in line:
#                     kus, vas = line.strip().split(':',1)
#                     kus_vas[kus]
#     except FileNotFoundError:
#         print("Faili 'kusimused_vastused.txt' ei ole leitud ")
#     return kus_vas





# def küsimustik(nimi: str, kus: str, N:int):
#     try:
#         with open('oiged.txt', 'r', encoding='utf-8-sig') as f:
#             oiged = f.read().splitlines() 
#             if nimi in oiged:
#                 print(f"{nimi} on juba vastanud!")
#                 return 0 
#     except FileNotFoundError:
#         with open('oiged.txt', 'w', encoding='utf-8-sig') as f:
#             pass  
#         oiged = []
#     try:
#         with open('kusimused_vastused.txt', 'r', encoding='utf-8') as f:
#             lines = f.read().splitlines()  # Читаем строки
#             if not lines:
#                 print(f"Fail {kusimused_vastused} on tühi!")
#                 return 0
#             questions = {}
#             for line in lines:
#                 if ':' in line:
#                     question, answer = line.split(':', 1)  # Разделяем по первому двоеточию
#                     questions[question.strip()] = answer.strip()
#                 else:
#                     continue  # Пропускаем некорректные строки
#     except FileNotFoundError:
#         lisa_kus()
#     r_kus = random.sample(list(questions.keys()), N)
#     õ_vas = 0  # Счетчик правильных ответов

#     # Задаем вопросы и проверяем ответы
#     for k in r_kus:
#         print(f"{nimi}, küsimus: {k}")
#         i_kus = input("Sinu vastus: ").lower()  # Получаем ответ пользователя
#         if i_kus == questions[k].lower():  # Сравниваем с правильным ответом
#             õ_vas += 1
#             print("Õige!")  # Сообщаем, что ответ правильный
#         else:
#             print(f"Vale! Õige vastus: {questions[k]}")

#     # Добавляем имя в файл oiged.txt
#     with open('oiged.txt', 'a', encoding='utf-8') as f:
#         f.write(nimi + '\n')







# # Генерація email
# def generate_email(name):
#     return f"{name.lower().replace(' ', '.')}@example.com"

# # Збереження результатів у файли
# def save_results(results):
#     # oiged.txt (успішні, сортування за балами)
#     successful = [(name, score, email) for name, (score, email) in results.items() if score > N // 2]
#     successful.sort(key=lambda x: x[1], reverse=True)
#     with open('oiged.txt', 'w', encoding='utf-8') as f:
#         for name, score, _ in successful:
#             f.write(f"{name} – {score} правильних\n")

#     # valed.txt (невдалі, сортування за алфавітом)
#     failed = [(name, score) for name, (score, _) in results.items() if score <= N // 2]
#     failed.sort(key=lambda x: x[0])
#     with open('valed.txt', 'w', encoding='utf-8') as f:
#         for name, score in failed:
#             f.write(f"{name} – {score} правильних\n")

#     # koik.txt (усі респонденти)
#     with open('koik.txt', 'w', encoding='utf-8') as f:
#         for name, (score, email) in results.items():
#             f.write(f"{name}, {score} правильних, {email}\n")

# # Надсилання листів
# def send_emails(results):
#     smtp_server = "smtp.example.com"
#     smtp_port = 587
#     sender_email = "no-reply@example.com"
#     password = "your_password"

#     try:
#         server = smtplib.SMTP(smtp_server, smtp_port)
#         server.starttls()
#         server.login(sender_email, password)

#         # Лист респондентам
#         for name, (score, email) in results.items():
#             msg = MIMEText(
#                 f"Шановна(ий) {name}!\n\n"
#                 f"Ваша кількість правильних відповідей: {score}.\n"
#                 f"{'Ви успішно пройшли тест.' if score > N // 2 else 'На жаль, тест не пройдено успішно.'}"
#             )
#             msg['Subject'] = "Результати анкети"
#             msg['From'] = sender_email
#             msg['To'] = email
#             server.sendmail(sender_email, email, msg.as_string())

#         # Звіт організатору
#         report = "Шановний(а)!\n\nСьогоднішні результати анкети:\n"
#         for i, (name, (score, email)) in enumerate(results.items(), 1):
#             status = "ПІДХОДИТЬ" if score > N // 2 else "НЕ ПІДХОДИТЬ"
#             report += f"{i}. {name} – {score} правильних – {email} – {status}\n"
#         best_respondent = max(results.items(), key=lambda x: x[1][0], default=("Немає", (0, "")))
#         report += f"\nНайкращий респондент: {best_respondent[0]} ({best_respondent[1][0]} правильних)\n"
#         report += "З повагою,\nАвтоматизована програма анкетування"

#         msg = MIMEText(report)
#         msg['Subject'] = "Звіт анкети"
#         msg['From'] = sender_email
#         msg['To'] = "tootaja@firma.ee"
#         server.sendmail(sender_email, "tootaja@firma.ee", msg.as_string())

#         server.quit()
#         print("Результати надіслано на електронні адреси.")
#     except Exception as e:
#         print(f"Помилка при надсиланні листів: {e}")

# # Виведення результатів
# def display_results(results):
#     print("\nУспішно пройшли тест:")
#     for name, (score, _) in results.items():
#         if score > N // 2:
#             print(f"{name}: {score} правильних")





# def ava_faili():
#     kus_vas = {}
#     try:
#         with open(kusimused_vastused.txt, 'r', encoding='utf-8-sig') as f:
#             for line in f:
#                 if 'i' in line:
#                     kus, vas = line.strip().split(':',1)
#                     kus_vas[kus]
#     except FileNotFoundError:
#         print("Faili 'kusimused_vastused.txt' ei ole leitud ")
#     return kus_vas


# def lisa_kus():
#     kus=input("Sisesta uus küsimus: ")
#     vas =input("Sisestage õige vastus")
#     with open ('Küsimustik.txt', 'a', encoding='utf-8-sig') as f:
#         f.write(f"{kus}:{vas}\n")
#     print("Küsimus lisatud")


# def küsimustik(nimi: str, kus: str, N:int):
#     if nimi in oiged:
#         print(f"{nimi} teid on juba testitud!")
#         return None
#     r_kus=random.sanmple(list(kus.key()), N)
#     õ_vas=0
#     for k in r_kus:
#         print(f"{name}, küsimus: {k}")
#         i_v == kus[k].lower():
#             õ_vas += 1
#     oiged.add(nimi)
#     return õ_vas




# import smtplib
# import ssl
# from email.message import EmailMessage
# from tkinter import filedialog
# def saada_kiri():
#     kellele=input("Kellele saata: ")
#     teema=input("Teema: ")
#     sisu=input("Sisu: ")
#     smtp_server="smtp.gmail.com"
#     smtp_port=587
#     kellelt="posvystakmariia@gmail.com"
#     salasõna=input("Salasõna: ") #"fgtg wert wert sdfg"
#     msg=EmailMessage()
#     msg['Subject']=teema
#     msg['From']=kellelt
#     msg['To']=kellele
#     sisu="""
#     <!DOCTYPE html>
#     <head>
#     </head>
#         <body>
#             <h1>TARpv24 tunniplaan</h1>
#             <p>Tere</p>
#             <a href="https://thk.edupage.org/timetable/">Minu tunniplaan</a>
#         </body>
#     </html>
#     """
#     msg.set_content(sisu, subtype='html')
#     fail=filedialog.askopenfilename(title="Vali fail", filetypes=[("All files","*.*")])
#     with open(fail,'rb') as f:
#         faili_sisu=f.read()
#         faili_nimi=fail.split("/")[-1]
#         msg.add_attachment(faili_sisu,maintype="application",subtype="octet-stream",filename="")
#     try:
#         with smtplib.SMTP(smtp_server,smtp_port) as server:
#             server.starttls(context=ssl.create_default_context())
#             server.login(kellelt,salasõna)
#             server.send_message(msg)
#         print("kiri saadetud")
#     except Exception as e:
#         print ("Viga:", e)