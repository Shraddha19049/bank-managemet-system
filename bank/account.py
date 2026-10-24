import random
class Account:
    def __init__(self,name,pin):
        self.account_no=str(random.randint(100000,999999))
        self.name=name
        self.pin=pin
        self.balance=0
        self.transactions=[]
    def deposit(self,amount):
        if amount <= 0:
            print("Invalid Amount")
            return False
        self.balance += amount
        self.transactions.append(f"₹{amount}: deposited")
        return True

    def withdraw(self,amount):
        if amount <= 0:
            print("Invalid Amount")
            return False
        if amount > self.balance:
            print("Insufficient balance")
            return False
        self.balance -= amount
        self.transactions.append(f"₹{amount}: withdrawn")
        return True

    def to_dict(self):
        return {
            "account_no": self.account_no,
            "name": self.name,
            "pin": self.pin,
            "balance": self.balance,
            "transactions": self.transactions
        }

    @classmethod
    def from_dict(cls,data):
        account = cls(data["name"], data["pin"])
        account.account_no = data.get("account_no", data.get("account no"))
        account.balance = data.get("balance", 0)
        account.transactions = data.get("transactions", [])

        return account
        
        