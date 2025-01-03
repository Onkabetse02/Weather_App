import unittest
from app import app
import json

class TestIntegration(unittest.TestCase):
    
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_integration_weather_api(self):
        """ Test the full integration from frontend to backend weather API """
        city = "London"
        # Making a GET request to the /weather endpoint
        response = self.app.get(f'/weather?city={city}')
        self.assertEqual(response.status_code, 200)

        # Parsing the response as JSON
        data = response.get_json()
        self.assertIn('city', data)
        self.assertEqual(data['city'], city)
        self.assertIn('temperature', data)
        self.assertIn('description', data)

    def test_integration_invalid_city(self):
        """ Test the integration with an invalid city """
        city = "NonExistentCity123"
        # Making a GET request to the /weather endpoint
        response = self.app.get(f'/weather?city={city}')
        self.assertEqual(response.status_code, 404)

        # Check that the response contains an error
        data = response.get_json()
        self.assertIn('error', data)  # Assuming you send back an error message

    def test_home_page_integration(self):
        """ Test the home route (integration) """
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Weather App", response.data)  # Check if the page contains "Weather App"

if __name__ == '__main__':
    unittest.main()