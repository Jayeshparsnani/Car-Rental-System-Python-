
import sqlite3
conn=sqlite3.connect('test.db')
print("CONNECTED!!!")

query = str("SELECT * FROM car_available")
r = conn.execute(query, )
conn.commit()
data = r.fetchall()
print(data)
