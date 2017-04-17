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
insert_statement = 'INSERT INTO parking_spot(latitude, longitude) VALUES(37.784172, -122.401558)'
cursor.execute(insert_statement)
insert_statement = 'INSERT INTO parking_spot(latitude, longitude) VALUES(38.784172, -121.401558)'
cursor.execute(insert_statement)
insert_statement = 'INSERT INTO parking_spot(latitude, longitude) VALUES(39.784172, -120.401558)'
cursor.execute(insert_statement)
insert_statement = 'INSERT INTO parking_spot(latitude, longitude) VALUES(40.784172, -119.401558)'
cursor.execute(insert_statement)
insert_statement = 'INSERT INTO parking_spot(latitude, longitude) VALUES(41.784172, -118.401558)'
cursor.execute(insert_statement)
insert_statement = 'INSERT INTO parking_spot(latitude, longitude) VALUES(42.784172, -117.401558)'
cursor.execute(insert_statement)
insert_statement = 'INSERT INTO parking_spot(latitude, longitude) VALUES(43.784172, -116.401558)'
cursor.execute(insert_statement)

create_stmt = 'CREATE TABLE IF NOT EXISTS booked_parking (id INTEGER PRIMARY KEY, booked_date TEXT)'
cursor.execute(create_stmt)

connection.commit()
connection.close()