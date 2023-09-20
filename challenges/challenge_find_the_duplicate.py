def find_duplicate(nums):
    if not nums:
        return False

    seen_numbers = set()
    for number in nums:
        if not isinstance(number, (int, float)) or number < 0:
            return False
        if number in seen_numbers:
            return number
        seen_numbers.add(number)
        # print(seen_numbers)
    return False
    raise NotImplementedError


# print(find_duplicate([3, 1, 2, 4, 6, 5, 7, 7, 7, 8]))
