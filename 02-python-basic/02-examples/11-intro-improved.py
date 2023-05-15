error = 1

# retry if wrong
while error == 1:
    print("Please enter a number")
    z = input()

    # casting
    try:
        num = int(z)
        print("You have entered the number", num, "correctly")
        error = 0

    except:
        print("You have not entered the number correct")