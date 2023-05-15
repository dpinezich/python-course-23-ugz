from bankaccount import BankAccount

mrx_bank_account = BankAccount(iban="CH21412312", start_amount=1000.50, pin=123456)

mrx_bank_account.show_credit()

mrx_bank_account.transfer_amount("CH142130123", amount_to_be_transferred=500.0)

mrx_bank_account.transfer_amount("CH883934933", amount_to_be_transferred=500.50)

mrx_bank_account.transfer_amount("CH125903493", amount_to_be_transferred=10.25)

mrx_bank_account.show_credit()
