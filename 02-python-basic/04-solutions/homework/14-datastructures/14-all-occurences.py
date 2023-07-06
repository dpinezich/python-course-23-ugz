def find_all(el, lst):
    occurrences = []

    for i, e in enumerate(lst):
        if e == el:
            occurrences.append(i)

    return occurrences


print(find_all("a", ["a", "b", "c", "a", "b", "a"]))
print(find_all("z", ["a", "b"]))
