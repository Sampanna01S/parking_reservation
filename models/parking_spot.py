import sqlite3


class ParkingSpotModel():
    __tablename__ = 'parking_spot'

    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    @classmethod
    def get_all_parking_spots(cls):
        """
        Get all the parking spots from the table
        """
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        rows = cursor.execute("SELECT * FROM parking_spot")
        results = []
        for row in rows:
            d = {}
            d['parking_id'] = row[0]
            d['latitude'] = row[1]
            d['longitude'] = row[2]
            results.append(d)
        return {'parking_spots': results}

    @classmethod
    def get_parking_spots_by_lat_and_long(cls, latitude, longitude, radius):
        """
        Get the parking spots information given the latitude, longitude and radius
        """
        #For this task, just ignoring latitude, longitude, radius for now
#         latitude = int(latitude)
#         longitude = int(longitude)
#         radius = int(radius)
#         start_latitude = latitude - radius
#         end_latitude = latitude + radius
#         start_longitude = longitude - radius
#         end_longitude = longitude + radius
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
#         select_stmt = (
#             "SELECT * FROM parking_spot WHERE latitude>=? and latitude>=? "
#             "and longitude>=? and longitude>=?"
#         )
        select_stmt = (
            "SELECT * FROM parking_spot"
        )
#         rows = cursor.execute(select_stmt, (start_latitude, end_latitude, start_longitude, end_longitude))
        rows = cursor.execute(select_stmt)
        results = []
        for row in rows:
            d = {}
            d['parking_id'] = row[0]
            d['latitude'] = row[1]
            d['longitude'] = row[2]
            results.append(d)
        return results

    @classmethod
    def get_parking_spot_ids_by_lat_and_long(cls, latitude, longitude, radius):
        """
        Get the parking spot id  given the latitude, longitude and radius
        """
        #For this task, just ignoring latitude, longitude, radius for now
#         latitude = int(latitude)
#         longitude = int(longitude)
#         radius = int(radius)
#         start_latitude = latitude - radius
#         end_latitude = latitude + radius
#         start_longitude = longitude - radius
#         end_longitude = longitude + radius
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
#         select_stmt = (
#             "SELECT id FROM parking_spot WHERE latitude>=? and latitude>=? "
#             "and longitude>=? and longitude>=?"
#         )
#         rows = cursor.execute(select_stmt, (start_latitude, end_latitude, start_longitude, end_longitude))
        select_stmt = (
            "SELECT id FROM parking_spot"
        )
        rows = cursor.execute(select_stmt)
        results = []
        for row in rows:
            results.append(row[0])
        return {'parking_spots': results}
