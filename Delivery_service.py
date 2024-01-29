# ID последней посылки 105917914


def get_min_number_platforms(array_weights: str, weight_limit: str) -> int:
    """Алгоритм определяет минимальное количество транспортных платформ,
необходимое для перевозки всех роботов, описанных в массиве array_weights.
- Количество платформ неограниченно.
- Каждая платформа выдерживает максимальный вес weight_limit.
- На каждой платформе можно перевезти не более двух роботов при условии,
что их совокупный вес не превышает weight_limit.
- Вес отдельного робота не может превышать weight_limit.
"""
    limit: int = int(weight_limit)
    weights: list[int] = [int(weight) for weight in array_weights.split()]
    weights.sort()

    num_platforms: int = 0

    l_pointer: int = 0
    r_pointer: int = len(weights)-1

    while l_pointer <= r_pointer:
        if weights[l_pointer] + weights[r_pointer] <= limit:
            l_pointer += 1

        num_platforms += 1
        r_pointer -= 1

    return num_platforms


if __name__ == '__main__':
    print(get_min_number_platforms(input(), input()))
