def find_first_occurrence(el, lst):
    for i, e in enumerate(lst):
        if e == el:
            return i

    return -1


print(find_first_occurrence("a", ["b", "c", "a"]))
print(find_first_occurrence("z", ["b", "c", "a"]))
