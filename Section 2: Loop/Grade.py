# lambda function matching.
operations = {
    "average": lambda seq: sum(seq) / len(seq),
    "total": lambda seq: sum(seq),
    "top": lambda seq: max(seq)
}

students = [
    {"name": "Rolf", "grades": (67, 90, 95, 100)},
    {"name": "Bob", "grades": (56, 78, 80, 90)},
    {"name": "Jen", "grades": (98, 90, 95, 100)},
    {"name": "Anne", "grades": (100, 100, 95, 100)}
]

for student in students:
    name = student["name"]
    grade = student["grades"]
    print(f"Student : {name}")
    operation = input("Enter one of 'average', 'total', 'top' :")
    operations_function = operations[operation]
    # call it with the student grade, which are the tuples
    print(operations_function(grade))
