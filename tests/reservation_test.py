import requests
import json
import unittest

confirmation_num = 0


class ReservationTests(unittest.TestCase):
    headers = {'content_type': 'application/json'}

    def test_end_to_end(self):
        self.add_reservation()
        self.get_reservation()
        self.update_reservation()
        self.delete_reservation()
        self.get_reservation_after_delete()

    def add_reservation(self):
        data = json.dumps({
            "customer_name": "john doe",
            "parking_id": 7,
            "start_date": "04/17/2017",
            "end_date": "04/17/2017"
        })
        resp = requests.post(
            'http://localhost:5000/reservation',
            data=data,
            headers=self.headers
        )
        self.assertEqual(resp.status_code, 200)
        resp_json = resp.json()
        self.assertEqual(resp_json['message'], 'Added reservation successfully.')
        global confirmation_num
        confirmation_num = resp_json['confirmation_number']
        self.assertNotEqual(confirmation_num, 0)

    def get_reservation(self):
        expected_keys = ["confirmation_num", "customer_name", "end_date", "parking_id", "start_date"]
        resp = requests.get('http://localhost:5000/reservation/{}'.format(confirmation_num))
        self.assertEqual(resp.status_code, 200)
        resp_json = resp.json()
        self.assertEqual(set(resp_json.keys()), set(expected_keys))

    def update_reservation(self):
        data = json.dumps({
            "customer_name": "john doe",
            "parking_id": 2,
            "start_date": "04/18/2017",
            "end_date": "04/18/2017"
        })
        resp = requests.put(
            'http://localhost:5000/reservation/{}'.format(confirmation_num),
            data=data,
            headers=self.headers
        )
        self.assertEqual(resp.status_code, 200)
        resp_json = resp.json()
        self.assertEqual(resp_json['message'], 'Updated reservation successfully')

    #Need to make this to run last
    def delete_reservation(self):
        headers = {'content_type': 'application/json'}
        data = json.dumps({'name': 'Walgreens'})
        resp = requests.delete(
            'http://localhost:5000/reservation/{}'.format(confirmation_num),
            data=data,
            headers=headers
        )
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json()['message'], 'Delete successful')

    def get_reservation_after_delete(self):
        resp = requests.get('http://localhost:5000/reservation/{}'.format(confirmation_num))
        self.assertEqual(resp.status_code, 404)
        resp_json = resp.json()
        self.assertEqual(resp_json, 'message: confirmation number {} not found'.format(confirmation_num))


