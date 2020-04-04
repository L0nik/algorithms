def search(input_list, item):

    low = 0
    high = len(input_list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = input_list[mid]
        if guess == item:
            return mid
        elif guess < item:
            low = mid + 1
        else:
            high = mid - 1

    return None

print(search([1, 2, 3, 4], 4))