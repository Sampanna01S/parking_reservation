# This is not a Model. These are scripts for create tables and inserting values
# in a table. Since the models requires data.db to be in the same place, 
# I added this file here for simplicity.

import sqlite3
from math import sin, cos, radians
import time

#sqlite has data in the file
connection = sqlite3.connect('data.db')
cursor = connection.cursor()

#USE INTEGER for autogenerating id
create_stmt = 'CREATE TABLE IF NOT EXISTS parking_spot (id INTEGER PRIMARY KEY, name text, address text, latitude float, longitude float, sin_lat, sin_lon, cos_lat, cos_lon)'
cursor.execute(create_stmt)

#parking_id is the foreign key from TABLE parking_spot(id)
create_stmt = 'CREATE TABLE IF NOT EXISTS reservation (id INTEGER PRIMARY KEY, parking_id INTEGER, customer_name TEXT, start_date TEXT, end_date TEXT)'
cursor.execute(create_stmt)

#Adding random latitude and longitude for the demo
# Since sqlite3 does not support sin, cos function, I followed the below website suggestion of creating
# sine and cosine values for latitude and longitude in the table column itself
#http://stackoverflow.com/questions/3126830/query-to-get-records-based-on-radius-in-sqlite
parking_info = []
parking_info.append({
    "latitude": 37.7811629, "longitude": -122.4052339,
    "name": "The beacon parking garage", "address": "250 King St, San Francisco, CA 94107"
})
parking_info.append({
    "latitude": 37.7811629, "longitude": -122.4052339,
    "name": "Holiday Inn civic center", "address": "50 8th St San Francisco CA 94103"
})
parking_info.append({
    "latitude": 37.7811629, "longitude": -122.4052339,
    "name": "Townsend garage", "address": "153 Townsend St San Francisco CA 94107"
})
parking_info.append({
    "latitude": 37.7811629, "longitude": -122.4052339,
    "name": "Howard Garage", "address": "75 Howard St San Francisco, CA 94105"
})
parking_info.append({
    "latitude": 37.7811629, "longitude": -122.4052339,
    "name": "EZ public parking", "address": "333 Jones St San Francisco CA 94102"
})
parking_info.append({
    "latitude": 37.7811629, "longitude": -122.4052339,
    "name": "Crocker garage", "address": "1045 California St San Francisco CA 94108"
})
parking_info.append({"latitude": 37.7811629, "longitude": -122.4052339, "name": "Ellis-O Farrell parking", "address": "123 O Farrell St San Francisco CA 94102"})

INSERT_STATEMENT = (
    "INSERT INTO parking_spot(id, name, address, latitude, longitude, sin_lat, sin_lon, cos_lat, cos_lon) "
    "VALUES({}, \"{}\", \"{}\", {}, {}, {}, {}, {}, {})"
)

for index, data in enumerate(parking_info):
    lat = data['latitude']
    lon = data['longitude']
    statement = INSERT_STATEMENT.format(
        (index + 1), data['name'], data['address'], lat, lon, sin(radians(lat)), sin(radians(lon)), cos(radians(lat)), cos(radians(lon))
    )
    cursor.execute(statement)

#parking_id is the foreign key from TABLE parking_spot(id)
#reservation_id is the foreign key from TABLE reservation(id)
create_stmt = 'CREATE TABLE IF NOT EXISTS booked_parking (id INTEGER PRIMARY KEY, parking_id INTEGER, reservation_id INT, booked_date TEXT)'
cursor.execute(create_stmt)
insert_stmt = "INSERT INTO booked_parking(parking_id, reservation_id, booked_date) VALUES(1, 1, \"{}\")".format(time.strftime("%x"))
cursor.execute(insert_stmt)
insert_stmt = "INSERT INTO booked_parking(parking_id, reservation_id, booked_date) VALUES(2, 2, \"{}\")".format(time.strftime("%x"))
cursor.execute(insert_stmt)
insert_stmt = "INSERT INTO booked_parking(parking_id, booked_date) VALUES(3, \"{}\")".format(time.strftime("%x"))
cursor.execute(insert_stmt)

connection.commit()
connection.close()