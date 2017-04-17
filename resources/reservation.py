from flask_restful import Resource, reqparse
import sqlite3
import time
from models.reservation import ReservationModel


class Reservation(Resource):
    def get(self, confirmation_num):
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
        row = ReservationModel.find_by_cfno(confirmation_num)
        if not row:
            return {'message': 'Confirmation number {} not found'.format(confirmation_num)}, 404

        parser = reqparse.RequestParser()
        parser.add_argument('customer_name', type=str, required=True, help='customer_name cannot be blank')
        parser.add_argument('parking_id', type=str, required=True, help='parking_id cannot be blank')
        parser.add_argument('start_date', type=str, required=True, help='start_date cannot be blank')
        parser.add_argument('end_date', type=str, required=True, help='end_date cannot be blank')

        data = AddReservation.parser.parse_args()
        try:
            ReservationModel.update_reservation(confirmation_num, data)
            return {'message': 'Updated reservation successfully'}
        except:
            return {'message': 'Update reservation failed'}, 400

    def delete(self, confirmation_num):
        row = ReservationModel.find_by_cfno(confirmation_num)
        if not row:
            return {'message': 'Confirmation {} number not found'.format(confirmation_num)}, 404

        try:
            ReservationModel.delete_reservation(confirmation_num)
            return {'message': 'Delete successful'}
        except:
            return {'message': 'Delete failed'}, 400


class AddReservation(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('customer_name', type=str, required=True, help='customer_name cannot be blank')
    parser.add_argument('parking_id', type=str, required=True, help='parking_id cannot be blank')
    parser.add_argument('start_date', type=str, required=True, help='start_date cannot be blank')
    parser.add_argument('end_date', type=str, required=True, help='end_date cannot be blank')

    def post(self):
        data = AddReservation.parser.parse_args()
        cfno = int(time())
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        INSERT_TABLE = (
            "INSERT INTO reservation(id, parking_id, customer_name, start_date, end_date)"
               "VALUES (?,?,?,?,?)")
        try:
            row = cursor.execute(
                INSERT_TABLE,
                (cfno, data['name'], data['address'], data['start_date'], data['end_date'],
                 data['cc_type'], data['cc_num'], data['cc_exp'], data['cc_cvv'])
            )
            for r in row:
                print 'hello: {}'.format(r)
            connection.commit()
            connection.close()
            return {'message': 'Added reservation successfully. Confirmation number: {}'.format(cfno)}
        except:
            return {'message': 'Adding reservation failed'}, 400