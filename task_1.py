"""
Модуль містить реалізації різних алгоритмів сортування (сортування вставками, 
сортування злиттям) та функцію для порівняння їх продуктивності з вбудованим 
алгоритмом Timsort (використовується в Python для методів sorted() та list.sort()).

Модуль дозволяє генерувати випадкові списки різних розмірів та вимірювати час 
виконання кожного алгоритму сортування на цих списках. Результати виводяться 
у вигляді таблиці для зручного порівняння.

Для використання цього модуля потрібно встановити бібліотеку prettytable:
pip install prettytable

Приклад використання:
python task_4.py
"""


import timeit
import random
from prettytable import PrettyTable


def insertion_sort(lst: list) -> list:
    """
    Реалізує алгоритм сортування вставками.

    Args:
        lst (list): Вхідний список для сортування.

    Returns:
        list: Відсортований список.
    """
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        # Зсуваємо елементи більші за key на одну позицію вперед
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst

def merge_sort(arr: list) -> list:
    """
    Реалізує алгоритм сортування злиттям.

    Args:
        arr (list): Вхідний список для сортування.

    Returns:
        list: Відсортований список.
    """
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left: list, right: list) -> list:
    """
    Допоміжна функція для злиття двох відсортованих списків.

    Args:
        left (list): Лівий відсортований підсписок.
        right (list): Правий відсортований підсписок.

    Returns:
        list: Злитий відсортований список.
    """
    merged = []
    left_index = right_index = 0

    # Порівнюємо елементи з обох списків
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Додаємо залишки елементів, якщо такі є
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    return merged

def generate_random_list(size: int) -> list:
    """
    Генерує список випадкових чисел заданого розміру.

    Args:
        size (int): Розмір списку.

    Returns:
        list: Список випадкових чисел.
    """
    return [random.randint(1, 1000) for _ in range(size)]

def compare_sorting_algorithms(n: list) -> None:
    """
    Порівнює алгоритми сортування на різних розмірах вхідних даних
    і виводить результати у вигляді таблиці.

    Args:
        n (list): Список розмірів вхідних даних для тестування.
    """
    table = PrettyTable()
    table.field_names = ["Розмір списку", "Insertion Sort (с)", "Merge Sort (с)", "Timsort (с)"]

    for size in n:
        data = generate_random_list(size)

        insertion_time = timeit.timeit(lambda: insertion_sort(data.copy()), number=1)
        merge_time = timeit.timeit(lambda: merge_sort(data.copy()), number=1)
        timsort_time = timeit.timeit(lambda: sorted(data.copy()), number=1)

        table.add_row([size, f"{insertion_time:.6f}", f"{merge_time:.6f}", f"{timsort_time:.6f}"])

    print(table)


# Тестування алгоритмів
sizes = [100, 1000, 10000, 100000]
compare_sorting_algorithms(sizes)
