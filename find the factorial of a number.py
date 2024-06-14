num = int(input('enter a number: '))
store = 1
if num >= 0:
  for i in range(1,num+1):
    store = store * i
  print(store)
else:
  print('factorial of a negative number is not possible.')