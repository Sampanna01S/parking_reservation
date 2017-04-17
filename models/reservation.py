import sqlite3


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
        result = cursor.execute("SELECT * FROM reservation WHERE ID=?", (confirmation_num,))
        row = result.fetchone()
        return row

    @classmethod
    def update_reservation(cls, confirmation_num, **data):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        UPDATE_TABLE = ("UPDATE reservation SET parking_id=?, customer_name=?, start_date=?, end_date=? WHERE id=?")
        cursor.execute(
            UPDATE_TABLE,
            (data['parking_id'], data['customer_name'], data['start_date'], data['end_date'], confirmation_num)
        )
        connection.commit()
        connection.close()

    @classmethod
    def delete_reservation(cls, confirmation_num):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        cursor.execute("DELETE FROM reservation WHERE id=?", (confirmation_num,))
        connection.commit()
        connection.close()

    @classmethod
    def add_reservation(cls, cfno, **data):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        INSERT_TABLE = (
            "INSERT INTO reservation(id, parking_id, customer_name, start_date, end_date)"
               "VALUES (?,?,?,?,?)"
        )
        cursor.execute(
            INSERT_TABLE,
            (cfno, data['parking_id'], data['customer_name'], data['start_date'], data['end_date'])
        )
        connection.commit()
        connection.close()


