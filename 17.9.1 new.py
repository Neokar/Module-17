def qsort(array, left, right):
    middle = (left + right) // 2
    p = array[middle]
    i, j = left, right
    while i <= j:
        while array[i] < p:
            i += 1
        while array[j] > p:
            j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1

    if j > left:
        qsort(array, left, j)
    if right > i:
        qsort(array, i, right)


def binary_search(array, element, left, right):
    if left > right:
        return right
    middle = (right + left) // 2
    if array[middle] == element:
        return middle - 1
    elif element < array[middle]:
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)


try:
    array = list(map(int, input("Введите последовательность целых чисел через пробел: ").split()))
    element = int(input("Введите целое число: "))
except ValueError:
    print("Ошибка ввода. Пример: 1 5 3 8 22 12")
    exit(0)

qsort(array, 0, (len(array) - 1))
result = binary_search(array, element, 0, len(array) - 1)
if result < 0 or result >= (len(array) - 1):
    print("Вы ввели некорректное число. Ох уж эти кожаные мешки....")
else:
    print(array)
    print(result)
