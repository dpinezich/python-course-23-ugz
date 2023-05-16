def elemwise_sum(lst1, lst2):
    if len(lst1) != len(lst2):
        # See https://docs.python.org/3/tutorial/errors.html#exceptions
        raise ValueError("Both lists should have the same number of elements")

    result = []

    for i, e in enumerate(lst1):
        result.append(e + lst2[i])

    return result


print(elemwise_sum([1, 2, 10], [3, 4, 40]))
