from Account import Account

actIns = Account()
account_holder_details = {'Name':'Rajveer', 'Age':21, 'Gender':'Male', 'Account_type':'Savings', 'Balance':10000}
account_number = 123456789
print(actIns.open_account(account_number, account_holder_details))
account_holder_details = {'Name':'Rohan', 'Age':20, 'Gender':'Male', 'Account_type':'Current', 'Balance':5000}
account_number = 123456788
print(actIns.open_account(account_number, account_holder_details))
print(actIns.account_details)

print(actIns.deposit(123456789, 5000))
print(actIns.deposit(123456788, 5000))

