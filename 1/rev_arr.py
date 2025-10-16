"""Дан массив целых чисел. Необходимо развернуть его. Сделать за линейное время без дополнительных аллокаций."""

arr = list(map(int, input().split()))

def reverce_array(arr):
    left, right = 0, len(arr) - 1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr

print(reverce_array(arr))