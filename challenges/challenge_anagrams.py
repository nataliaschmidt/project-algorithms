def merge_sort(arr):
    # caso base
    if len(arr) <= 1:
        return arr

    middle = len(arr) // 2
    left = arr[:middle]
    right = arr[middle:]
    print(left, right)

    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)


def merge(left, right):
    result = ""
    left_index, right_index = 0, 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result += left[left_index]
            left_index += 1
        else:
            result += right[right_index]
            right_index += 1

    result += left[left_index:]
    result += right[right_index:]

    return result


def is_anagram(first_string, second_string):
    if len(first_string) == 0 and len(second_string) == 0:
        return first_string, second_string, False

    sorted_first_string = merge_sort(first_string.lower())
    sorted_second_string = merge_sort(second_string.lower())
    is_strings_anagram = sorted_first_string == sorted_second_string

    if len(first_string) != len(second_string):
        return sorted_first_string, sorted_second_string, is_strings_anagram

    return sorted_first_string, sorted_second_string, is_strings_anagram
    raise NotImplementedError


print(is_anagram("", ""))
