nr_1 = int(input("Please enter a number (step 1 of 2): "))
nr_2 = int(input("Please enter a number (step 2 of 2): "))
operator = input("Please select an operator (+, -, /, or * are allowed): ")

if operator == "+":
    print(f"The result is {nr_1 + nr_2}")
elif operator == "-":
    print(f"The result is {nr_1 - nr_2}")
elif operator == "/":
    print(f"The result is {nr_1 / nr_2}")
elif operator == "*":
    print(f"The result is {nr_1 * nr_2}")
else:
    print("Error: Invalid operator was selected!")
