"""Дан не отсортированный массив целых чисел. Необходимо перенести в начало массива все четные числа, сохраняя их очередность"""

arr = list(map(int, input("Введите массив целых чисел: \n").split()))

def move_even_first_array(arr):
    even_ind = 0

    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            arr[i], arr[even_ind] = arr[even_ind], arr[i]
            even_ind += 1
        
    return arr

print(move_even_first_array(arr))