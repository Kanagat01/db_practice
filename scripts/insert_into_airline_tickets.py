import sqlite3
import random

conn = sqlite3.connect('../kaspi_travel.db')
cur = conn.cursor()

passengers = cur.execute("SELECT passenger_id FROM passengers").fetchall()
flights = cur.execute('''
    SELECT f.where_from, f.where_to, f.flight_id, a.airline_seat_id, a.seat_num
    FROM airline_seats a
    JOIN flights f ON f.flight_id == a.flight_id
    ORDER BY seat_num
''').fetchall()

ticket_ids = range(1, 346321) #len(flights) + 1
passenger_ids = random.sample([x for x, in passengers], k=100)*3464
where_from_s, where_to_s, flight_ids, airline_seat_ids = [], [], [], []
for x in flights:
    where_from_s.append(x[0])
    where_to_s.append(x[1])
    flight_ids.append(x[2])
    airline_seat_ids.append(x[3])
where_from_s, where_to_s, flight_ids, airline_seat_ids = where_from_s*156, where_to_s*156, flight_ids*156, airline_seat_ids*156

class_ids = []
seat_nums = [x[4] for x in flights][0:156]
for x in seat_nums:
    x = 2 if x in ['A1', 'B1', 'C1', 'A2', 'B2', 'C2', 'A3', 'B3', 'C3'] else 1
    class_ids.append(x)
class_ids = class_ids*2220

vals = zip(ticket_ids, passenger_ids, where_from_s, where_to_s, flight_ids, class_ids, airline_seat_ids)
cur.executemany("insert into airline_tickets values (?, ?, ?, ?, ?, ?, ?)", vals)
conn.commit()