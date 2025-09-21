class Solution:
  def manipulate(self, nums: list[int])-> int:
    a, b = 0, 1
    step = 1

    while len(nums) > 1:
      if step == 1:
        nums = self.stepone(nums)
        step = 2
      elif step == 2:
        nums = self.steptwo(nums)
        step = 1
    return nums

  def stepone(self, nums: list[int])->list[int]:
    i = 0
    res = []
    while i < len(nums)-1:
      res.append(nums[1] + nums[i+1])
      i += 2
    return res
  
  def steptwo(self, nums: list[int])->list[int]:
    i = 0
    res = []
    while i < len(nums)-1:
      res.append(nums[1] * nums[i+1])
      i += 2
    return res
  
a = [1, 2, 3, 4,6,8,9,10]
sol = Solution()
print(sol.manipulate(a))
    