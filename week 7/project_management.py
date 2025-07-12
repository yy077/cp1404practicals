"""
Project Management Program
Author: <your name>
Time estimate: 4.5 hours
"""

import csv
import datetime
import sys
from project import Project

DEFAULT_FILE = "projects.txt"
MENU = """- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit"""


def load_projects(filename):
    """Load projects from *filename*; return list[Project]."""
    projects = []
    with open(filename, newline='') as f:
        reader = csv.reader(f, delimiter='\t')
        next(reader)                            # skip header
        for row in reader:
            name, date_str, priority, cost, percent = row
            start_date = datetime.datetime.strptime(date_str, "%d/%m/%Y").date()
            projects.append(Project(name, start_date, priority, cost, percent))
    return projects


def save_projects(projects, filename):
    """Save projects to *filename* (TAB-delimited)."""
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f, delimiter='\t')
        writer.writerow(["Name", "Start Date", "Priority",
                         "Cost Estimate", "Completion Percentage"])
        for p in projects:
            writer.writerow([p.name, p.start_date.strftime("%d/%m/%Y"),
                             p.priority, p.cost_estimate, p.completion_percentage])


def display_projects(projects):
    """Print incomplete and completed projects, each sorted by priority."""
    incomplete = [p for p in projects if not p.is_completed()]
    completed = [p for p in projects if p.is_completed()]

    print("Incomplete projects:")
    for p in sorted(incomplete):
        print(" ", p)

    print("Completed projects:")
    for p in sorted(completed):
        print(" ", p)


def filter_projects_by_date(projects):
    """Show projects starting after user-supplied date."""
    date_str = input("Show projects that start after date (dd/mm/yyyy): ")
    try:
        filter_date = datetime.datetime.strptime(date_str, "%d/%m/%Y").date()
    except ValueError:
        print("Invalid date format.")
        return

    filtered = [p for p in projects if p.start_date > filter_date]
    filtered.sort(key=lambda x: x.start_date)
    for p in filtered:
        print(" ", p)


def add_new_project(projects):
    """Prompt user for new project details and append to list."""
    print("Let's add a new project")
    name = input("Name: ").strip()
    date_str = input("Start date (dd/mm/yyyy): ").strip()
    try:
        start_date = datetime.datetime.strptime(date_str, "%d/%m/%Y").date()
    except ValueError:
        print("Invalid date format.")
        return
    try:
        priority = int(input("Priority: "))
        cost = float(input("Cost estimate: "))
        percent = int(input("Percent complete: "))
    except ValueError:
        print("Invalid number.")
        return
    projects.append(Project(name, start_date, priority, cost, percent))
    print("Project added.")


def update_project(projects):
    """Allow user to modify completion % and/or priority of a chosen project."""
    for idx, p in enumerate(projects):
        print(f"{idx} {p}")

    try:
        choice = int(input("Project choice: "))
        project = projects[choice]
    except (ValueError, IndexError):
        print("Invalid choice.")
        return

    print(project)
    new_percent = input("New Percentage: ").strip()
    new_priority = input("New Priority: ").strip()

    if new_percent:
        project.completion_percentage = int(new_percent)
    if new_priority:
        project.priority = int(new_priority)
    print("Project updated.")


def main():
    print("Welcome to Pythonic Project Management")
    projects = load_projects(DEFAULT_FILE)
    print(f"Loaded {len(projects)} projects from {DEFAULT_FILE}")

    while True:
        print(MENU)
        choice = input(">>> ").lower()

        if choice == 'l':
            filename = input("Filename to load: ")
            projects = load_projects(filename)
        elif choice == 's':
            filename = input("Filename to save: ")
            save_projects(projects, filename)
        elif choice == 'd':
            display_projects(projects)
        elif choice == 'f':
            filter_projects_by_date(projects)
        elif choice == 'a':
            add_new_project(projects)
        elif choice == 'u':
            update_project(projects)
        elif choice == 'q':
            if input("Would you like to save to {}? (y/n): "
                     .format(DEFAULT_FILE)).lower() == 'y':
                save_projects(projects, DEFAULT_FILE)
            print("Thank you for using custom-built project management software.")
            sys.exit()
        else:
            print("Invalid menu choice.")


if __name__ == "__main__":
    main()