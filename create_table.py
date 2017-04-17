# This is not a Model. These are scripts for create tables and inserting values
# in a table. Since the models requires data.db to be in the same place, 
# I added this file here for simplicity.

import sqlite3

#sqlite has data in the file
connection = sqlite3.connect('data.db')
cursor = connection.cursor()

#USE INTEGER for autogenerating id
create_stmt = 'CREATE TABLE IF NOT EXISTS parking_spot (id INTEGER PRIMARY KEY, latitude INTEGER, longitude INTEGER)'
cursor.execute(create_stmt)

create_stmt = 'CREATE TABLE IF NOT EXISTS reservation (id INTEGER PRIMARY KEY, parking_id INTEGER, customer_name TEXT, start_date TEXT, end_date TEXT)'
cursor.execute(create_stmt)

#Adding random latitude and longitude for the demo
insert_statement = 'INSERT INTO parking_spot(id, latitude, longitude) VALUES(1, 37.784172, -122.401558)'
cursor.execute(insert_statement)
insert_statement = 'INSERT INTO parking_spot(id, latitude, longitude) VALUES(2, 38.784172, -121.401558)'
cursor.execute(insert_statement)
insert_statement = 'INSERT INTO parking_spot(id, latitude, longitude) VALUES(3, 39.784172, -120.401558)'
cursor.execute(insert_statement)
insert_statement = 'INSERT INTO parking_spot(id, latitude, longitude) VALUES(4, 40.784172, -119.401558)'
cursor.execute(insert_statement)
insert_statement = 'INSERT INTO parking_spot(id, latitude, longitude) VALUES(5, 41.784172, -118.401558)'
cursor.execute(insert_statement)
insert_statement = 'INSERT INTO parking_spot(id, latitude, longitude) VALUES(6, 42.784172, -117.401558)'
cursor.execute(insert_statement)
insert_statement = 'INSERT INTO parking_spot(id, latitude, longitude) VALUES(7, 43.784172, -116.401558)'
cursor.execute(insert_statement)

create_stmt = 'CREATE TABLE IF NOT EXISTS booked_parking (id INTEGER PRIMARY KEY, parking_id INTEGER, booked_date TEXT)'
cursor.execute(create_stmt)
insert_stmt = "INSERT INTO booked_parking(parking_id, booked_date) VALUES(1, '04/17/2017')"
cursor.execute(insert_stmt)
insert_stmt = "INSERT INTO booked_parking(parking_id, booked_date) VALUES(2, '04/17/2017')"
cursor.execute(insert_stmt)
insert_stmt = "INSERT INTO booked_parking(parking_id, booked_date) VALUES(3, '04/17/2017')"
cursor.execute(insert_stmt)

connection.commit()
connection.close()