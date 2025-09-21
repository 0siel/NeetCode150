class Solution:

  def encode(self, strs):
    res = ""
    for s in strs:
      res += str(len(s)) + "#" + s
    return res
  
  def decode(self, s):
    res = []
    i = 0
    while i < len(s):
      j = i
      while s[j] != '#':
        j += 1
      strl = s[i:j]
      wl = int(strl)
      word = s[j + 1: j + 1 + wl]
      res.append(word)
      i =  j + 1 + wl
        
        

        
    
      
    return res
  
sol = Solution()
strs = ["Hello", "world"]
encoded_strs = sol.encode(strs)
print(sol.decode(encoded_strs))
print(strs == sol.decode(encoded_strs))  
