def counting_sort(arr):
    k = max(arr)
    count = [0] * (k+1)

    for x in arr:
        count[x] += 1

    for i in range(1, k + 1):
        count[i] += count[i-1]

    out = [0] * len(arr)

    for x in reversed(arr):
        count[x] -= 1
        out[count[x]] = x

    return out

arr = [4,2,2,8,3,3,1]
print(counting_sort(arr))