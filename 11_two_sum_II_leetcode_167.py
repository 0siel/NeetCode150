class Solution:
  def twoSum(self, nums: list[int], target: int)-> list[int]:
    l, r = 0, len(nums) - 1

    while l < r:
     sum = nums[l] + nums[r]
     if sum > target:
       r -=1
     elif sum < target:
       l += 1
     else:
       return (l + 1, r + 1)
     
sol = Solution()
print(sol.twoSum([1,2,3,6,5,4], 10))

