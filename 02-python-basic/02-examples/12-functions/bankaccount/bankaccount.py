import security
import output
from formatting import format_amount


class BankAccount:
    def __init__(self, iban: str, start_amount: float, pin: int):
        self.__iban = iban
        self.__amount = start_amount
        self.__pin = pin

    def show_credit(self) -> None:
        output.print_operation("Show credit.")
        pin_check_successful = security.check_pin_code(self.__pin)

        if pin_check_successful:
            output.print_status(f"Your balance is {format_amount(self.__amount)}")
        else:
            output.print_error("Access denied! Unfortunately, the PIN was entered incorrectly too often.")

        print()

    def transfer_amount(self, iban_destination_account: str, amount_to_be_transferred: float) -> None:
        output.print_operation("Transfer amount.")
        output.print_status(f"IBAN of the destination account: {iban_destination_account}")
        output.print_status(f"Amount to be transferred: format_amount({amount_to_be_transferred})")

        pin_check_successful = security.check_pin_code(self.__pin)

        if pin_check_successful:
            if amount_to_be_transferred <= self.__amount:
                self.__amount -= amount_to_be_transferred
                output.print_status(f"The amount {format_amount(amount_to_be_transferred)} will be transferred to the "
                                    f"account {iban_destination_account}.")
                output.print_status(f"Your balance is now {format_amount(self.__amount)}")
            else:
                output.print_error("Unfortunately, you do not have enough credit to perform the desired transaction!")
        else:
            output.print_error("Access denied! Unfortunately, the PIN was entered incorrectly too often.")

        print()
