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
    return array


def binary_search(array, element, left, right):
    if left > right:
        return False

    middle = (right + left) // 2
    if array[middle] == element:
        return middle
    elif element < array[middle]:
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)


try:
    numbers = input('Введите числа через пробел:\n').replace(' ', '')
    digit = int(input('Введите любое число:\n'))
    numbers = list(map(int, numbers))
    numbers = qsort(numbers, 0, len(numbers) - 1)
    if digit not in numbers:
        print("Указанное число не входит в диапазон списка!")
    else:
        digit_index = binary_search(numbers, digit, 0, len(numbers))
        print(f'Индекс числа {digit} - {digit_index}')
    print(numbers)
except ValueError:
    print('Введите целое число:')