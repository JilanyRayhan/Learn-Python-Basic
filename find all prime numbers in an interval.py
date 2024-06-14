low = int(input('enter the range - lowest limit: '))
high = int(input('enter the range - highest limit: '))
quantity = 0

for num in range(low,high+1):
  if num > 1:
    for i in range(2, num):
      if num % i == 0:
        break
    else:
      print(num)
      quantity += 1
print('total prime numbers found: ',quantity)