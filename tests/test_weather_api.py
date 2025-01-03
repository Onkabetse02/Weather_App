import unittest
from app import app

class TestWeatherAPI(unittest.TestCase):

    def setUp(self):
        # Set up the test client
        self.app = app.test_client()

    def test_get_weather_invalid_city(self):
        # Test an invalid city that is not found
        response = self.app.get('/weather?city=NonExistentCity123')
        self.assertEqual(response.status_code, 404)  # Expect 404 for city not found
        data = response.get_json()
        self.assertIn('error', data)  # Ensure the response contains an error key

    def test_get_weather_valid_city(self):
        # Test a valid city for the API (e.g., London)
        response = self.app.get('/weather?city=London')
        self.assertEqual(response.status_code, 200)  # Expect 200 for valid city
        data = response.get_json()
        self.assertIn('city', data)  # Ensure the data contains the city name
        self.assertIn('temperature', data)  # Ensure the data contains temperature
        self.assertIn('condition', data)  # Ensure the data contains weather condition

if __name__ == '__main__':
    unittest.main()