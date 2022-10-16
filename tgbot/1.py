import requests
import json
import sqlite3
con = sqlite3.connect('db.db')
cur = con.cursor()
b = cur.execute(f"SELECT bal1 from users").fetchone()[0]
print(b)
