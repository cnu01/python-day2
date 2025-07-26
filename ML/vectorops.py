a = [1, 2, 3]

b = [4, 5, 6]

sum = []
dotproduct = 0

for i, (iteama, iteamb) in enumerate(zip(a,b)): 
    sum.append(iteama + iteamb)
    dotproduct += iteama * iteamb
    
    
print(sum,dotproduct)
if dotproduct == 0 :
    print('Orthogonal')
else :
    print('Not Orthogonal')
    

A = [[1, 2], [3, 4]]

B = [[5, 6], [7, 8]]

result = [[0, 0],[0, 0]]


for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            result[i][j] += A[i][k] * B[k][j]


for row in result:
    print(row)