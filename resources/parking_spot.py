from flask_restful import Resource
from models.parking_reserved import BookedParkingModel
from flask import request


class ParkingSpot(Resource):
    """
    Resource for finding available parking space within a radius
    given the longitude and latitude
    """
    def get(self):
        """
        Returns all the available spots for the date requested
        given the longitude, latitude and radius
        """
        latitude = request.args.get('latitude')
        longitude = request.args.get('longitude')
        radius = request.args.get('radius')
        booking_date = request.args.get('date')

        # TODO
        # Need to add checking to make sure latitude, longitude and radius are given

        if booking_date is None:
            booking_date = '04/17/2017'
        result = BookedParkingModel.get_available_spots(
            latitude,
            longitude,
            radius,
            booking_date
        )
        return result