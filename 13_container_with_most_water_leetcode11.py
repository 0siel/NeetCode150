class Solution:
  def maxArea(self, heights: list[int])->int:
    l, r = 0, len(heights) -1
    maxArea = 0

    while l < r:
      area = (r - l) * min(heights[l], heights[r])
      maxArea = max(maxArea, area)

      if heights[l] < heights[r]:
        l +=1
      else:
        r -=1
    return maxArea
  
sol = Solution()
print(sol.maxArea([7,8,3,4,53,2,1]))