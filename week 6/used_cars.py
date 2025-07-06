# used_cars.py

from prac_06.car import Car

def main():
    """Demo test code to show how to use car class."""
    my_car = Car("My Car", 180)
    my_car.drive(30)
    print(f"Car has fuel: {my_car.fuel}")
    print(my_car)

    limo = Car("Limousine", 100)  # Create a new Car object with 100 units of fuel
    limo.add_fuel(20)  # Add 20 more units of fuel
    print(f"Limousine has fuel: {limo.fuel}")  # Print the amount of fuel in the car
    limo.drive(115)  # Attempt to drive the car 115 km
    print(limo)  # Print the car object to test the __str__ method

main()