array = input("Введите последовательность чисел через пробел: ")
array_list = [int(a) for a in array.split()]

num = int(input("Введите любое число: "))
if num % 1 == 0:
    array_list.append(num)
    print("Список до сортировки: ", array_list)

def my_sort(array_list):
    for i in range(len(array_list)):  # проходим по всему массиву
        idx_min = i  # сохраняем индекс предположительно минимального элемента
        for j in range(i, len(array_list)):
            if array_list[j] < array_list[idx_min]:
                idx_min = j
        if i != idx_min:  # если индекс не совпадает с минимальным, меняем
            array_list[i], array_list[idx_min] = array_list[idx_min], array_list[i]
    return array_list

print("Список после сортировки:", my_sort(array_list))


