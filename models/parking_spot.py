import sqlite3
from math import sin, cos, radians


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

    def get_parking_spots_by_lat_and_long(self, radius):
        """
        Get the parking spots information given the latitude, longitude and radius

        :param float radius: the radius(distance) in miles
        """

        #For this task, just ignoring latitude, longitude, radius for now
        lat = float(self.latitude)
        lon = float(self.longitude)
        radius = float(radius)

        #Used a workaround for sqlite since it does not support sin, cos functions
        #as suggested by below website for calculating distance with a radius.
        #The distance is displayed in kilometers. 
        #http://stackoverflow.com/questions/3126830/query-to-get-records-based-on-radius-in-sqlite
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        cos_allowed_distance = cos(radius / 6371)
        select_stmt = ('SELECT id, name, address, latitude, longitude, '
            '({} * sin_lat + {} * cos_lat *'
            '({} * sin_lon + {} * cos_lon)) AS "distance"'
            'FROM parking_spot where distance > {} ORDER BY "distance_acos" DESC'.format(
                sin(radians(lat)), cos(radians(lat)), sin(radians(lon)),
                cos(radians(lon)), cos_allowed_distance)
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

