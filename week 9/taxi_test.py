from prac_09.taxi import Taxi

my_taxi = Taxi("Prius 1", 100, 1.23)

my_taxi.drive(40)

print(my_taxi)
print(f"Current fare: ${my_taxi.get_fare():.2f}")

my_taxi.start_fare()
my_taxi.drive(100)

print(my_taxi)
print(f"Current fare: ${my_taxi.get_fare():.2f}")