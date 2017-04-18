from flask_restful import Resource
from models.parking_reserved import BookedParkingModel
from flask import request
import time


class ParkingSpot(Resource):
    """
    Resource for finding available parking space within a radius
    given the longitude and latitude
    """
    def get(self, latitude, longitude, radius):
        """
        Returns all the available spots for the date requested
        given the longitude, latitude and radius
        """
        booking_date = request.args.get('date')
        # If date was not provided, use today's date
        if booking_date is None:
            booking_date = time.strftime("%x")

        result = BookedParkingModel.get_available_spots(
            latitude,
            longitude,
            radius,
            booking_date
        )
        return result
