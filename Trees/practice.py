def twoSum(numbers, target):
    seen = {}

    for key, val in enumerate(numbers):
        goal = target - val
        if goal in seen:
            return [seen[goal] + 1, key + 1]
        seen[val] = key


nums = [2,7,11,15]
print(twoSum(nums, 9))




