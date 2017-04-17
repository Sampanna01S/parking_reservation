# This is not a Model. These are scripts for create tables and inserting values
# in a table. Since the models requires data.db to be in the same place, 
# I added this file here for simplicity.

import sqlite3

#sqlite has data in the file
connection = sqlite3.connect('data.db')
cursor = connection.cursor()


select_stmt = 'SELECT id FROM parking_spot'
# select_stmt = 'SELECT * FROM reservation WHERE ID=1492461428'
result = cursor.execute(select_stmt)
for row in result:
    print row

connection.commit()
connection.close()