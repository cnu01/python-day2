monday = {"Alice", "Bob", "Charlie", "David"}
tuesday = {"Bob", "Charlie", "Eve", "Frank"}
wednesday = {"Charlie", "George", "Alice", "Frank"}


unique_visitors = monday | tuesday | wednesday
print("Unique Visitors:", unique_visitors)



returning_tuesday = monday & tuesday
print("Returning Visitors on Tuesday:", returning_tuesday)


new_monday = monday
new_tuesday = tuesday - monday
new_wednesday = wednesday - (monday | tuesday)

print("New on Monday:", new_monday)
print("New on Tuesday:", new_tuesday)
print("New on Wednesday:", new_wednesday)


loyal_visitors = monday & tuesday & wednesday
print("Loyal Visitors:", loyal_visitors)


print("Monday & Tuesday:", monday & tuesday)
print("Tuesday & Wednesday:", tuesday & wednesday)
print("Monday & Wednesday:", monday & wednesday)
