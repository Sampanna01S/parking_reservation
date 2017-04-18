import datetime
import requests
import unittest

confirmation_num = 0


class AvailableParkingSpotsTest(unittest.TestCase):
    headers = {'content_type': 'application/json'}

    def test_get_available_spots_for_today(self):
        """
        Tests the get available spots for today.
        If date param is not sent, the default is today
        There are 7 rows in the database, However for today's date(which is default)
        3 are filled up. So the test should return 4 spots
        """
        expected_keys = ["address", "latitude", "longitude", "parking_id", "name"]
        lat = 37.7811629
        lon = -122.4052339
        radius = 1
        resp = requests.get('http://localhost:5000/parking_spots/{}/{}/{}'.format(lat, lon, radius))
        self.assertEqual(resp.status_code, 200)
        resp_json = resp.json()
        self.assertIn('spots_available', resp_json)
        spots_available = resp_json['spots_available']
        self.assertEqual(len(spots_available), 4)
        for spots in spots_available:
            self.assertEqual(set(spots.keys()), set(expected_keys))

    def test_get_available_spots_for_tomorrow(self):
        """
        Tests the get available spots for tomorrow
        Since there is no reservation for tomorrow, the query
        should return all 7 rows
        """
        expected_keys = ["address", "latitude", "longitude", "parking_id", "name"]
        lat = 37.7811629
        lon = -122.4052339
        radius = 1
        tomorrow = datetime.date.today() + datetime.timedelta(days=1)
        date = tomorrow.strftime('%m/%d/%Y')
        params = {'date': date}
        resp = requests.get(
            'http://localhost:5000/parking_spots/{}/{}/{}'.format(lat, lon, radius),
            params=params
        )
        self.assertEqual(resp.status_code, 200)
        resp_json = resp.json()
        self.assertIn('spots_available', resp_json)
        spots_available = resp_json['spots_available']
        self.assertEqual(len(spots_available), 7)
        for spots in spots_available:
            self.assertEqual(set(spots.keys()), set(expected_keys))

