def print_animals(*animals):
    for a in animals:
        print(a)

def print_human_details(name, eyecolor, haircolor, height=170, weight=65):
    print("Details: Name", name, "eyecolor", eyecolor, "haircolor", haircolor, "height", height, "weight", weight)


print_animals("Bill", "Tom")
print_human_details("David", "Brown", "Brown", 171)