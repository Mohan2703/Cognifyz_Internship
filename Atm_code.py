from datetime import datetime

class ATMMachine:
    def __init__(self, initial_pin="1234", initial_balance=0):
        """
        Initialize the ATM machine with an initial PIN and balance.
        
        Parameters:
        initial_pin (str): The default PIN for the account.
        initial_balance (float): The starting balance in the account.
        """
        self.pin = initial_pin
        self.balance = initial_balance
        self.transaction_history = []

    def check_pin(self, entered_pin):
        """Check if the entered PIN matches the account PIN."""
        return entered_pin == self.pin

    def display_balance(self):
        """Display the current account balance."""
        return f"Your current balance is: Rs.{self.balance:.2f}"

    def withdraw_cash(self, amount):
        """Withdraw a specified amount from the account if sufficient balance exists."""
        if amount <= 0:
            return "Invalid withdrawal amount."
        elif amount > self.balance:
            return "Insufficient balance."
        else:
            self.balance -= amount
            transaction_time = datetime.now().strftime("%Y-%m-%d")
            self.transaction_history.append((transaction_time, f"Withdrawn: Rs.{amount:.2f}"))
            return f"Successfully withdrawn: Rs.{amount:.2f}"

    def deposit_cash(self, amount):
        """Deposit a specified amount into the account."""
        if amount <= 0:
            return "Invalid deposit amount."
        else:
            self.balance += amount
            transaction_time = datetime.now().strftime("%Y-%m-%d")
            self.transaction_history.append((transaction_time, f"Deposited: Rs.{amount:.2f}"))
            return f"Successfully deposited: Rs.{amount:.2f}"

    def change_pin(self, old_pin, new_pin):
        """Change the account PIN if the old PIN matches the current PIN."""
        if self.check_pin(old_pin):
            if len(new_pin) == 4 and new_pin.isdigit():
                self.pin = new_pin
                transaction_time = datetime.now().strftime("%Y-%m-%d")
                self.transaction_history.append((transaction_time, "PIN changed successfully."))
                return "PIN changed successfully."
            else:
                return "New PIN must be a 4-digit number."
        else:
            return "Incorrect old PIN."

    def get_transaction_history(self):
        """Display the transaction history of the account in a table format."""
        if not self.transaction_history:
            return "No transactions yet."

        # Create a formatted string for the transaction history
        history_table = "Date\t\tTransaction\n"
        history_table += "-" * 50 + "\n"
        for transaction in self.transaction_history:
            date, details = transaction
            history_table += f"{date}\t{details}\n"
        
        return history_table


def main():
    atm = ATMMachine()
    print("Welcome to the ATM!")

    while True:
        print("\nSelect an option:")
        print("1. Check Balance")
        print("2. Withdraw Cash")
        print("3. Deposit Cash")
        print("4. Change PIN")
        print("5. View Transaction History")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            entered_pin = input("Enter your PIN: ")
            if atm.check_pin(entered_pin):
                print(atm.display_balance())
            else:
                print("Incorrect PIN.")

        elif choice == "2":
            entered_pin = input("Enter your PIN: ")
            if atm.check_pin(entered_pin):
                amount = input("Enter amount to withdraw: ")
                try:
                    amount = float(amount)
                    print(atm.withdraw_cash(amount))
                except ValueError:
                    print("Invalid input. Please enter a numeric value.")
            else:
                print("Incorrect PIN.")

        elif choice == "3":
            entered_pin = input("Enter your PIN: ")
            if atm.check_pin(entered_pin):
                amount = input("Enter amount to deposit: ")
                try:
                    amount = float(amount)
                    print(atm.deposit_cash(amount))
                except ValueError:
                    print("Invalid input. Please enter a numeric value.")
            else:
                print("Incorrect PIN.")

        elif choice == "4":
            old_pin = input("Enter your old PIN: ")
            new_pin = input("Enter your new PIN (4 digits): ")
            print(atm.change_pin(old_pin, new_pin))

        elif choice == "5":
            entered_pin = input("Enter your PIN: ")
            if atm.check_pin(entered_pin):
                print("\nTransaction History:")
                print(atm.get_transaction_history())
            else:
                print("Incorrect PIN.")

        elif choice == "6":
            print("Thank you for using the ATM!")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
