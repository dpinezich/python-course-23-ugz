def count_occurrences(el, lst):
    nr_occurrences = 0

    for i, e in enumerate(lst):
        if e == el:
            nr_occurrences += 1

    return nr_occurrences


print(count_occurrences("a", ["a", "b", "c", "a", "a"]))
print(count_occurrences("z", ["a", "b", "c"]))
