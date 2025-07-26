
student_records = [
                   (101, "Alice", 85, 20),
                    (102, "Bob", 90, 21),
                    (103, "Charlie", 78, 22),
                    (104, "David", 88, 23),
                    (105, "Eve", 92, 19)        
                  ]

heighst_scorer = max(student_records, key=lambda x: x[2]) 
print("Highest Scorer:", heighst_scorer)

nameandgrade = [(student[1], student[2]) for student in student_records]
print("Names and Grades:", nameandgrade)

student_records[0][2] = 98 # Update student ID for Alice
print("Updated Student Records:", student_records)

#Here i am trying to update the grade of user with ID 102, so grade should be not change but tring to change so here we can use tuple to aviod those kind of changes

