class Solution:
  def isPalindrome(self, x : int) -> bool:
    conv = str(x)
    return conv == conv[::-1]

num = int(input("enter a number to check palindrome: "))
sol = Solution()
result = sol.isPalindrome(num)
print(result)