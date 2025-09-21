class Solution:
  def firstDuplicate(self, nums: list[int])-> int:
    numset =set()
    for i in range(len(nums)):
      if nums[i] in numset:
        return nums[i]
      numset.add(nums[i])
    return -1
      
sol = Solution()
print(sol.firstDuplicate([2,1,3,5,3,2]))
print(sol.firstDuplicate([2,4,3,5,1]))
