nr_1 = int(input("Please enter a number (step 1 of 3): "))
# The first number we enter is initially the largest number,
# exactly until the moment when a larger number is entered
largest_nr = nr_1

nr_2 = int(input("Please enter a number (step 2 of 3): "))
if nr_2 > largest_nr:
    largest_nr = nr_2

nr_3 = int(input("Please enter a number (step 3 of 3): "))
if nr_3 > largest_nr:
    largest_nr = nr_3

print(f"The largest number you entered is {largest_nr}")


## Alternate solution

# if nr_1 < nr_2:
#     if nr_2 < nr_3:
#         print(nr_3)
#     elif nr_2 > nr_3:
#         print(nr_2)
# else:
#     print(nr_1)