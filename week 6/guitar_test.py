# guitar_test.py

from guitar import Guitar

def test_guitar():
    gibson_l5 = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another_guitar = Guitar("Another Guitar", 2013, 1000)

    print("Gibson L-5 CES get_age() - Expected 100. Got", gibson_l5.get_age())
    print("Another Guitar get_age() - Expected 9. Got", another_guitar.get_age())
    print("Gibson L-5 CES is_vintage() - Expected True. Got", gibson_l5.is_vintage())
    print("Another Guitar is_vintage() - Expected False. Got", another_guitar.is_vintage())

test_guitar()