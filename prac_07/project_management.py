import datetime
from project import Project


def main():
    projects = load_projects("projects.txt")
    print(f"Welcome to Pythonic Project Management\nLoaded {len(projects)} projects from projects.txt")

    while True:
        print("\n- (L)oad projects")
        print("- (S)ave projects")
        print("- (D)isplay projects")
        print("- (F)ilter projects by date")
        print("- (A)dd new project")
        print("- (U)pdate project")
        print("- (Q)uit")

        choice = input(">>> ").lower()

        if choice == 'l':
            file_name = input("Enter filename to load projects from: ")
            projects = load_projects(file_name)
            print(f"Loaded {len(projects)} projects from {file_name}")

        elif choice == 's':
            file_name = input("Enter filename to save projects to: ")
            save_projects(file_name, projects)
            print(f"Projects saved to {file_name}")

        elif choice == 'd':
            display_projects(projects)

        elif choice == 'f':
            filter_projects_by_date(projects)

        elif choice == 'a':
            add_new_project(projects)

        elif choice == 'u':
            update_project(projects)

        elif choice == 'q':
            save_choice = input("Would you like to save to projects.txt? ").lower()
            if save_choice.startswith('y'):
                save_projects("projects.txt", projects)
            print("Thank you for using custom-built project management software.")
            break


def load_projects(file_name):
    projects = []
    with open(file_name, 'r') as file:
        next(file)  # skip header
        for line in file:
            data = line.strip().split('\t')
            name = data[0]
            start_date = datetime.datetime.strptime(data[1], "%d/%m/%Y").date()
            priority = int(data[2])
            cost_estimate = float(data[3])
            completion_percentage = int(data[4])
            projects.append(Project(name, start_date, priority, cost_estimate, completion_percentage))
    return projects


def save_projects(file_name, projects):
    with open(file_name, 'w') as file:
        file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            file.write(
                f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t{project.priority}"
                f"\t{project.cost_estimate}\t{project.completion_percentage}\n")


def display_projects(projects):
    incomplete_projects = [project for project in projects if project.completion_percentage < 100]
    completed_projects = [project for project in projects if project.completion_percentage == 100]

    print("Incomplete projects:")
    for project in sorted(incomplete_projects, key=lambda x: x.priority):
        print(f"  {project}")

    print("Completed projects:")
    for project in sorted(completed_projects, key=lambda x: x.priority):
        print(f"  {project}")


def filter_projects_by_date(projects):
    date_string = input("Show projects that start after date (dd/mm/yyyy): ")
    filter_date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    filtered_projects = [project for project in projects if project.start_date > filter_date]
    for project in sorted(filtered_projects, key=lambda x: x.start_date):
        print(f"  {project}")


def add_new_project(projects):
    name = input("Name: ")
    start_date = datetime.datetime.strptime(input("Start date (dd/mm/yyyy): "), "%d/%m/%Y").date()
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    completion_percentage = int(input("Percent complete: "))
    projects.append(Project(name, start_date, priority, cost_estimate, completion_percentage))


def update_project(projects):
    display_projects(projects)
    project_choice = int(input("Project choice: "))
    project = projects[project_choice]
    new_percentage = input("New Percentage: ")
    if new_percentage:
        project.completion_percentage = int(new_percentage)
    new_priority = input("New Priority: ")
    if new_priority:
        project.priority = int(new_priority)


if __name__ == "__main__":
    main()
