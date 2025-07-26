class Solution:
  def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
      return False
    
    alphabet = [0] * 26

    for i in range(len(s)):
      alphabet[ord(s[i]) - ord('a')] += 1
      alphabet[ord(t[i]) - ord('a')] -= 1

    for letter in alphabet:
      if letter != 0:
        return False
      
    return True
    
sol = Solution()

print(sol.isAnagram("cat", "naragam"))
print(sol.isAnagram("anagram", "naragam"))
print(sol.isAnagram("gaby", "abyg"))


