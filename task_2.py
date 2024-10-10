"""
Задача 2
Дан массив целых чисел. Нужно удалить из него нули. Можно использовать только O(1) дополнительной памяти.
"""


def remove_zeros(array):
    write_index = 0
    for read_index in range(len(array)):
        if array[read_index] != 0:
            array[write_index] = array[read_index]
            write_index += 1
    del array[write_index:]
    return array


array = [0, 7, 0, 0, 1, 1, 3, 2, 1, 8, -4, 0, 7]
remove_zeros(array)
print(array)


"""
Объяснение:
Изменения производятся непосредственно в исходном массиве без использования дополнительных структур данных.
Время О(N)
Память О(1)
"""