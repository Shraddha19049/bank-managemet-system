from account import Account
from storage import Storage
class Bank:
    def __init__(self):
        self.storage=Storage()
        self.accounts=self.storage.load_accounts()
    
    def create_account(self,user_name,pin):
        account=Account(user_name,pin)
        self.accounts.append(account)
        self.storage.save_accounts(self.accounts)
        print("Account is Created!")
        print(f"Your Account no is: {account.account_no}")

    def find_account(self,account_no):
        for account in self.accounts:
            if account.account_no == account_no:
                return account

        return None

    def deposit(self,account_number,amount):
        account = self.find_account(account_number)
        if account is None:
            print("account not found")
            return
        if account.deposit(amount):
            self.storage.save_accounts(self.accounts)
            print("Deposit successful")

    def withdraw(self,account_number,amount):
        account = self.find_account(account_number)
        if account is None:
            print("account is not found")
            return
        if account.withdraw(amount):
            self.storage.save_accounts(self.accounts)
            print("Withdraw successful")
    
    def transfer(self,sender_acc,receiver_acc,amount):
        sender = self.find_account(sender_acc)
        receiver = self.find_account(receiver_acc)

        if sender is None or receiver is None:
            print("Invalid account number")
            return
        if amount <= 0:
            print("Invalid amount")
            return
        if sender.withdraw(amount):
            receiver.deposit(amount)
            self.storage.save_accounts(self.accounts)
            print("Amount transferred successfully!")
        else:
            print("Transfer failed")

    def show_balance(self,account_number):
        account=self.find_account(account_number)
        if account is None:
            print("account not found!")
            return
        print(f"current balance: ₹{account.balance}")
    
    def show_transactions(self,account_number):
        account = self.find_account(account_number)
        if account is None:
            print("account not found")
            return
        print("\nTransaction History\n")
        if not account.transactions:
            print("No transactions found")
            return
        for transaction in account.transactions:
            print(transaction)


            
    