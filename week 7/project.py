"""
Project class for the Project Management Program.
Estimated completion time: 4–5 hours (iterative development).
"""


class Project:
    """Represent a single project."""

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """Initialise a Project with validation-ready types."""
        self.name = name
        self.start_date = start_date            # datetime.date object
        self.priority = int(priority)
        self.cost_estimate = float(cost_estimate)
        self.completion_percentage = int(completion_percentage)

    def __repr__(self):
        return (f"{self.name}, start: {self.start_date:%d/%m/%Y}, "
                f"priority {self.priority}, "
                f"estimate: ${self.cost_estimate:,.2f}, "
                f"completion: {self.completion_percentage}%")

    def __lt__(self, other):
        """Sort Projects by priority (ascending)."""
        return self.priority < other.priority

    def is_completed(self):
        """Utility helper: project finished when 100 %."""
        return self.completion_percentage == 100