from typing import List

class Solution:
  def twoSum(self, numbers: List[int], target: int) -> List[int]:

    seen = {} # value : index
    for index, number in enumerate(numbers):
      if (target - number) in seen:
        return [index, seen[target-number]]
      
      seen[number] = index

    return
  
sol = Solution()

print(sol.twoSum([13,6,8,2,1], 3))