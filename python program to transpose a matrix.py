a = [[4,5,2],
  [2,8,9]]

result = [[0,0],
       [0,0],
       [0,0]]

for i in range(len(a)):
for j in range(len(a[0])):
  result[j][i] = a[i][j]

for r in result:
print(r)