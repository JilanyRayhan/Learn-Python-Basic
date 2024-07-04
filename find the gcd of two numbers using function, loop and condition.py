def max_min(x,y):
  if x > y:
    smaller = y
    larger = x
  elif x < y:
    smaller = x
    larger = y
  return smaller,larger
def find_gcd(max,min):
  for i in range(2,smaller):
    if smaller % i == 0 and larger % 2 == 0:
      gcd = i
  return gcd
a = int(input())
b = int(input())
smaller,larger = max_min(a,b)
print(f"the gcd of {smaller} and {larger} is: {find_gcd(smaller,larger)}")