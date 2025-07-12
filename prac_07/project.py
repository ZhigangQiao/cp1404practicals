# project.py

import datetime


def main():
    # Example usage of the Project class
    project1 = Project("Project A", datetime.date(2024, 3, 23), "High", 10000, 50)
    print(project1)


class Project:
    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        return f"{self.name}, start: {self.start_date}, priority {self.priority}, " \
               f"estimate: ${self.cost_estimate: .2f}, completion: {self.completion_percentage}%"


if __name__ == "__main__":
    main()
