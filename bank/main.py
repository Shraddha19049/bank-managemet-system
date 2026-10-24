from bank import Bank


class Application:

    def __init__(self):
        self.bank = Bank()

    def line(self):
        print("-" * 50)

    def display_menu(self):
        self.line()
        print("BANK MANAGEMENT SYSTEM")
        self.line()
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer")
        print("5. Check Balance")
        print("6. Transaction History")
        print("7. Exit")
        self.line()

    def create_account(self):
        name = input("Enter Name: ")
        pin = input("Create PIN: ")

        self.bank.create_account(name, pin)

    def deposit_money(self):
        account = input("Account Number: ")
        amount = float(input("Amount: "))

        self.bank.deposit(account, amount)

    def withdraw_money(self):
        account = input("Account Number: ")
        amount = float(input("Amount: "))

        self.bank.withdraw(account, amount)

    def transfer_money(self):
        sender = input("Sender Account: ")
        receiver = input("Receiver Account: ")
        amount = float(input("Amount: "))

        self.bank.transfer(sender, receiver, amount)

    def check_balance(self):
        account = input("Account Number: ")

        self.bank.show_balance(account)

    def transaction_history(self):
        account = input("Account Number: ")

        self.bank.show_transactions(account)

    def run(self):

        while True:

            self.display_menu()

            choice = input("Enter Choice: ")

            match choice:

                case "1":
                    self.create_account()

                case "2":
                    self.deposit_money()

                case "3":
                    self.withdraw_money()

                case "4":
                    self.transfer_money()

                case "5":
                    self.check_balance()

                case "6":
                    self.transaction_history()

                case "7":
                    print("Thank you!")
                    break

                case _:
                    print("Invalid Choice")


if __name__ == "__main__":
    app = Application()
    app.run()