"""Есть массив с числами, среди которых есть 0. Необходимо все числа, равные нулю перенести в конец массива."""

arr = list(map(int, input("Введите массив: \n").split()))

def zero_end_array(arr):
    zero_arr = []
    nonzero_arr = []

    zero_arr = [arr[i] for i in range(len(arr)) if arr[i] == 0]
    nonzero_arr = [arr[i] for i in range(len(arr)) if arr[i] != 0]

    arr = nonzero_arr + zero_arr

    return arr

print(zero_end_array(arr))