import unittest
from silver_service_taxi import SilverServiceTaxi


class TestSilverServiceTaxi(unittest.TestCase):
    def setUp(self):
        self.taxi = SilverServiceTaxi("Hummer", 200, 2)

    def test_fare_calculation(self):
        # Test fare calculation for an 18 km trip in a SilverServiceTaxi with fanciness of 2
        expected_fare = 18 * 2 * 2 + 4.50
        self.assertEqual(self.taxi.get_fare(), expected_fare)


if __name__ == '__main__':
    unittest.main()
