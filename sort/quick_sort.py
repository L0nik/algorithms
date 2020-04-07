def qsort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        lesser_items = [item for item in array[1:] if item <= pivot]
        greater_items = [item for item in array[1:] if item > pivot]
        return qsort(lesser_items) + [pivot] + qsort(greater_items)

print("test 1: " + str(qsort([5, 7, 0, -2, 1])))
print("test 2: " + str(qsort([])))