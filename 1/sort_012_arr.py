"""Дан массив состоящий из нулей, единиц и двоек. Необходимо его отсортировать за линейное время """

arr = list(map(int, input("Введите массив из 0, 1 и 2: \n").split()))

def sort_012_array(arr):
    low, mid, high = 0, 0, len(arr) - 1

    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        if arr[mid] == 2:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
        if arr[mid] == 1:
            mid += 1
        
    return arr

print(sort_012_array(arr))