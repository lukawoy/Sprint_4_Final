weights = '1 2 2 1 3 2'
limit = '3'


def main(array_weights: str, weight_limit: str) -> None:
    limit: int = int(weight_limit)
    weights: list[int] = [int(i) for i in array_weights.split()]
    weights.sort()

    num_platforms: int = 0

    l_pointer: int = 0
    r_pointer: int = len(weights)-1

    while l_pointer <= r_pointer:
        sum_weight: int = weights[l_pointer] + weights[r_pointer]

        # Если кол-во элементов нечетное,
        # то в конце алгоритма указатели на одном элементе
        if l_pointer == r_pointer:
            num_platforms += 1
            break

        if sum_weight == 2*limit:
            num_platforms += 2
            l_pointer += 1
            r_pointer -= 1
        elif sum_weight <= limit:
            num_platforms += 1
            l_pointer += 1
            r_pointer -= 1
        elif sum_weight > limit:
            num_platforms += 1
            r_pointer -= 1

    print(num_platforms)


if __name__ == '__main__':
    main(weights, limit)
