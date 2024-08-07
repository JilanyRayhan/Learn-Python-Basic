def sumofn(n):
  if n <= 1:
    return n
  else:
    return n + sumofn(n-1)

n = int(input("enter number of terms: "))
if n <= 0:
  print("enter a positive number.")
else:
  print("the sum of the natural number upto the given terms is:",sumofn(n))