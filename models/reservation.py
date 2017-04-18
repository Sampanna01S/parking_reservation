import sqlite3
from parking_reserved import BookedParkingModel


class ReservationModel():
    __tablename__ = 'reservation'

    def __init__(self, parking_id, customer_name, start_date, end_date):
        self.parking_id = parking_id
        self.customer_name = customer_name
        self.start_date = start_date
        self.end_date = end_date

    @classmethod
    def find_by_cfno(cls, confirmation_num):
        print '111 {}'.format(confirmation_num)
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        try:
            result = cursor.execute("SELECT * FROM reservation WHERE ID=?", (confirmation_num,))
            row = result.fetchone()
            return row
        except Exception as e:
            raise e
        finally:
            connection.close()
        return None

    @classmethod
    def update_reservation(cls, confirmation_num, **data):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        try:
            UPDATE_TABLE = ("UPDATE reservation SET parking_id=?, customer_name=?, start_date=?, end_date=? WHERE id=?")
            cursor.execute(
                UPDATE_TABLE,
                (data['parking_id'], data['customer_name'], data['start_date'], data['end_date'], confirmation_num)
            )
            connection.commit()
        except Exception as e:
            raise e
        finally:
            connection.close()
        connection.close()

    @classmethod
    def delete_reservation(cls, confirmation_num):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        try:
            cursor.execute("DELETE FROM reservation WHERE id=?", (confirmation_num,))
            cursor.execute("DELETE FROM booked_parking WHERE reservation_id=?", (confirmation_num,))
            connection.commit()
        except Exception as e:
            raise e
        finally:
            connection.close()

    @classmethod
    def add_reservation(cls, cfno, **data):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        try:
            INSERT_TABLE = (
                "INSERT INTO reservation(id, parking_id, customer_name, start_date, end_date)"
                   "VALUES (?,?,?,?,?)"
            )
            cursor.execute(
                INSERT_TABLE,
                (cfno, data['parking_id'], data['customer_name'], data['start_date'], data['end_date'])
            )

            ## Right now just adding only the start date. Might need to have all the dates including
            ## start date and end date
            cursor.execute(
                "INSERT INTO booked_parking(parking_id, reservation_id, booked_date) VALUES (?,?,?)",
                (data['parking_id'], cfno, data['start_date'])
            )
            connection.commit()
        except Exception as e:
            raise e
        finally:
            connection.close()


