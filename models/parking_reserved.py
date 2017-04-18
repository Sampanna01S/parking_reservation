import sqlite3
from parking_spot import ParkingSpotModel


class BookedParkingModel():
    __tablename__ = 'booked_parking'

    def __init__(self, parking_id, booked_date):
        self.parking_id = parking_id
        self.booked_date = booked_date

    @classmethod
    def get_available_spots(cls, latitude, longitude, radius, booking_date):
        """
        Get available spots given the latitude, longitude, radius and date

        :param int latitude: The latitude of the place
        :param int longitude: The longitude of the place
        :param int radius: The radius within which we want the parking space to be available
        """
        #This will give bookings for lat/long for all spots within the radius
        parking_model = ParkingSpotModel(latitude, longitude, radius)
        results = parking_model.get_parking_spots_by_lat_and_long()
        all_parking_ids = [result.get('parking_id') for result in results]

        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()

        #These will give all parking ids that re booked for the date
        rows = cursor.execute("SELECT parking_id FROM booked_parking WHERE booked_date = ?",
            (booking_date, )
        )

        all_used_parking = [row[0] for row in rows]

        available_spots = list(set(all_parking_ids) - set(all_used_parking))
        spots_available_result = [result for result in results if result.get('parking_id') in available_spots]
        connection.close()
        return {'spots_available': spots_available_result}
