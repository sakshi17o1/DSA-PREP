#Requirements: 1. Marks in descending order. 2. If marks are equal, names in ascending alphabetical order.

students = [
    ("Ravi", 80),
    ("Asha", 90),
    ("Neha", 80)
]

students.sort(key=lambda x: (-x[1], x[0]))

print(students)