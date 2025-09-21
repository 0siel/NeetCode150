class  Solution:
  def trap(self, height: list[int])-> int:
    l, r = 0, len(height) - 1
    maxLeft, maxRight = height[l], height[r]
    res = 0

    while l < r:
      if maxLeft < maxRight:
        l += 1
        maxLeft = max(maxLeft, height[l])
        res  += maxLeft - height[l]
      else:
        r -= 1
        maxRight = max(maxRight, height[r])
        res += maxRight - height[r]
    return res
  
sol = Solution()
print(sol.trap([0,1,0,2,1,0,1,3,2,1,2,1]))