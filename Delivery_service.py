weights = '1 2 2 1 3 2'
limit = '3'


def main(weights: str, limit: str) -> None:
    limit = int(limit)
    weights = [int(i) for i in weights.split()]
    weights.sort()
    num_platforms = 0
    l_pointer = 0
    r_pointer = len(weights)-1

    while l_pointer <= r_pointer:
        sum_weight = weights[l_pointer] + weights[r_pointer]

        if l_pointer == r_pointer:
            num_platforms += 1
            break

        if sum_weight == 2*limit:
            num_platforms += 2
            l_pointer += 1
            r_pointer -= 1

        if sum_weight <= limit:
            num_platforms += 1
            l_pointer += 1
            r_pointer -= 1

        if sum_weight > limit and sum_weight < 2*limit:
            num_platforms += 1
            r_pointer -= 1

    print(num_platforms)


if __name__ == '__main__':
    main(weights, limit)
