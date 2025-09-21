class Solution:
  def longestConsecutiveSequence(self, nums: list[int]) -> int:
    numset = set(nums)
    longest = 0

    for n in nums:
      if n - 1 not in numset:
        length = 1
        while n + length in numset:
          length += 1
          if length > longest:
            longest = length
    return longest
      



sol = Solution()
print(sol.longestConsecutiveSequence([6, 4, 200, 2, 3, 5, 7]))