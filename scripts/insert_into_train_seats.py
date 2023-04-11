import sqlite3

conn = sqlite3.connect('../kaspi_travel.db')
cur = conn.cursor()

res = cur.execute("SELECT trip_id FROM trips")
trips = res.fetchall()

vals = zip(range(1, 108001), list(range(1, 55))*2000, [x for x, in trips]*54)
cur.executemany(f"INSERT INTO train_seats VALUES (?, ?, ?)", vals)
conn.commit()