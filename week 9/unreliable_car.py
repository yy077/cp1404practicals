"""
CP1404/CP5632 Practical
UnreliableCar class — inherits from Car
"""

import random
from prac_09.car import Car


class UnreliableCar(Car):
    """A Car that might not always drive due to reliability issues."""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar, extending Car."""
        super().__init__(name, fuel)
        self.reliability = reliability  # 0–100

    def drive(self, distance):
        """
        Drive only if a random number (0–100) is less than reliability.
        Always return the distance actually driven (0 if failed).
        """
        if random.randint(0, 100) < self.reliability:
            return super().drive(distance)
        else:
            return 0