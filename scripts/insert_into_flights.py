import sqlite3
import random

conn = sqlite3.connect('../kaspi_travel.db')
cur = conn.cursor()

with open ('../info/airplanes.txt', encoding='utf-8') as f:
    txt = f.read().split('\n')

with open('../info/travel_dates.txt', encoding='utf-8') as f:
    travel_dates = f.read().split('\n')[:30]

flight_ids = range(1, 3000)
company_ids = []
flight_dates = []
travel_times = []
airplanes = []
where_from_s = []
where_to_s = []

for line in txt:
    time, city, airplane, name, *travel_time = line.split()
    id, = cur.execute(f"SELECT company_id FROM companies WHERE company_name = '{name}'").fetchone()
    company_ids.append(id)
    for date in travel_dates:
        flight_dates.append(date + ' ' + time)
    travel_times.append(" ".join(travel_time))
    airplanes.append(airplane)
    where_from, where_to = random.sample(['Алматы', city], k=2)
    where_from_s.append(where_from)
    where_to_s.append(where_to)

flight_dates.sort()

vals = zip(flight_ids, company_ids*30, flight_dates, travel_times*30, airplanes*30, where_from_s*30, where_to_s*30)
cur.executemany("INSERT INTO flights VALUES (?, ?, ?, ?, ?, ?, ?)", vals)
conn.commit()