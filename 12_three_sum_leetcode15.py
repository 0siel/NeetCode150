class Solution():
  def threeSum(self, nums: list[int], target: int)->list[list[int]]:
    nums.sort()
    res = []

    for i in range(len(nums)-1):

      if i > 0 and nums[i] == nums[i + 1]:
        continue

      left, right = i + 1, len(nums) - 1

      while left < right:
        total = nums[i] + nums[left] + nums[right]

        if total == target:
          res.append([nums[i], nums[left], nums[right]])

          while left < right and nums[left] == nums[left  + 1]:
            left += 1

          while left < right and nums[right] == nums[right - 1]:
            right -= 1

          left += 1
          right -= 1

        elif(total > target):
          right -= 1

        else:
          left += 1

    return res
  
sol = Solution()
print(sol.threeSum([5,-3,-2,1,0,-1,6,-3,-4], 0))



def threeSumF(nums, target=0):
  res = []
  nums.sort()

  for i, a in enumerate(nums):
    if i > 0 and nums[i] == nums[i -1]:
      continue
    l, r = i +1, len(nums) - 1
    while l < r:
      threeSum = a + nums[l] + nums[r]
      if threeSum < target:
        l += 1
      elif threeSum > target:
        r -= 1
      else:
        res.append([a, nums[l], nums[r]])
        l += 1
        while nums[l] == nums[l - 1] and l < r:
          l += 1
  return res


print(threeSumF([5,-3,-2,1,0,-1,6,-3,-4], 0))


