class Solution:
  def matchCount(self, source: str, pattern: str)-> int:
    patLen = len(pattern)
    res = 0
    for i in range(len(source)):
        subS= source[i:i + patLen]
        if self.matches(pattern, subS):
          res += 1
    return res


  def matches(self, p: str, s:str)-> bool:
    for i in range(len(p)):
      if p[i] == '0' and s[i] not in ('a', 'e', 'i', 'o', 'u', 'y'):
        return False
      elif p[i] == '1' and s[i] in ('a', 'e', 'i', 'o', 'u', 'y'):
        return False
    return True

pattern = "010"
source = "amazing"

sol = Solution()
print(sol.matchCount(source, pattern))