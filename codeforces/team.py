n = int(input())
s = 0
for i in range(n):
  view = input()
  a,b,c = map(int,view.split(' '))
  if a + b + c >= 2:
    s = s + True
  else:
    s = s + False
print(s)