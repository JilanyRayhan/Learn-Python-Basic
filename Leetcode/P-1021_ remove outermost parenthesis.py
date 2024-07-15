class Solution:
  def removeOuterParentheses(self, s: str) -> str:
      result = []
      p_count = 0
      start = 0
      for index,char in enumerate(s):
          if char == "(":
              p_count += 1
          elif char == ")":
              p_count -= 1
          if p_count == 0:
              result.append(s[start+1:index])
              start = index + 1
      return "".join(result)

# Example usage:
s1 = "(()())"
sol = Solution()
result = sol.removeOuterParentheses(s1)
print(result)  # Output: "()()()()(())"
