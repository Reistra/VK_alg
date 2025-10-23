"""Является ли слово палиндромом? Метод двух указателей."""

def is_palindrome(word):
    left = 0
    right = len(word) - 1

    while left < right:
        if word[left] != word[right]:
            return False
        left += 1
        right -= 1

    return True


values = [1, 2, 3, 2, 1]
print(is_palindrome("racecar"))  # True
print(is_palindrome("hello"))    # False
print(is_palindrome(values))     # True