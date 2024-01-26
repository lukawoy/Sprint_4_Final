# ID последней посылки 105917914


def get_min_number_platforms(array_weights: str, weight_limit: str) -> int:
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
    weights = input()
    limit = input()
    print(get_min_number_platforms(weights, limit))
