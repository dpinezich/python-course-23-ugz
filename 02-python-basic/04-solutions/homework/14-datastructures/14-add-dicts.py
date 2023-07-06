def add_dicts(d1, d2):
    result = dict(d2)

    for k_d1, v_d1 in d1.items():
        if k_d1 in result:
            result[k_d1] += v_d1
        else:
            result[k_d1] = v_d1

    return result


print(add_dicts({'a': 100, 'b': 42}, {'b': 200, 'd': 32}))
