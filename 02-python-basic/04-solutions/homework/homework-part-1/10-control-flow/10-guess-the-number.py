#import random
#number_to_be_guessed = random.randint(1, 10)


print("Guessing game: try to guess the number (the number is between 1 and 10)")

while True:
    suggested_number = int(input("Your suggestion: "))

    if suggested_number > number_to_be_guessed:
        print(f"Almost! The number to be guessed is smaller than {suggested_number}")
    elif suggested_number < number_to_be_guessed:
        print(f"Almost! The number to be guessed is greater than {suggested_number}")
    else:
        print(f"Congratulations! You guessed the number!")
        break