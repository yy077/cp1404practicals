"""
CP1404/CP5632 Practical
Testing code using assert and doctest
"""

import doctest
from prac_06.car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    return " ".join([s] * n)


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length


def sentence(phrase):
    """
    Format a phrase as a sentence: capitalized and ending with a single dot.

    >>> sentence('hello')
    'Hello.'
    >>> sentence('It is an ex parrot.')
    'It is an ex parrot.'
    >>> sentence('multiple   spaces  ')
    'Multiple   spaces.'
    """
    phrase = phrase.strip()
    if not phrase:
        return '.'
    return phrase[0].upper() + phrase[1:] + ('.' if not phrase.endswith('.') else '')


def run_tests():
    """Run the tests on the functions."""
    # assert test for repeat_string
    assert repeat_string("Python", 1) == "Python"
    assert repeat_string("hi", 2) == "hi hi"

    # assert tests for Car
    car = Car()
    assert car._odometer == 0, "Car does not set odometer correctly"
    assert car.fuel == 0, "Car does not set default fuel correctly"

    car = Car(fuel=10)
    assert car.fuel == 10, "Car does not set passed-in fuel correctly"


if __name__ == "__main__":
    run_tests()
    doctest.testmod()