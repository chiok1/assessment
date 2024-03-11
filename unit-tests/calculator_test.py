import unittest
import requests

class TestCalculatorAPI(unittest.TestCase):
    BASE_URL = "http://localhost:8080/application"

    def test_add(self):
        response = requests.post(f"{self.BASE_URL}/add", data={'num1': '5', 'num2': '3'})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['result'], 8)
        print("Test Case - Addition - PASSED")

    def test_subtract(self):
        response = requests.post(f"{self.BASE_URL}/subtract", data={'num1': '10', 'num2': '4'})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['result'], 6)
        print("Test Case - Subtraction - PASSED")

if __name__ == '__main__':
    unittest.main()