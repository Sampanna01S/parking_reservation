# README for parking reservation

This is a parking reservation application for finding available parking spots in a given radius from the specified latitude and lobgitude paramaters.

Assumption: The parking spot is reserved for a day basis and not time slots 

The following Rest API's are provided. The code is implemented in python and flask using sqlite database

1. Get all available parking spots.
2. Reserve an available parking spot. This will return a confirmation number
3. View existing reservation using existing confirmation number
4. Cancel existing reservation using confirmation number
5. Update existing reservation using confirmation number

## How to run the program
1. Clone the project using git
2. Create a virtualenv ``virtualenv venv``
3. Activate venv ``source venv/bin/activate``
4. Run ``pip install -r requirements.txt``
5. Run the create_table.py to create the required tables. You should notice a ``data.db`` file under the directory
6. Run the app.py file. This will run the flask application on port 5000

## Running Tests
1. Make sure the app.py is running
2. Run the reservation_test.py located under tests
   ```nosetests tests/reservation_test.py```

##Limitations
I am currently using sqlite database. However, I realized that  sqlite is not suited for geo operations. The database does not support sine, cosine fuctions. I had to use the workaround of storing the sine/cosine values for latitude and longitude in separate columns in the table. I am just not sure how well this works.

## Future Improvements
With the limited time I had, I just implemented the basic implementation. Some of the improvements that can be done in future:


1. Use a different database other than sqlite if geo operations need to be used. For example: mysql
2. Replace connection calls with sqlite with SQL Alchemy since it improves the code to fewer lines
3. Use time slots for reservation instead of a day reservation