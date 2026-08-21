def threesumclose(nums, target):
    arr = sorted(nums)
    close = None


    for i in range(len(arr) - 2):
        l, r = i + 1, len(nums) - 1
        while l < r:

            curSum = arr[i] + arr[l] + arr[r]

            if curSum > target:
                r -= 1
            elif curSum < target:
                l += 1
            else:
                return curSum
            if close is None:
                close = curSum
            elif abs(curSum - target) < abs(close - target):
                close = curSum

    return close



nums = [-1,2,1,-4]
target = 1

print(threesumclose(nums, target))