"""Необходимо написать функцию которая объединит два отсорированных массива в один отсортированный."""

arr1 = list(map(int, input("Введите отсортированный массив: \n").split()))
arr2 = list(map(int, input("Введите отсортированный массив: \n").split()))

def merge_sorted_arrays(arr1, arr2):
    arr_merged = []
    i, j = 0, 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            arr_merged.append(arr1[i])
            i += 1
        else:
            arr_merged.append(arr2[j])
            j += 1

    if i < len(arr1):
        arr_merged.extend(arr1[i:])
    if j < len(arr2):
        arr_merged.extend(arr2[j:])

    return arr_merged

print(merge_sorted_arrays(arr1, arr2))