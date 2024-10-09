"""
Модуль для об'єднання k відсортованих списків у один відсортований список.
"""


from typing import List


def merge(left: List[int], right: List[int]) -> List[int]:
    """
    Допоміжна функція для злиття двох відсортованих списків.

    Args:
        left (List[int]): Лівий відсортований підсписок.
        right (List[int]): Правий відсортований підсписок.

    Returns:
        List[int]: Злитий відсортований список.
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


def merge_k_lists(lists: List[List[int]]) -> List[int]:
    """
    Об'єднує k відсортованих списків у один відсортований список,
    використовуючи рекурсивний підхід.

    Args:
        lists (List[List[int]]): Список відсортованих списків.

    Returns:
        List[int]: Один відсортований список, що містить всі елементи вхідних списків.
    """
    # Базові випадки
    if not lists:
        return []
    if len(lists) == 1:
        return lists[0]
    if len(lists) == 2:
        return merge(lists[0], lists[1])
    
    # Об'єднуємо перші два списки
    merged = merge(lists.pop(0), lists.pop(0))
    # Додаємо об'єднаний список назад до списку списків
    lists.append(merged)
    # Рекурсивно обробляємо оновлений список списків
    return merge_k_lists(lists)


# Тестування
test_cases = [
    ([], []),
    ([[1, 2, 3]], [1, 2, 3]),
    ([[1], [2], [3], [4], [5]], [1, 2, 3, 4, 5]),
    ([[1, 4, 5], [1, 3, 4], [2, 6]], [1, 1, 2, 3, 4, 4, 5, 6]),
    ([[]], []),
    ([[1], [1], [1]], [1, 1, 1]),
    ([[-1, 0, 1], [-2, 2], [-3, 3]], [-3, -2, -1, 0, 1, 2, 3])
]

for i, (input_lists, expected) in enumerate(test_cases):
    result = merge_k_lists(input_lists)
    print(f"Тест {i+1}: {'Пройдено' if result == expected else 'Не пройдено'}")
    print(f"  Вхід: {input_lists}")
    print(f"  Очікувано: {expected}")
    print(f"  Отримано: {result}\n")
