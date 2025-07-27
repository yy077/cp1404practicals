"""
CP1404/CP5632 Practical
Car class
"""
from prac_09.car import Car


class Taxi(Car):
    """Specialised version of a Car that includes fare costs."""

    def __init__(self, name, fuel, price_per_km):
        """Initialise a Taxi instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.price_per_km = price_per_km
        self.current_fare_distance = 0
        self.fare_total = 0.0

    def __str__(self):
        """Return a string like a Car but with current fare distance."""
        return (f"{super().__str__()}, "
                f"{self.current_fare_distance}km on current fare, "
                f"${self.price_per_km:.2f}/km, "
                f"total fares=${self.fare_total:.2f}")

    def get_fare(self):
        """Return the price for the taxi trip."""
        return self.price_per_km * self.current_fare_distance

    def start_fare(self):
        """Begin a new fare."""
        self.current_fare_distance = 0

    def end_fare(self):
        """End the current fare, add to total, and return the cost."""
        fare = self.get_fare()
        self.fare_total += fare
        self.current_fare_distance = 0
        print(f"Trip fare: ${fare:.2f} | Total fares so far: ${self.fare_total:.2f}")
        return fare

    def drive(self, distance):
        """Drive like parent Car but calculate fare distance as well."""
        distance_driven = super().drive(distance)
        self.current_fare_distance += distance_driven
        return distance_driven