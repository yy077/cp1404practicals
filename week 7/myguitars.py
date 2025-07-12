from guitar import Guitar
import csv

CSV_FILE = 'guitars.csv'


def load_guitars(filename):
    """Read all guitars from CSV file and return a list of Guitar objects."""
    guitars = []
    with open(filename, newline='') as f:
        reader = csv.reader(f)
        next(reader)
        for name, year, cost, ptr in reader:
            guitars.append(Guitar(name,
                                  int(year),
                                  float(cost),
                                  ptr == "Yes"))
    return guitars


def display_guitars(guitars, title="List of Guitars"):
    """Print a list of guitars."""
    print(title)
    for g in guitars:
        print(g)


def add_new_guitars(guitars):
    """Interactively add new guitars until the user leaves the name blank."""
    print("\nAdd your own guitars (blank name to finish):")
    while True:
        name = input("Name: ").strip()
        if not name:
            break
        try:
            year = int(input("Year: "))
            cost = float(input("Cost: "))
            ptr = input("Pointer Arithmetic (Yes/No): ").strip().lower()
            guitars.append(Guitar(name, year, cost, ptr == "yes"))
        except ValueError:
            print("Invalid input, please try again.")


def save_guitars(guitars, filename):
    """Write the current list back to CSV (overwrites the file)."""
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Year", "Cost", "PointerArithmetic"])  # 写表头
        for g in guitars:
            writer.writerow([g.name, g.year, g.cost,
                             "Yes" if g.pointer_arithmetic else "No"])


def main():
    guitars = load_guitars(CSV_FILE)

    # Original order
    display_guitars(guitars, "Original order")

    # Sorted by year
    guitars.sort()
    display_guitars(guitars, "\nSorted by year (oldest first)")

    # Add user guitars
    add_new_guitars(guitars)

    # Save back
    save_guitars(guitars, CSV_FILE)
    print("\nUpdated file written to", CSV_FILE)

    # Reload & verify
    reloaded = load_guitars(CSV_FILE)
    display_guitars(reloaded, "\nRe-loaded guitars from file")


if __name__ == '__main__':
    main()