numbers = [2,7,8,11,24,3,11]

def contain_duplicates(numbers):
  seen_numbers= set()
  for n in numbers:
    if n in seen_numbers:
      return True
    seen_numbers.add(n)

  return False

print(contain_duplicates(numbers))
