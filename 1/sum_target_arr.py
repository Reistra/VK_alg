"""Дан отсортированный по возрастанию массив целых чисел и некоторое число target.
    Необходимо найти два числа в массиве, которые в сумме дают заданное значение target, и вернуть их индексы."""

arr = list(map(int, input("Введите отсортированный массив:\n").split()))
target = int(input())

def two_sum(arr, target):
    left, right = 0, len(arr) - 1

    while left < right:
        cur_sum = arr[left] + arr[right]
        if cur_sum == target:
            return [left, right]
        if cur_sum < target:
            left += 1
        else:
            right -= 1
    return [-1, -1] 

print(two_sum(arr, target))