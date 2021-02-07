# Increment a number from [1] => [2]
# [1, 9] => [2, 0]
# [0] => [1, 0]

def increment_by_x(numbers=[], number=1):
    index = len(numbers) - 1
    carry = number

    while carry > 0 and index > -1:
        current_number = numbers[index] + carry
        numbers[index] = current_number % 10
        index = index - 1
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
