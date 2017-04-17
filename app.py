from flask import Flask
from flask_restful import Api
from resources.parking_spot import ParkingSpot
from resources.reservation import Reservation, AddReservation

app = Flask(__name__)
api = Api(app)
api.add_resource(Reservation, '/reservation/<int:confirmation_num>')
api.add_resource(AddReservation, '/reservation')
api.add_resource(ParkingSpot, '/parking_spots')


if __name__ == '__main__':
    app.run(port=5000, debug=True)