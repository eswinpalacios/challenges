# Increment a number from [1] => [2]
# [1, 9] => [2, 0]
# [0] => [1, 0]

def increment_by_x(numbers=[], increment=1):
    carry = increment

    if increment == 0:
        return numbers

    for i in range(len(numbers) - 1, -1, -increment):
        current_number = numbers[i] + carry
        numbers[i] = current_number % 10
        carry = int(current_number / 10)

    if carry > 0:
        numbers.insert(0, 1)

    return numbers


print(increment_by_x([1, 2, 3], 1))
print(increment_by_x([1, 9, 2, 4, 0, 9], 1))
print(increment_by_x([0], 1))
print(increment_by_x([9], 1))
print(increment_by_x([8, 9], 1))
print(increment_by_x([1, 9, 9], 1))
print(increment_by_x([9, 9, 9, 9, 9], 1))
