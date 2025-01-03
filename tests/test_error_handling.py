import unittest
from app import app

class TestErrorHandling(unittest.TestCase):

    def setUp(self):
        # Set up the test client
        self.app = app.test_client()

    def test_invalid_city(self):
        # Test when the city is not provided
        response = self.app.get('/weather?city=')
        self.assertEqual(response.status_code, 400)  # Expect 400 for missing city
        data = response.get_json()
        self.assertIn('error', data)  # Ensure the response contains an error key

    def test_city_not_found(self):
        # Test when the city is not found by the geolocation API
        response = self.app.get('/weather?city=NonExistentCity123')
        self.assertEqual(response.status_code, 404)  # Expect 404 for city not found
        data = response.get_json()
        self.assertIn('error', data)  # Ensure the response contains an error key

    def test_fetch_weather_data_error(self):
        # Test for an error when fetching weather data from OpenWeatherMap
        # You might mock the API call to return an error (500 or another code)
        response = self.app.get('/weather?city=London')
        self.assertEqual(response.status_code, 200)  # Ensure this is a valid city
        data = response.get_json()
        self.assertIn('city', data)  # Ensure the data contains a city field
        self.assertIn('temperature', data)  # Ensure the data contains temperature

if __name__ == '__main__':
    unittest.main()