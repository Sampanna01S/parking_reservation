# README for parking reservation

This is a parking reservation application for finding available parking spots in a given radius from the specified latitude and lobgitude paramaters. 

The following Rest API's are provided. The code is implemented in python and flask using sqlite database

1. Get all parking spots.
2. Reserve an available parking spot. This will return a confirmation number
3. View existing reservation using existing confirmation number
4. Cancel existing reservation using confirmation number
5. Update existing reservation using confirmation number

## How to run the program
1. Clone the project using git
2. Run the create_table.py to create the required tables. You should notice a ``data.db`` file under the directory
3. Run the app.py file. This will run the flask application on port 5000

