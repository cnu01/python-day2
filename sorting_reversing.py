employees = [
    ("Alice", 50000, "Engineering"),
    ("Bob", 60000, "HR"),
    ("Charlie", 55000, "Engineering"),
    ("David", 45000, "Marketing"),
    ("Eve", 65000, "HR"),
    ("Frank", 48000, "Marketing")
]


# Ascending order by salary
sorted_by_salary_asc = sorted(employees, key=lambda x: x[1])
print("Salary Ascending:", sorted_by_salary_asc)

# Descending order by salary
sorted_by_salary_desc = sorted(employees, key=lambda x: x[1], reverse=True)
print("Salary Descending:", sorted_by_salary_desc)


sorted_by_dept_salary = sorted(employees, key=lambda x: (x[2], x[1]))
print("Sorted by Department and then Salary:", sorted_by_dept_salary)


reversed_employees = list(reversed(employees))
print("Reversed List:", reversed_employees)


sorted_by_name_length = sorted(employees, key=lambda x: len(x[0]))
print("Sorted by Name Length:", sorted_by_name_length)


# Using .sort() - modifies the original list
employees_copy = employees.copy()
employees_copy.sort(key=lambda x: x[1])
print("Using .sort():", employees_copy)

# Using sorted() - does not modify the original list
sorted_copy = sorted(employees, key=lambda x: x[1])
print("Using sorted():", sorted_copy)
