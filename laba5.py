class Bug:
    def __init__(self, description, severity, deadline, status, assignee):
        self.description = description
        self.severity = severity
        self.deadline = deadline
        self.status = status
        self.assignee = assignee
      #
    def __str__(self):
        return f"Bug: {self.description}, Severity: {self.severity}, Deadline: {self.deadline}, Status: {self.status}, Assignee: {self.assignee}"

    def get_assignee(self):
        return self.assignee

    def get_status(self):
        return self.status

    def set_status(self, new_status):
        self.status = new_status


class Backlog:
    def __init__(self):
        self.bugs = []

    def add_bug(self, bug):
        self.bugs.append(bug)

    def display_assigned_resolved_bugs(self, assignee):
        assigned_resolved_bugs = [bug for bug in self.bugs if bug.get_assignee() == assignee and bug.get_status() == "RESOLVED"]
        for bug in assigned_resolved_bugs:
            print(bug)

    def sort_by_severity(self):
        self.bugs.sort(key=lambda x: x.severity)

    def display_backlog(self):
        for bug in self.bugs:
            print(bug)


def main():
    # Creating Bug instances
    bug1 = Bug("UI issue", "Critical", "2023-12-01", "OPEN", "John")
    bug2 = Bug("Functionality problem", "High", "2023-12-10", "IN PROGRESS", "Alice")
    bug3 = Bug("Database error", "Medium", "2023-11-30", "RESOLVED", "Bob")
    bug4 = Bug("Performance bug", "Low", "2023-12-05", "RESOLVED", "John")

    # Creating Backlog instance and adding bugs
    backlog = Backlog()
    backlog.add_bug(bug1)
    backlog.add_bug(bug2)
    backlog.add_bug(bug3)
    backlog.add_bug(bug4)

    # Displaying the original backlog
    print("Original Backlog:")
    backlog.display_backlog()

    # Displaying resolved bugs assigned to a specific developer
    assignee_name = "John"
    print(f"\nResolved Bugs assigned to {assignee_name}:")
    backlog.display_assigned_resolved_bugs(assignee_name)

    # Sorting the backlog by severity
    backlog.sort_by_severity()
    print("\nBacklog after sorting by severity:")
    backlog.display_backlog()


if __name__ == "__main__":
    main()
