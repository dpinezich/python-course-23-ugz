MAX_NUMBER_OF_ATTEMPTS = 3


def check_pin_code(pin: int) -> bool:  # -> bool means a boolean return is expected
    """Checks whether the user enters the defined PIN.

    Args:
        pin: PIN of the account.

    Return:
        Returns true if the user has entered the defined PIN correctly
    """
    number_of_attempts = 0

    while number_of_attempts < MAX_NUMBER_OF_ATTEMPTS:
        pin_input = int(input("[SECURITY] Please enter a PIN: "))

        if pin_input == pin:
            return True
        else:
            number_of_attempts += 1
            number_of_remaining_attempts = MAX_NUMBER_OF_ATTEMPTS - number_of_attempts

            if number_of_attempts != MAX_NUMBER_OF_ATTEMPTS:
                print(f"[WARNING] PIN was entered incorrectly. "
                      f"You still have {number_of_remaining_attempts} attempt(s)!")

    return False
