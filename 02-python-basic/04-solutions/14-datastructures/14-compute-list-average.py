def compute_list_average(lst):
    result = 0
    for el in lst:
        result += el

    return result / len(lst)


print(compute_list_average([1, 2, 3]))
