num = float(input('enter a number: '))
store = 0
while num/10 != 0:
  last_digit = num % 10
  num = int(num/10)
  store = store + last_digit

print(store)