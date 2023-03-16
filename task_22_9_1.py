def bubble_sort(L): # сортировка методом "всплывающего" пузырька
    for j in range(len(L)):
        for i in range(len(L) - 1):
            if L[i] > L[i + 1]:
                L[i], L[i + 1] = L[i + 1], L[i]
    return L

def binary_search(array, element, left, right): # двоичный поиск индекса определённого элемента в массиве
    if left > right:  # если левая граница превысила правую,
        return False  # значит элемент отсутствует

    middle = (right + left) // 2  # находимо середину
    if array[middle] == element:  # если элемент в середине,
        return middle  # возвращаем этот индекс
    elif element < array[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(array, element, left, middle - 1)
    else:  # иначе в правой
        return binary_search(array, element, middle + 1, right)

while True:
    """ Ввод произвольного массива целых чисел через пробел (больше одного числа), с проверкой ввода.
    """
    try:
        array_numbers = list(map(int, input('Введи массив целых чисел через пробел: ').split()))

        if len(array_numbers) == 1: # ошибка: ввод чисел без пробелов или одного числа
            print('Ошибка, необходимо ввести несколько чисел через пробел')
            continue

    except ValueError: # ошибка: ввод иных символов
        print('Ошибка, необходимо вводить только целые числа:')
    else:
        break

while True:
    """ Ввод произвольного элемента - целого числа, с проверкой ввода.
        """
    try:
        element = int(input('Введи элемент - любое целое число: '))
    except ValueError: # ошибка: ввод иных символов
        print('Ошибка, необходимо ввести целое число:')
    else:
        break

array_numbers.append(element) # вставка элемента в массив

bubble_sort(array_numbers) # сортировка массива

print('Номер позиции элемента в массиве, начиная с ноля -', binary_search(array_numbers, element, 0, len(array_numbers)-1))

"""
Альтернативный код методами python без дополнительных функций bubble_sort, binary_search

array_numbers.append(element) # вставка элемента в массив
array_numbers.sort() # сортировка массива
print('Номер позиции элемента в массиве -',array_numbers.index(element))
"""