class Solution:
  def productExceptSelf(self, nums: list[int]) -> list[int]:
    res = [1] * len(nums)

    postfix = 1

    for i in range(1, len(nums)):
      res[i] = nums[i - 1] * res[i - 1]

    print(res)

    for i in range(len(nums) - 2, -1, -1):
      postfix *= nums[i + 1]
      res[i] *= postfix

    print(res)

    
    

    
  
sol = Solution()
print(sol.productExceptSelf([1,2,3,4]))