def check_pal(num):
  if num == num[::-1]:
    print(f"{num} is a palindrome.")
  else:
    print(f"{num} is not a palindrome.")

n = str(input("enter a word: "))
check_pal(n)