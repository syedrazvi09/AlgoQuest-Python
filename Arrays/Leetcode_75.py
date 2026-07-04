def sort_colors(arr):
    first_index = 0
    last_index = len(arr) - 1

    for i in range(len(arr)):
        if arr[i] == 0:
            arr[first_index], arr[i] = arr[i], arr[first_index]
            first_index += 1

    for i in range(last_index, first_index - 1, -1):
        if arr[i] == 2:
            arr[last_index], arr[i] = arr[i], arr[last_index]
            last_index -= 1

    print(arr)


arr = [1,0,2,2,1,1,0,1,0,2]
sort_colors(arr
            )