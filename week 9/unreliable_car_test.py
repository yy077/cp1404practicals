from unreliable_car import UnreliableCar

test_car = UnreliableCar("Lemon", 100, 50)

print("Single drive attempt:")
print("Drove", test_car.drive(10), "km")
print(test_car)

print("\n100-drive statistics:")
trials = 100
success = 0
total_driven = 0

for _ in range(trials):
    test_car.start_fare()
    driven = test_car.drive(10)
    if driven > 0:
        success += 1
    total_driven += driven

print(f"Out of {trials} attempts, the car drove {success} times.")
print(f"Total distance driven: {total_driven} km")