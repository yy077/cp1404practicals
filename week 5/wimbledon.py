"""
Wimbledon
File: wimbledon.py

This program reads Wimbledon gentlemen's singles champions data from a CSV file,
processes the data, and displays processed information about the champions and their countries.

Estimated Time: 45 minutes
"""

import csv

def read_data(filename):
    """Read data from the CSV file."""
    champions = []
    countries = set()
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        reader = csv.reader(in_file)
        next(reader)  # Skip the header row
        for row in reader:
            name, country = row[1], row[2]
            champions.append((name, country))
            countries.add(country)
    return champions, countries

def count_champions(champions):
    """Count the number of wins for each champion."""
    champion_counts = {}
    for name, _ in champions:
        if name in champion_counts:
            champion_counts[name] += 1
        else:
            champion_counts[name] = 1
    return champion_counts

def list_countries(countries):
    """Return a comma-separated string of countries."""
    return ', '.join(sorted(countries))

def print_results(champion_counts, countries_str):
    """Print the results."""
    print("Wimbledon Champions:")
    for name, count in champion_counts.items():
        print(f"{name} {count}")
    print(f"These {len(countries_str.split(', '))} countries have won Wimbledon:")
    print(countries_str)

def main():
    filename = 'wimbledon.csv'
    champions, countries = read_data(filename)
    champion_counts = count_champions(champions)
    countries_str = list_countries(countries)
    print_results(champion_counts, countries_str)

if __name__ == "__main__":
    main()