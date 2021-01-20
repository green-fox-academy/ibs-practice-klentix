
accounts = [
	{ 'client_name': 'Igor', 'account_number': 11234543, 'balance': 203004099.2 },
	{ 'client_name': 'Vladimir', 'account_number': 43546731, 'balance': 5204100071.23 },
	{ 'client_name': 'Sergei', 'account_number': 23456311, 'balance': 1353600.0 }
]

# Create function that returns the name and balance of cash on an account in a list
#get_name_and_balance(accounts, 11234543)
# The output should be: "Igor", "203004099.2"

def get_name_and_balance(accounts,s):
    for account in accounts:
        if account['account_number'] == s:
            print(account['client_name'], account['balance'])

get_name_and_balance(accounts,11234543)

# Create function that transfers an amount of cash from one account to another
# it should have three parameters:
#
#  - from account_number
#  - to account_number
#  - amount to transfer
#
# Print "404 - account not found" if any of the account numbers don't exist

#transfer_amount(43546731, 23456311, 500.0)
#After printing the "accounts" it should look like:
# accounts = [
#	{ 'client_name': 'Igor', 'account_number': 11234543, 'balance': 203004099.2 },
#	{ 'client_name': 'Vladimir', 'account_number': 43546731, 'balance': 5204099571.23 },
#	{ 'client_name': 'Sergei', 'account_number': 23456311, 'balance': 1354100.0 }
#]

def transfer_amount(account_from,account_to,amount):
    account_number = []
    for account in accounts:
        account_number.append(account['account_number'])
        #print(account_number)
    if account_from not in account_number or account_to not in account_number:
        print("404 - account not found")
    else:
        for account in accounts:
            if account['account_number'] == account_from:
                account['balance'] -= amount
            elif account['account_number'] == account_to:
                account['balance'] += amount
        print(accounts)

transfer_amount(43546731, 23456311, 500.0)