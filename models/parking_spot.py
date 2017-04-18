import sqlite3
from math import sin, cos


class ParkingSpotModel():
    __tablename__ = 'parking_spot'

    def __init__(self, latitude, longitude, radius):
        self.latitude = latitude
        self.longitude = longitude
        self.radius = radius

    @classmethod
    def get_all_parking_spots(cls):
        """
        Get all the parking spots from the table
        """
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        try:
            rows = cursor.execute("SELECT * FROM parking_spot")
            results = []
            for row in rows:
                d = {}
                d['parking_id'] = row[0]
                d['latitude'] = row[1]
                d['longitude'] = row[2]
                results.append(d)
            return {'parking_spots': results}
        except Exception as e:
            raise e
        finally:
            connection.close()
        return None

    def get_parking_spots_by_lat_and_long(self):
        """
        Get the parking spots information given the latitude, longitude and radius
        """

        #For this task, just ignoring latitude, longitude, radius for now
        lat = float(self.latitude)
        lon = float(self.longitude)
        radius = float(self.radius)

        #Used the formula from below website for calculating distance with a radius.
        #The distance is displayed in kilometers. I don't think this works
        # https://github.com/sozialhelden/wheelmap-android/wiki/Sqlite,-Distance-calculations
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        select_stmt = ('SELECT id, name, address, latitude, longitude, '
            '({} * sin_lat + {} * cos_lat *'
            '({} * sin_lon + {} * cos_lon)) AS "distance"'
            'FROM parking_spot where distance < {} ORDER BY "distance_acos" DESC'.format(
                sin(lat), cos(lat), sin(lon), cos(lon), radius
            )
        )

        rows = cursor.execute(select_stmt)
        try:
            results = []
            for row in rows:
                d = {}
                d['parking_id'] = row[0]
                d['name'] = row[1]
                d['address'] = row[2]
                d['latitude'] = row[3]
                d['longitude'] = row[4]
                results.append(d)
            return results
        except Exception as e:
            raise e
        finally:
            connection.close()
        return None

