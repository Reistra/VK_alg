""" Дан массив целых чисел. Необходимо развернуть справа налево часть массива, которая указана вторым параметром.
    Сделать это надо за линейное время без дополнительных аллокаций"""

arr = list(map(int, input().split()))
k = int(input())

def reverce_k_array(arr, k):
    k = k % len(arr)

    def reverce_array(arr, left, right):
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        return arr
    
    reverce_array(arr, 0, len(arr) - 1)
    reverce_array(arr, 0, k - 1)
    reverce_array(arr, k, len(arr) - 1)
    return arr

print(reverce_k_array(arr, k))