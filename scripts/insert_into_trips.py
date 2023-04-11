import sqlite3

conn = sqlite3.connect('../kaspi_travel.db')
cur = conn.cursor()

with open('../info/trains.txt', encoding='utf-8') as f:
    trains = f.read().replace('—', '').split('\n')

with open('../info/travel_dates.txt', encoding='utf-8') as f:
    train_travel_dates = f.read().split('\n')

trip_ids = range(1, 2001)
trip_dates = sorted([x for x in train_travel_dates]*len(trains))
trains, where_from_s, where_to_s, travel_time_s = [], [], [], []

vals = zip(trip_ids, trip_dates, trains, where_from_s, where_to_s, travel_time_s)
for x in trains:
    x = x.split()
    train, where_from, where_to, travel_time = x[0], x[1], x[2], " ".join(x[3::])
    trains.append(train)
    where_from_s.append(where_from)
    where_to_s.append(where_to)
    travel_time_s.append(travel_time)

cur.executemany("INSERT INTO trips VALUES (?, ?, ?, ?, ?, ?)", vals)
conn.commit()