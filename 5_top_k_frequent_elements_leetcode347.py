class Solution:
  def topKFrequent(self, nums: list[int], k: int) -> list[int]:

    count = {}
    freq = [[] for i in range(len(nums) +1)]

    for num in nums:
      count[num] = 1 + count.get(num, 0)
    for n, c in count.items():
      freq[c].append(n)

    res = []
    for i in range(len(freq) -1, 0, -1):
      for n in freq[i]:
        res.append(n)
        if len(res) == k:
          return res


    

        
sol = Solution()

print(sol.topKFrequent([1,2,5,7,7,7,2,3,3,3],2))




