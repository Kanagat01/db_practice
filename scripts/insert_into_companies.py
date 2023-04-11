import sqlite3

conn = sqlite3.connect('../kaspi_travel.db')
cur = conn.cursor()

with open ('../info/airplanes.txt', encoding='utf-8') as f:
    txt = f.read().split('\n')
    
companies = set([x.split()[3] for x in txt])
vals = zip(range(1, 23), companies)

cur.executemany("INSERT INTO companies VALUES (?, ?)", vals)
conn.commit()
