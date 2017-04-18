import sqlite3


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
        latitude = float(self.latitude)
        longitude = float(self.longitude)
        radius = float(self.radius)
        start_latitude = latitude - radius
        end_latitude = latitude + radius
        start_longitude = longitude - radius
        end_longitude = longitude + radius
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        select_stmt = (
            "SELECT id, (3959 * acos(cos(radians(37)) * cos(radians(lat)) * cos(radians(lng) - radians(-122)) + sin(radians(37)) * sin(radians(lat )))) AS distance"
            " FROM parking_spot HAVING distance < 25 ORDER BY distance LIMIT 0, 20"
        )
#         select_stmt = (
#             "SELECT * FROM parking_spot"
#         )
        rows = cursor.execute(select_stmt, (start_latitude, end_latitude, start_longitude, end_longitude))
        try:
#             rows = cursor.execute(select_stmt)
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

    def get_parking_spot_ids_by_lat_and_long(self):
        """
        Get the parking spot id  given the latitude, longitude and radius
        """
        #For this task, just ignoring latitude, longitude, radius for now
#         latitude = int(self.latitude)
#         longitude = int(self.longitude)
#         radius = int(self.radius)
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
        try:
            select_stmt = (
                "SELECT id FROM parking_spot"
            )
            rows = cursor.execute(select_stmt)
            results = []
            for row in rows:
                results.append(row[0])
            return {'parking_spots': results}
        except Exception as e:
            raise e
        finally:
            connection.close()
        return None
