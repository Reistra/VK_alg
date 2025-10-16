"""Необходимо написать функцию которая объединит два отсорированных массива в один отсортированный. Без дополнительного аллоцирования памяти."""

arr1 = list(map(int, input("Введите первый отсортированный массив: \n").split()))
arr2 = list(map(int, input("Введите второй отсортированный массив: \n").split()))

def merge_sorted_arrays(arr1, arr2):
    arr1.extend([0] * len(arr2))  # Расширяем arr1, чтобы вместить элементы arr2

    # p1 - по arr1, p2 - по arr2, p3 - по расширенному arr1
    pointer1, pointer2, pointer3 = len(arr1) - len(arr2) - 1, len(arr2) - 1, len(arr1) - 1

    while pointer1 >= 0 and pointer2 >= 0:
        if arr1[pointer1] > arr2[pointer2]:
            arr1[pointer3] = arr1[pointer1]
            pointer1 -= 1
        else:
            arr1[pointer3] = arr2[pointer2]
            pointer2 -= 1

        pointer3 -= 1

    if pointer2 >= 0:
        arr1[:pointer2 + 1] = arr2[:pointer2 + 1]
    
    return arr1

print(merge_sorted_arrays(arr1, arr2))

