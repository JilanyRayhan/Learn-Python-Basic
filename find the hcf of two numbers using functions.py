def div(a,b):
  while b != 0:
    a , b = b , a % b
  return a

def hcf(num1,num2):
  a = max(num1,num2)
  b = min(num1,num2)
  return div(a,b)

print(hcf(18,12))
