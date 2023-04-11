import sqlite3
import random

countries = ["Казахстан", "Туркия", "США", "ОАЭ", "Азербайджан", 
            "Киргизстан", "Озбекистан", "Китай"]
with open('../info/passengers_name.txt', encoding='utf-8') as f:
    name_surname = f.read().split("\n")
with open('../info/birth_dates.txt', encoding='utf-8') as f:
    dates = f.read().split("\n")

conn = sqlite3.connect('../kaspi_travel.db')
cur = conn.cursor()

vals = []
id = 1
for x, birth_date in zip(name_surname, dates):
    name, surname = x.split()
    half_IIN = birth_date.replace('/', '')[2::]
    IIN = int(half_IIN + str(random.randint(100_000, 999_999)))
    birth_date = str(birth_date)
    gender = 'Мужской' if id < 51 else 'Женский'
    citizen = random.choice(countries)
    doc_type = "Удостоверение личности" if id % 2 == 1 else "Паспорт"
    doc_num = random.randint(1_000_000_00, 9_999_999_99)
    vals += [id, name, surname, IIN, birth_date, gender, citizen, doc_type, doc_num]
    id += 1
print(*vals)
cur.executemany("INSERT INTO passengers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", vals)
conn.commit()

