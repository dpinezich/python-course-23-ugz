def create_dict(keys, values):
    if len(keys) != len(values):
        # See https://docs.python.org/3/tutorial/errors.html#exceptions
        raise ValueError("Both lists should have the same number of elements")

    dictionary = {}

    for i, key in enumerate(keys):
        dictionary[key] = values[i]

    return dictionary


print(create_dict(['a', 'b'], [100, 200]))
