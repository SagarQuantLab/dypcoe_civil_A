class Bank:

    def __init__(self):
        self.account_details = {}

    def open_account(self, account_number, user_details):
        if self.check_for_existence(account_number):
            self.account_details[account_number] = user_details
            return f"Account open for - {user_details['Name']} - {account_number}"
        else:
            raise ValueError("Account number already exists")
    
    def check_for_existence(self, account_number):
        account_list = list(self.account_details.keys())
        status = True
        if account_number in account_list:
            status = False

        return status