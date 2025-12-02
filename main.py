def build_roster(registrations):
    roster = {}

    for student, course in registrations:
        if course not in roster:
            roster[course] = set()
        roster[course].add(student)

    # Convert sets to sorted lists
    return {course: sorted(list(students)) for course, students in roster.items()}
