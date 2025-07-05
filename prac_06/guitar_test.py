from guitar import Guitar


def test_guitar_methods():
    # Create a test guitar
    test_guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)

    # Test get_age() method
    expected_age = 100
    actual_age = test_guitar.get_age(2022)
    print(f"{test_guitar.name} get_age() - Expected {expected_age}. Got {actual_age}")

    # Test is_vintage() method
    expected_vintage = True
    actual_vintage = test_guitar.is_vintage(2022)
    print(f"{test_guitar.name} is_vintage() - Expected {expected_vintage}. Got {actual_vintage}")


# Run the test
test_guitar_methods()
