import sqlite3
from parking_spot import ParkingSpotModel
from flask import jsonify


class BookedParkingModel():
    __tablename__ = 'booked_parking'

    def __init__(self, _id, date):
        self.id = _id
        self.date = date

    @classmethod
    def get_available_spots(cls, latitude, longitude, radius, booking_date):
        """
        Get available spots given the latitude, longitude, radius and date

        :param int latitude: The latitude of the place
        :param int longitude: The longitude of the place
        param int radius: The radius within which we want the parking space to be available
        """
        #This will give bookings for lat/long for all spots within the radius
        result = ParkingSpotModel.get_parking_spot_ids_by_lat_and_long(latitude, longitude, radius)
        all_parking_ids = []
        if result:
            all_parking_ids = result['parking_spots']
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()

        #These will give all paking ids that re booked for the date
        rows = cursor.execute("SELECT id FROM booked_parking WHERE date = ?",
            (booking_date, )
        )

        all_used_parking = []
        for row in rows:
            all_used_parking.append(row[0])

        available_spots = list(set(all_parking_ids) - set(all_used_parking))
        return jsonify({'spots_available': available_spots})
