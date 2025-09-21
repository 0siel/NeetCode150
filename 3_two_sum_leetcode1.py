from typing import List

class Solution:
  def twoSum(self, numbers: List[int], target: int) -> List[int]:

    seen = {}

    for index, number in enumerate(numbers):
      if target - number in seen:
        return seen[target - number], index
      seen[number] = index 
  
sol = Solution()

print(sol.twoSum([13,6,8,2,1], 7))