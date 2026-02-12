import random  as r

class Bank:
    def __init__(self):
        self.name = None
        self.account_number = None
        self.balance = 0.0
        self.account_created = False

    def create_account(self):
        self.name = input("Enter your name: ")
        self.account_number = r.randint(111111, 999999)
        self.balance = 0.0
        self.account_created = True
        print("\nAccount successfully created!")
        print(f"Name: {self.name}")
        print(f"Account Number: {self.account_number}")

    def deposit(self):
        if not self.account_created:
            print("Please create an account first.")
            return
        try:
            amount = float(input("Enter amount to deposit: "))
            if amount > 0:
                self.balance += amount
                print(f"\nSuccessfully deposited Rs. {amount:.2f}")
                self.display_account_info()
            else:
                print("Invalid amount. Please enter a positive value.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    def withdraw(self):
        if not self.account_created:
            print("Please create an account first.")
            return
        try:
            amount = float(input("Enter amount to withdraw: "))
            if amount <= 0:
                print("Invalid amount. Please enter a positive value.")
            elif amount > self.balance:
                print("Insufficient balance.")
                self.display_account_info()
            else:
                self.balance -= amount
                print("Withdrawal successful!")
                print("Do you want to print a voucher?")
                print("1. Yes")
                print("2. No")
                voucher_choice = input("Enter 1 or 2: ").strip()
                if voucher_choice == '1':
                    print("\n===== Withdrawal Voucher =====")
                    print(f"Name: {self.name}")
                    print(f"Account Number: {self.account_number}")
                    print(f"Withdrawn Amount: Rs. {amount:.3f}")
                    print(f"remaining balance is:{self.balance:.3f}")
                    print("Thank you for banking with us.")
                elif voucher_choice == '2':
                    print("You chose not to print a voucher. Thank you!")
                else:
                    print("Invalid choice. Skipping voucher.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    def check_balance(self):
        if not self.account_created:
            print("Please create an account first.")
            return
        self.display_account_info()
        print(f"Current Balance: Rs. {self.balance:.3f}")

    def display_account_info(self):
        print(f"\nAccount Holder: {self.name}")
        print(f"Account Number: {self.account_number}")

def main():
    bank = Bank()
    while True:
        print("\n<======= Apna Bank Menu =======>")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Exit")
        try:
            choice = int(input("Choose an option (1-5): "))
            match choice:
                case 1:
                    bank.create_account()
                case 2:
                    bank.deposit()
                case 3:
                    bank.withdraw()
                case 4:
                    bank.check_balance()
                case 5:
                    print("Thank you for using Apna Bank. Goodbye!")
                    break
                case _:
                    print("Invalid option. Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number.")
main()