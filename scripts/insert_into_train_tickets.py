import sqlite3
import random

conn = sqlite3.connect('../kaspi_travel.db')
cur = conn.cursor()

passengers = cur.execute("SELECT passenger_id FROM passengers").fetchall()
trips = cur.execute("SELECT where_from, where_to, trip_id FROM trips").fetchall()
classes = cur.execute("SELECT class_id FROM train_classes").fetchall()

ticket_ids = range(1, 60001)
passenger_ids = [x for x, in passengers]*600
where_from_s = [a for a, b, c, in trips]*30
where_to_s = [b for a, b, c, in trips]*30
class_ids = random.choices([x for x, in classes], k=60000)
trip_ids = [c for a, b, c, in trips]*30
train_seat_ids = random.choices(range(1, 55), k=60000)

vals = zip(ticket_ids, passenger_ids, where_from_s, where_to_s, trip_ids, class_ids, train_seat_ids)

cur.executemany("insert into train_tickets values (?, ?, ?, ?, ?, ?, ?)", vals)
conn.commit()