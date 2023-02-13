__all__ = (
    'even_odd',
)


def even_odd(arr: list[int]) -> float:
    """
    Функция возвращает отношение суммы четных элементов массив к сумме нечетных
    Пример:
    even_odd([1, 2, 3, 4, 5]) == 0.8889
    """
    even = 0
    odd = 0
    for i in arr:
        if i % 2 == 0:
            even += i
        else:
            odd += i
    if not odd:
        return 0
    if not even:
        return 0
    return round(even / odd, 5)
