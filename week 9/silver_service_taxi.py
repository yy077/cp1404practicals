from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Premium taxi with fanciness multiplier and flagfall charge."""

    flagfall = 4.50

    def __init__(self, name, fuel, price_per_km, fanciness):
        """Initialise SilverServiceTaxi, scaling price by fanciness."""
        super().__init__(name, fuel, price_per_km)
        self.price_per_km *= fanciness  # scale base price

    def __str__(self):
        """Return string including flagfall."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"

    def get_fare(self):
        """Return total fare including flagfall."""
        return super().get_fare() + self.flagfall