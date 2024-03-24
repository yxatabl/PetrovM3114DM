import sqlite3 as sql
import json

with open('result.json', 'r') as file:
    data : dict = json.load(file)

db = sql.connect('db.db')
cur = db.cursor()

cur.execute(''' CREATE TABLE IF NOT EXISTS "edges" (
	"source"	INTEGER,
	"target"	INTEGER
) ''')
cur.execute(''' CREATE TABLE IF NOT EXISTS "nodes" (
	"id"	INTEGER,
	"label"	TEXT,
	PRIMARY KEY("id")
) ''')

for country in data.keys():
    for neighbour in data[country]['neighbours']:
        cur.execute(''' INSERT INTO edges VALUES (?, ?)''', (country, neighbour))
db.commit()