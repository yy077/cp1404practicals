def get_valid_score():
    """Get a valid score from the user (0-100 inclusive)."""
    score = float(input("Enter score (0-100): "))
    while score < 0 or score > 100:
        print("Invalid score. Please enter a score between 0 and 100.")
        score = float(input("Enter score (0-100): "))
    return score


def get_result(score):
    """Determine the result based on the score."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def show_stars(score):
    """Print a number of stars equal to the score."""
    print("*" * int(score))


def main():
    """Main function to run the score menu program."""
    print("Welcome to the Score Menu Program")
    score = get_valid_score()

    while True:
        print("\nMenu:")
        print("(G)et a valid score")
        print("(P)rint result")
        print("(S)how stars")
        print("(Q)uit")

        choice = input(">>> ").upper()

        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            result = get_result(score)
            print(f"Result: {result}")
        elif choice == "S":
            show_stars(score)
        elif choice == "Q":
            print("Farewell")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()