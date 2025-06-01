"""""
Display "Enter name:"
Get name
Display "(H)ello"
Display "(G)oodbye"
Display "(Q)uit"
Get choice
While choice != "Q"
    If choice == "H"
        Display "Hello " and name
    Else if choice == "G"
        Display "Goodbye " and name
    Else
        Display "Invalid choice"
    Display "(H)ello"
    Display "(G)oodbye"
    Display "(Q)uit"
    Get choice
Display "Finished."
"""
def main():
    name = input("Enter name: ")
    print("(H)ello\n(G)oodbye\n(Q)uit")
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "H":
            print(f"Hello {name}")
        elif choice == "G":
            print(f"Goodbye {name}")
        else:
            print("Invalid choice")
        print("(H)ello\n(G)oodbye\n(Q)uit")
        choice = input(">>> ").upper()
    print("Finished.")

main()