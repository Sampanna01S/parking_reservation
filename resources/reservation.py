from flask_restful import Resource, reqparse
import logging
from time import time
from models.reservation import ReservationModel


class Reservation(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('customer_name', type=str, required=True, help='customer_name cannot be blank')
    parser.add_argument('parking_id', type=str, required=True, help='parking_id cannot be blank')
    parser.add_argument('start_date', type=str, required=True, help='start_date cannot be blank')
    parser.add_argument('end_date', type=str, required=True, help='end_date cannot be blank')

    def get(self, confirmation_num):
        """
        Get the reservation for the user using the confirmation number

        :returns: reservation details
        """
        row = ReservationModel.find_by_cfno(confirmation_num)
        if row:
            d = {}
            if len(row) == 5:
                d['confirmation_num'] = row[0]
                d['parking_id'] = row[1]
                d['customer_name'] = row[2]
                d['start_date'] = row[3]
                d['end_date'] = row[4]
            return d
        else:
            return "message: confirmation number {} not found".format(confirmation_num), 404

    def put(self, confirmation_num):
        """
        Update the reservation for the user using the confirmation number

        :returns: dict containing message
        """
        row = ReservationModel.find_by_cfno(confirmation_num)
        if not row:
            return {'message': 'Confirmation number {} not found'.format(confirmation_num)}, 404

        data = Reservation.parser.parse_args()
        try:
            ReservationModel.update_reservation(confirmation_num, **data)
            return {'message': 'Updated reservation successfully'}
        except Exception as e:
            logging.exception(e)
            return {'message': 'Update reservation failed'}, 400

    def delete(self, confirmation_num):
        """
        Delete the reservation using the confirmation number

        :returns: dict containing message
        """
        row = ReservationModel.find_by_cfno(confirmation_num)
        if not row:
            return {'message': 'Confirmation {} number not found'.format(confirmation_num)}, 404

        try:
            ReservationModel.delete_reservation(confirmation_num)
            return {'message': 'Delete successful'}
        except Exception as e:
            logging.exception(e)
            return {'message': 'Delete failed'}, 400


class AddReservation(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('customer_name', type=str, required=True, help='customer_name cannot be blank')
    parser.add_argument('parking_id', type=str, required=True, help='parking_id cannot be blank')
    parser.add_argument('start_date', type=str, required=True, help='start_date cannot be blank')
    parser.add_argument('end_date', type=str, required=True, help='end_date cannot be blank')

    def post(self):
        """
        Add a new reservation for the user.

        :returns: dict containing message and confirmation number
        """
        data = AddReservation.parser.parse_args()
        cfno = int(time())
        try:
            ReservationModel.add_reservation(cfno, **data)
            return {'message': 'Added reservation successfully.', 'confirmation_number': '{}'.format(cfno)}
        except Exception as e:
            logging.exception(e)
            return {'message': 'Adding reservation failed'}, 400