def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # store positives in cache
    cache = {}
    result = []
    for i in a:
        # 0 has no negative
        # abs returns absolute of number
        if i == abs(i) and i != 0:
            # key: -
            # value: +
            cache[-i] = i

    # if negative in list
    for i in a:
        if i in cache:
            result.append(cache[i])

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
