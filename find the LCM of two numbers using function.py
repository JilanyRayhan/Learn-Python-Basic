def hcf(num1,num2):
  a = max(num1,num2)
  b = min(num1,num2)
  return div(a,b)

def div(a,b):
  d = a * b
  while a % b != 0:
    c = a % b
    a = b
    b = c

  return d/b

print(hcf(1424,3084))