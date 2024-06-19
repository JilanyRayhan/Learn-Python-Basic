a = 0
b = 1
num = int(input('enter a number to obtain fibonacci sequence: '))

for i in range(1,num+1):
  if i == 1:
    print(a)
  elif i == 2:
    print(b)
  else:
    c = a + b
    a = b
    b = c
    print(c)