a = [[4,5,2],
  [2,8,9]]

t = [[a[j][i] for j in range(len(a))] for i in range(len(a[0]))]

for T in t:
print(T)