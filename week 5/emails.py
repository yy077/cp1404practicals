"""
Emails
File: emails.py

This program stores users' emails (unique keys) and names (values) in a dictionary.
It asks the user for an email until they enter a blank one.
The program extracts a name from the email and checks if it's correct.

Estimated Time: 30 minutes
"""

import re


def extract_name_from_email(email):
    """Extract a name from the email."""
    # Remove the domain part of the email
    name_part = email.split('@')[0]

    # Replace numbers and special characters with spaces
    name_part = re.sub(r'[0-9_.+-]', ' ', name_part)

    # Split the name part into words and capitalize each word
    name = ' '.join(word.capitalize() for word in name_part.split())

    return name


def main():
    # Initialize an empty dictionary to store emails and names
    email_to_name = {}

    while True:
        # Ask the user for an email
        email = input("Email: ")

        # Exit the loop if the user enters a blank email
        if not email:
            break

        # Extract the name from the email
        name = extract_name_from_email(email)

        # Ask the user if the extracted name is correct
        response = input(f"Is your name {name}? (Y/n) ")

        # If the user does not confirm the name, ask for their name
        if response.lower() != 'y':
            name = input("Name: ")

        # Store the email and name in the dictionary
        email_to_name[email] = name

    # Print the stored emails and names
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


if __name__ == "__main__":
    main()