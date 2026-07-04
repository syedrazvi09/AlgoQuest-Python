def max_element(arr):
    freq = {}
    for i in arr:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
        # dictionary created after this loop ends

    max_freq = 0
    element = None

    for key, val in freq.items():
        if val > max_freq:
            max_freq = val
            element = key
        if max_freq > (len(arr))/2:
            return element
    return element

arr = [2,2,6,4,8,1,4,4,3]
print(max_element(arr))