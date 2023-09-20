def is_palindrome_recursive(word, low_index, high_index):
    if not word:
        return False

    # Caso base
    if low_index >= high_index:
        return True
    # Caso recursivo
    if word[low_index] == word[high_index]:
        return is_palindrome_recursive(word, low_index + 1, high_index - 1)

    return False
    raise NotImplementedError

# print(is_palindrome_recursive('AGUA', 0, 3))
