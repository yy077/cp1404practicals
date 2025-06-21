"""
Word Occurrences
File: word_occurrences.py

This program counts the occurrences of words in a given string.

Estimated Time: 30 minutes

Instructions:
1. Ask the user for a string.
2. Count the occurrences of each word in the string.
3. Print the counts of each word, sorted alphabetically.
4. Align the output so the numbers are in one nice column.

"""


def main():
    # Ask the user for a string
    text = input("Enter a string: ")

    # Convert the string to lowercase and split it into words
    words = text.lower().split()

    # Create a dictionary to store word counts
    word_counts = {}

    # Count the occurrences of each word
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    # Sort the words alphabetically
    sorted_words = sorted(word_counts.keys())

    # Find the longest word for formatting
    max_word_length = max(len(word) for word in sorted_words)

    # Print the word counts with aligned output
    for word in sorted_words:
        print(f"{word:{max_word_length}} : {word_counts[word]}")


if __name__ == "__main__":
    main()