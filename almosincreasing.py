class Solution:
  def almostIncreasing(self, secuence: list[int])-> bool:
    not_valid= 0
    for i in range(1, len(secuence)):
      if secuence[i] < secuence[i - 1]:
        not_valid +=1
        if not_valid > 1:
          return False
    return True
        

sol = Solution()
print(sol.almostIncreasing([1,2,3,3,2,34]))