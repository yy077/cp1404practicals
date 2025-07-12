# guitar.py
class Guitar:
    def __init__(self, name="", year=0, cost=0, pointer_arithmetic=False):
        self.name = name
        self.year = year
        self.cost = cost
        self.pointer_arithmetic = pointer_arithmetic

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def __repr__(self):
        return self.__str__()

    def __lt__(self, other):
        """For sorting by year ascending."""
        return self.year < other.year

    def get_age(self):
        return 2025 - self.year

    def is_vintage(self):
        return self.get_age() >= 50