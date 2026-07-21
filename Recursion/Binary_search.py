def binarySearch(arr, left, right, target):
    if left >= right:
        return -1

    mid = (left + right) // 2

    if arr[mid] == target:
        return mid

    if arr[mid] < target:
        return binarySearch(arr, mid + 1, right, target)

    if arr[mid] > target:
        return binarySearch(arr, left, mid, target)


arr = [2,5,8,9,11,23]
n = len(arr)
print(binarySearch(arr, 0, n, 11))