class Solution:
  def containsDuplicate(self, numbers: list[int]) -> bool:
    hashset = set()

    for number in numbers:
      if number in hashset:
        return True
      hashset.add(number)
    return False


sol =  Solution()
print(sol.containsDuplicate([1,3,4,5,2]))
    