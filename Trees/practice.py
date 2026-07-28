def rob(nums):
    prof1 = 0
    prof2 = 0

    for i in range(0, len(nums), 2):
        prof1 += nums[i]

    for i in range(1, len(nums), 2):
        prof2 += nums[i]

    print(prof1)
    print(prof2)

arr = [1,2,3,1]
rob(arr)