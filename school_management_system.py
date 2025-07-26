school = {
    "ClassA": {
        "teacher": "Mr. Smith",
        "students": [("Alice", 85), ("Bob", 90), ("Charlie", 78)]
    },
    "ClassB": {
        "teacher": "Ms. Johnson",
        "students": [("David", 92), ("Eva", 88), ("Frank", 75)]
    },
    "ClassC": {
        "teacher": "Mrs. Lee",
        "students": [("Grace", 95), ("Hank", 80), ("Ivy", 89)]
    }
}

# Print Teacher Names
for cls in school.values():
    print(cls["teacher"])

# Calculate Class Average Grades
for class_name, details in school.items():
    total = sum(grade for _, grade in details["students"])
    avg = total / len(details["students"])
    print(f"{class_name} Average: {avg:.2f}")

# Find Top Student Across All Classes
top_student = ("", 0)
for details in school.values():
    for name, grade in details["students"]:
        if grade > top_student[1]:
            top_student = (name, grade)
print(f"Top Student: {top_student[0]} with grade {top_student[1]}")
