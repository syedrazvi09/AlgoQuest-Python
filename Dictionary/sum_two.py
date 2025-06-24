def two_sums(nums, target):
  seen = {}
  for i, num in enumerate(nums):
    complement = target - num
    if complement in seen:
      return [seen[complement], i]
    seen[num] = i

nums = [2, 7 , 11, 15]
target = 13
print(two_sums(nums,target))