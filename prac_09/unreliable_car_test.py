import unittest
from unreliable_car import UnreliableCar


class TestUnreliableCar(unittest.TestCase):
    def setUp(self):
        self.car = UnreliableCar("Unreliable", 100, 50)  # Name, fuel, reliability

    def test_drive_successful(self):
        distance_driven = self.car.drive(50)
        self.assertGreater(distance_driven, 0)

    def test_drive_unsuccessful(self):
        distance_driven = self.car.drive(50)
        self.assertEqual(distance_driven, 0)


if __name__ == '__main__':
    unittest.main()
