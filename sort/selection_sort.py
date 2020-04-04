def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0

    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i

    return smallest_index

def sort(arr):
    result = []

    for i in range(len(arr)):
        smallest = find_smallest(arr)
        result.append(arr.pop(smallest))

    return result

res = sort([8, -2, 2, 1, 0, 9, 6, -4])
res = sort([])
print(res)