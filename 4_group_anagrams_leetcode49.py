from typing import List
from collections import defaultdict
class Solution:
  def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    res = defaultdict(list) # for handling empty values

    for s in strs:
      count = [0] * 26

      for c in s:
        count[ord(c)-ord('a')] += 1

      res[tuple(count)].append(s) # hashmaps key should be unmutable, lists are mutable, tuples are unmutable 
    return res.values()

sol = Solution()


strs = ("cat", "eat", "act", "ate", "act", "bat")
print(sol.groupAnagrams(strs))

  

      

