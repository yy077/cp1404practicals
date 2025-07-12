"""
CP1404/CP5632 Practical
File and class example - opens/reads a file, stores in objects of custom class
(contains multiple versions for demonstration: using csv and namedtuple)
"""

import csv
from collections import namedtuple

from programming_language import ProgrammingLanguage


def main():
    """Read file of programming language details, save as objects, display."""
    languages = []
    with open('languages.csv', 'r', newline='') as in_file:
        reader = csv.reader(in_file)
        next(reader)  # skip header
        for row in reader:
            # row = [Language,Typing,Reflection,Year,PointerArithmetic]
            name, typing, reflection_str, year_str, ptr_str = row
            reflection = reflection_str == "Yes"
            pointer_arithmetic = ptr_str == "Yes"
            year = int(year_str)
            language = ProgrammingLanguage(name, typing, reflection,
                                           year, pointer_arithmetic)
            languages.append(language)

    for language in languages:
        print(language)


def using_csv():
    """Language file reader version using the csv module."""
    with open('languages.csv', 'r', newline='') as in_file:
        reader = csv.reader(in_file)
        next(reader)  # skip header
        for row in reader:
            name, typing, reflection_str, year_str, ptr_str = row
            reflection = reflection_str == "Yes"
            pointer_arithmetic = ptr_str == "Yes"
            year = int(year_str)
            language = ProgrammingLanguage(name, typing, reflection,
                                           year, pointer_arithmetic)
            print(language)


def using_namedtuple():
    """Language file reader version using a named tuple."""
    Language = namedtuple('Language',
                          'name, typing, reflection, year, pointer_arithmetic')
    with open('languages.csv', 'r', newline='') as in_file:
        next(in_file).strip().split(',')
        reader = csv.reader(in_file)
        for row in reader:
            lang = Language._make(row)
            reflection = lang.reflection == "Yes"
            pointer_arithmetic = lang.pointer_arithmetic == "Yes"
            language = ProgrammingLanguage(lang.name, lang.typing,
                                           reflection, int(lang.year),
                                           pointer_arithmetic)
            print(language)


def using_csv_namedtuple():
    """Language file reader version using both csv module and named tuple."""
    Language = namedtuple('Language',
                          'name, typing, reflection, year, pointer_arithmetic')
    with open('languages.csv', 'r', newline='') as in_file:
        next(in_file)  # skip header
        for lang in map(Language._make, csv.reader(in_file)):
            reflection = lang.reflection == "Yes"
            pointer_arithmetic = lang.pointer_arithmetic == "Yes"
            language = ProgrammingLanguage(lang.name, lang.typing,
                                           reflection, int(lang.year),
                                           pointer_arithmetic)
            print(language.name, 'was released in', language.year,
                  'Pointer Arithmetic:', language.pointer_arithmetic)
            print(repr(language))


if __name__ == "__main__":
    main()