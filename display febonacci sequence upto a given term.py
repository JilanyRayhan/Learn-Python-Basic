def feb(num1, num2, term):
  fib_list = []
  # Append initial numbers
  fib_list.append(num2)
  fib_list.append(num1)

  # Calculate the next Fibonacci number
  num3 = num1 + num2

  while num3 < term:
      # Append the next number in the sequence
      fib_list.append(num3)

      # Update the sequence
      num2 = num1
      num1 = num3
      num3 = num1 + num2

  return fib_list

n = int(input("Enter the upper limit for terms: "))
a = feb(0, 1, n)  # Start with 0 and 1 for the traditional Fibonacci sequence
print(a)