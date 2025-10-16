"""Дан массив, содержащий только 0 и 1. Напишите функцию, которая сортирует его так, чтобы все нули оказались в начале, а все единички — в конце. """

arr = list(map(int, input("Введите бинарный массив: \n").split()))

def sort_01_array(arr):
    left, right = 0, len(arr) - 1

    while left < right:
        if arr[left] == 0:
            left += 1
        if arr[right] == 1:
            right -= 1
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1


    return arr

print(sort_01_array(arr))