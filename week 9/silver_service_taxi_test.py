from silver_service_taxi import SilverServiceTaxi

hummer = SilverServiceTaxi("Hummer", 200, 1.23, 4)
print(hummer)  # 应显示 Hummer... $4.92/km plus flagfall of $4.50

luxury = SilverServiceTaxi("Luxury Prius", 100, 1.23, 2)
luxury.start_fare()
luxury.drive(18)
fare = luxury.get_fare()
expected = 48.78
print(f"Calculated fare: ${fare:.2f}")
assert abs(fare - expected) < 0.01, f"Expected {expected}, got {fare}"
print("Fare assertion passed!")