a = [[4,5,2],
  [2,8,9],
  [3,5,6]]

b = [[1,4,8],
  [6,7,3],
  [9,8,1]]

result = [[0,0,0],
       [0,0,0],
       [0,0,0]]

for i in range(len(a)):
for j in range(len(a[0])):
  result[i][j] = a[i][j] + b[i][j]

for r in result:
print(r)