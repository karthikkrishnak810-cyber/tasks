class InvalidMarkError(Exception):
    """Custom exception for invalid marks."""
    pass


def calculate_grade(name, *marks):
    if not marks:
        return name, 0, "No Marks"

    for mark in marks:
        if mark < 0 or mark > 100:
            raise InvalidMarkError(
                f"Invalid mark {mark} for {name}. Marks must be between 0 and 100."
            )

    average = sum(marks) / len(marks)

    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 50:
        grade = "C"
    else:
        grade = "F"

    return name, average, grade


def generate_report(students):
    print("-" * 50)
    print(f"{'Name':<15}{'Average':<15}{'Grade':<10}")
    print("-" * 50)

    for student in students:
        try:
            name, avg, grade = calculate_grade(*student)
            print(f"{name:<15}{avg:<15.2f}{grade:<10}")
        except InvalidMarkError as e:
            print(f"{student[0]:<15}{'ERROR':<15}{str(e)}")

    print("-" * 50)


# Test Cases
students = [
    ("Alice", 95, 88, 92),      # Valid marks
    ("Bob", 150, 80, 70),       # Invalid mark
    ("Charlie",),               # Empty marks
    ("David", 60, 40, 110),     # Mixed valid and invalid
]

generate_report(students)