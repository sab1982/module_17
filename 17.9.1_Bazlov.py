# Ввод пользователя последовательность чисел
while True:
    try:
        input_data = list(map(int, input("Введите любую последовательность чисел через пробел: ").split()))
        break
    except ValueError:
        print("Вы ввели не число! Попробуйте заново: ")

# Ввод любого числа пользователем
while True:
    try:
        element = int(input("Введите любое число: "))
        input_data.append(element)  # Добавление числа в список
        break
    except ValueError:
        print("Вы ввели не число! Попробуйте еще раз:")
print(input_data)

# Сортировка списка пузырьковым методом
def bubble_sort(list1):
    for i in range(0, len(list1) - 1):
        for j in range(len(list1) - 1):
            if list1[j] > list1[j + 1]:
                temp = list1[j]
                list1[j] = list1[j + 1]
                list1[j + 1] = temp
    return list1

# Создание переменой с отсортированным списком
sorting = bubble_sort(input_data)
print(sorting)

# Бинарный поиск по индексу
def binary_search(array, position, left, right):
    if left > right:
        return False
    sorting.append(position)
    middle = (left + right) // 2
    if array[middle] == position:
        middle -= 1
        return middle
    elif position <= array[middle]:
        return binary_search(array, position, left, middle - 1)
    else:
        return binary_search(array, position, middle + 1, right)

# Создание переменой с результатом бинарного поиска
element_id = binary_search(sorting, element, -1, len(sorting) - 1)

# Вывод информации на экран
print(f"Номер позиции меньшего элемента: {element_id},")
# print(f"Введенное число: {element},")
print(f"Число меньше введенного числа: {sorting[element_id]}")
print(f"Число больше или равное введенному: {sorting[element_id + 2]}")