import sqlite3
import random

conn = sqlite3.connect('../kaspi_travel.db')
cur = conn.cursor()

res = cur.execute("SELECT flight_id FROM flights")
flights = res.fetchall()
chairs = ['A1', 'B1', 'C1', 'A2', 'B2', 'C2', 'A3', 'B3', 'C3']
chairs += [x + str(y) for y in range(10, 41) for x in ['A', 'B', 'C', 'D', 'E', 'F']]

airline_seat_ids = range(1, 346321)
seat_nums = random.sample(chairs, k=156)*2220
flight_ids = sorted([x for x, in flights]*156)
vals = zip(airline_seat_ids, seat_nums, flight_ids)
cur.executemany(f"INSERT INTO airline_seats VALUES (?, ?, ?)", vals)
conn.commit()