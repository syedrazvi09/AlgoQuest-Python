def move_zeros(arr):
    next_index = 0
    for i in range(len(arr)):
        if arr[i] == 0:
            continue
        else:
            arr[next_index] = arr[i]
            next_index += 1

    for i in range(next_index, len(arr)):
        arr[i] = 0

    print(arr)


arr = [0,4,8,0,1,4,6,0]
move_zeros(arr)