import heapq


def findkthlarget(nums, k):
    for i in range(len(nums)):
        nums[i] = -nums[i]

    heapq.heapify(nums)

    for _ in range(k-1):
        heapq.heappop(nums)

    return -heapq.heappop(nums)


nums = [2,5,72,6,7,2,1]
print(findkthlarget(nums, 2))
