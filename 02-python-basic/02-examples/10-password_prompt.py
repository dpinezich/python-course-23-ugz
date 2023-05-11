PASSWORD = "test123"
MAX_NUMBER_OF_TRIES = 3

password_successfully_entered = False
number_of_tries = 0

while number_of_tries < MAX_NUMBER_OF_TRIES:
	password_input = input("Please enter your password: ")

	if password_input == PASSWORD:
		print("Password is correct. Welcome to our site!")
		password_successfully_entered = True
		break
	else: 
		number_of_tries += 1
		number_of_remaining_attempts = MAX_NUMBER_OF_TRIES - number_of_tries

		if number_of_tries != MAX_NUMBER_OF_TRIES:
			print(f"Password was entered incorrectly. You still have {number_of_remaining_attempts} attempt(s)!!")

if not password_successfully_entered:
	print("Password was entered incorrectly too often. Access denied!")
