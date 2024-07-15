def sum_two_smallest_numbers(numbers):

    sort_num = sorted(numbers)
    return sum(sort_num[:2])

    numbers.sort()
    return sum(numbers[:2])

print(sum_two_smallest_numbers([5, 8, 12, 18, 22]), 13)
print(sum_two_smallest_numbers([7, 15, 12, 18, 22]), 19)
print(sum_two_smallest_numbers([25, 42, 12, 18, 22]), 30)


def sum_two_smallest_numbers(numbers):
    first_min = min(numbers)
    numbers.remove(first_min)
    second_min = min(numbers)
    return first_min + second_min


def sum_two_smallest_numbers(numbers):
    first_min = min(numbers)
    del numbers[numbers.index(first_min)]
    # del numbers[numbers.index(min(numbers))]
    second_min = min(numbers)
    return first_min + second_min