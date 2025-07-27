from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    """Run the interactive taxi simulator."""
    taxis = [
        Taxi("Prius", 100),
        SilverServiceTaxi("Limo", 100, 2),
        SilverServiceTaxi("Hummer", 200, 4)
    ]

    current_taxi = None
    bill = 0.0

    print("Let's drive!")
    while True:
        print(MENU)
        choice = input(">>> ").lower()

        if choice == 'q':
            break
        elif choice == 'c':
            current_taxi = choose_taxi(taxis)
        elif choice == 'd':
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                bill += drive_taxi(current_taxi)
        else:
            print("Invalid option")
        print(f"Bill to date: ${bill:.2f}")

    print(f"Total trip cost: ${bill:.2f}")
    print("Taxis are now:")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def choose_taxi(taxis):
    """Display list and return the chosen taxi instance."""
    print("Taxis available:")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")
    try:
        index = int(input("Choose taxi: "))
        if 0 <= index < len(taxis):
            return taxis[index]
        else:
            print("Invalid taxi choice")
    except ValueError:
        print("Invalid taxi choice")
    return None


def drive_taxi(taxi):
    """Ask distance, drive, and return the trip cost."""
    try:
        distance = float(input("Drive how far? "))
        if distance < 0:
            print("Distance must be non-negative")
            return 0.0
    except ValueError:
        print("Invalid distance")
        return 0.0

    taxi.start_fare()
    taxi.drive(distance)
    cost = taxi.get_fare()
    print(f"Your {taxi.name} trip cost you ${cost:.2f}")
    return cost


if __name__ == "__main__":
    main()