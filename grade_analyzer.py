grades = [85, 92, 78, 90, 88, 76, 94, 89, 87, 91]

sliced = grades[2:7:1]
print(sliced)


above = [n for n in grades if n > 85]
print(above)

grades[3] = 95
print(grades)


grades.append(88)
grades.append(92)
grades.append(75)

print(grades)

grades.sort(reverse=True)
print(grades[0:6:1])

print(grades[:5])