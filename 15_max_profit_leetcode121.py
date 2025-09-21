class Solution:
  def maxProfit(self, prices: list[int])-> list[int]:
    l, r = 0, 1
    maxprofit = 0

    while r < len(prices):
      if prices[l] < prices[r]:
        profit = prices[r] - prices[l]
        maxprofit = max(maxprofit, profit)
      else: l = r
      r+=1
    return maxprofit
  
sol = Solution()
print(sol.maxProfit([6,1,5,3,4,9]))

      
