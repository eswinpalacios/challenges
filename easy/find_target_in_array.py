def binary_search(numbers, target, pos_start, pos_end):
    pos = (pos_start + pos_end) // 2

    if pos_end < pos_start: 
        return False

    if target == numbers[pos]:
        return True
    elif target > numbers[pos]:
        return binary_search(numbers, target, pos + 1, pos_end)
    else:
        return binary_search(numbers, target, pos_start, pos-1)

numbers = [2, 2, 3, 4, 8, 9]
print(binary_search(numbers, 1, 0, len(numbers) - 1)) # False
print(binary_search(numbers, 4, 0, len(numbers) - 1)) # True
print(binary_search(numbers, 5, 0, len(numbers) - 1)) # False
print(binary_search(numbers, 10, 0, len(numbers) - 1)) # False
