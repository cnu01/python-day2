students = ['Alice','Bob','Carol','David','Eve']
scores = [85,92,78,88,95]

for i,student in enumerate(students,start=1):
    print(f'{i} . {student}')
    
for i,(student,score) in enumerate(zip(students,scores),start=1):
    print(f'{i} . {student} - {score}')
    
    
high_scorer_positions = [i for i, score in enumerate(scores) if score > 90]
print(high_scorer_positions)

position_to_name = {i: name for i, name in enumerate(students)}
print(position_to_name)
