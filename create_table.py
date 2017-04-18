# This is not a Model. These are scripts for create tables and inserting values
# in a table. Since the models requires data.db to be in the same place, 
# I added this file here for simplicity.

import sqlite3

#sqlite has data in the file
connection = sqlite3.connect('data.db')
cursor = connection.cursor()

#USE INTEGER for autogenerating id
create_stmt = 'CREATE TABLE IF NOT EXISTS parking_spot (id INTEGER PRIMARY KEY, name text, address text, latitude float, longitude float)'
cursor.execute(create_stmt)

#parking_id is the foreign key from TABLE parking_spot(id)
create_stmt = 'CREATE TABLE IF NOT EXISTS reservation (id INTEGER PRIMARY KEY, parking_id INTEGER, customer_name TEXT, start_date TEXT, end_date TEXT)'
cursor.execute(create_stmt)

#Adding random latitude and longitude for the demo
insert_statement = "INSERT INTO parking_spot(id, name, address, latitude, longitude) VALUES(1, 'Awesome Parking', '514 Bryant Street, San Fransisco CA', 37.784172, -122.401558)"
cursor.execute(insert_statement)
insert_statement = "INSERT INTO parking_spot(id, name, address, latitude, longitude) VALUES(2, 'Awesome Parking', '123 Bryant Street, San Fransisco CA', 38.784172, -121.401558)"
cursor.execute(insert_statement)
insert_statement = "INSERT INTO parking_spot(id, name, address, latitude, longitude) VALUES(3, 'Best Parking', '123 Brannan Street, San Fransisco CA', 39.784172, -120.401558)"
cursor.execute(insert_statement)
insert_statement = "INSERT INTO parking_spot(id, name, address, latitude, longitude) VALUES(4, 'Cheap Parking', '123 Montgomerry Street, San Fransisco CA',40.784172, -119.401558)"
cursor.execute(insert_statement)
insert_statement = "INSERT INTO parking_spot(id, name, address, latitude, longitude) VALUES(5, 'Johns Parking', '123 Harrison Street, San Fransisco CA', 41.784172, -118.401558)"
cursor.execute(insert_statement)
insert_statement = "INSERT INTO parking_spot(id, name, address, latitude, longitude) VALUES(6, 'Awesome Parking', '123 Folsom Street, San Fransisco CA', 42.784172, -117.401558)"
cursor.execute(insert_statement)
insert_statement = "INSERT INTO parking_spot(id, name, address, latitude, longitude) VALUES(7, 'Awesome Parking', '123 Howard Street, San Fransisco CA', 43.784172, -116.401558)"
cursor.execute(insert_statement)

#parking_id is the foreign key from TABLE parking_spot(id)
#reservation_id is the foreign key from TABLE reservation(id)
create_stmt = 'CREATE TABLE IF NOT EXISTS booked_parking (id INTEGER PRIMARY KEY, parking_id INTEGER, reservation_id INT, booked_date TEXT)'
cursor.execute(create_stmt)
insert_stmt = "INSERT INTO booked_parking(parking_id, reservation_id, booked_date) VALUES(1, 1, '04/17/2017')"
cursor.execute(insert_stmt)
insert_stmt = "INSERT INTO booked_parking(parking_id, reservation_id, booked_date) VALUES(2, 2, '04/17/2017')"
cursor.execute(insert_stmt)
insert_stmt = "INSERT INTO booked_parking(parking_id, booked_date) VALUES(3, '04/17/2017')"
cursor.execute(insert_stmt)

connection.commit()
connection.close()