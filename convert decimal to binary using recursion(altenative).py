def decimal_to_binary(n):
  if n > 1:
    decimal_to_binary(n // 2)
  print(n % 2, end = "")

if __name__ == "__main__":
  number = int(input("enter a number in decimal: "))
  decimal_to_binary(number)