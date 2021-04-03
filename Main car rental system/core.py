from tkinter import *
import home as w
import sqlite3
conn=sqlite3.connect('test.db')
print("CONNECTED!!!")


conn.execute("CREATE TABLE IF NOT EXISTS car_available\
            (car_name VARCHAR PRIMARY KEY ,\
            mileage INT,\
            model VARCHAR,\
            available INT);")

print("car_available table created ")

conn.execute("INSERT OR REPLACE INTO car_available(car_name,mileage,model,available) VALUES ('Honda',100,'A',-1)");
conn.commit()

conn.execute("INSERT OR REPLACE INTO car_available(car_name,mileage,model,available) VALUES ('Mercedes',30,'MH876',-1)");
conn.commit()
conn.execute("INSERT OR REPLACE INTO car_available(car_name,mileage,model,available) VALUES ('Mustang',22,'HY234',-1)");
conn.commit()
conn.execute("INSERT OR REPLACE INTO car_available(car_name,mileage,model,available) VALUES ('Audi',23,'HUI78',-1)");
conn.commit()
conn.execute("INSERT OR REPLACE INTO car_available(car_name,mileage,model,available) VALUES ('Sedan',21,'UPC978',-1)");
conn.commit()
conn.execute("INSERT OR REPLACE INTO car_available(car_name,mileage,model,available) VALUES ('Mini',20,'FTH865',-1)");
conn.commit()
conn.execute("INSERT OR REPLACE INTO car_available(car_name,mileage,model,available) VALUES ('Chevrolt',40,'PQR768',-1)");
conn.commit()
conn.execute("INSERT OR REPLACE INTO car_available(car_name,mileage,model,available) VALUES ('Hyundai',33,'AKM987',-1)");
conn.commit()
conn.execute("INSERT OR REPLACE INTO car_available(car_name,mileage,model,available) VALUES ('Range Rover',18,'QWT123',-1)");
conn.commit()
conn.execute("INSERT OR REPLACE INTO car_available(car_name,mileage,model,available) VALUES ('Ferrari',19,'HJE765',-1)");
conn.commit()
conn.execute("INSERT OR REPLACE INTO car_available(car_name,mileage,model,available) VALUES ('peugeot',18,'MNB176',-1)");
conn.commit()
conn.execute("INSERT OR REPLACE INTO car_available(car_name,mileage,model,available) VALUES ('Lotus',19,'MNB765',-1)");
conn.commit()

root = Tk()
root.title("Car Rental")
mb = w.Home(root)

root.mainloop()