from abc import ABC, abstractmethod


# ---------------- ABSTRACT CLASS ----------------
class Account(ABC):

    def __init__(self, name, acc_no, pin, balance):
        self.name = name
        self.acc_no = acc_no
        self.__pin = pin              # ---------- ENCAPSULATION
        self.__balance = balance      # ---------ENCAPSULATION
        self.history = []             # --------Transaction History

    # PIN Check
    def verify_pin(self, pin):
        return self.__pin == pin

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):

        if amount > 0:
            self.__balance += amount
            self.history.append(f"+{amount} Deposit")
            print("Deposit Successful!")
        else:
            print("Invalid Amount")

    def withdraw(self, amount):

        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self.history.append(f"-{amount} Withdraw")
            print("Withdrawal Successful!")
        else:
            print("Insufficient Balance")

    def show_history(self):

        if not self.history:
            print("No Transactions Yet")
        else:
            print("\n--- Transaction History ---")
            for i, t in enumerate(self.history, 1):
                print(i, t)

    @abstractmethod
    def calculate_interest(self):
        pass

    def display(self):

        print("\n------ Account Details ------")
        print("Name:", self.name)
        print("Account No:", self.acc_no)
        print("Balance:", self.get_balance())


# ---------------- INHERITANCE ----------------
class SavingsAccount(Account):

    def calculate_interest(self):

        interest = self.get_balance() * 0.04
        print("Savings Interest:", interest)


class CurrentAccount(Account):

    def calculate_interest(self):

        print("Current Account does not provide interest.")


# ---------------- BANK CLASS ----------------
class Bank:

    def __init__(self):

        self.accounts = {}
        self.next_acc_no = 1001

    def generate_acc_no(self):

        acc = self.next_acc_no
        self.next_acc_no += 1
        return acc

    def create_account(self):

        print("\n--- Open New Account ---")

        name = input("Enter Name: ")

        pin = input("Set 4 Digit PIN: ")

        if len(pin) != 4 or not pin.isdigit():
            print("PIN must be 4 digits")
            return

        balance = float(input("Enter Initial Balance (>=500): "))

        if balance < 500:
            print("Minimum balance is 500")
            return

        print("\n1. Savings Account")
        print("2. Current Account")

        choice = int(input("Choose Type: "))

        acc_no = self.generate_acc_no()

        if choice == 1:
            acc = SavingsAccount(name, acc_no, pin, balance)

        elif choice == 2:
            acc = CurrentAccount(name, acc_no, pin, balance)

        else:
            print("Invalid Choice")
            return

        self.accounts[acc_no] = acc

        print("\nAccount Created Successfully!")
        print("Your Account Number:", acc_no)

    def login(self):

        acc_no = int(input("Enter Account Number: "))
        pin = input("Enter PIN: ")

        acc = self.accounts.get(acc_no)

        if acc and acc.verify_pin(pin):
            print("\nLogin Successful!")
            return acc

        else:
            print("Invalid Login")
            return None


# ---------------- MAIN PROGRAM ----------------
bank = Bank()

while True:

    print("\n-------------BANK MANAGEMENT SYSTEM-----------")
    print("1. Open Account")
    print("2. Login")
    print("3. Exit")

    ch = int(input("Enter Choice: "))

    if ch == 1:
        bank.create_account()

    elif ch == 2:

        user = bank.login()

        if user:

            while True:

                print("\n--- USER MENU ---")
                print("1. Deposit")
                print("2. Withdraw")
                print("3. Check Balance")
                print("4. View Details")
                print("5. Transaction History")
                print("6. Interest")
                print("7. Logout")

                opt = int(input("Enter Choice: "))

                if opt == 1:
                    amt = float(input("Enter Amount: "))
                    user.deposit(amt)

                elif opt == 2:
                    amt = float(input("Enter Amount: "))
                    user.withdraw(amt)

                elif opt == 3:
                    print("Balance:", user.get_balance())

                elif opt == 4:
                    user.display()

                elif opt == 5:
                    user.show_history()

                elif opt == 6:
                    user.calculate_interest()  # POLYMORPHISM

                elif opt == 7:
                    print("Logged Out")
                    break

                else:
                    print("Invalid Option")

    elif ch == 3:
        print("Thank You for Using Bank System!")
        break

    else:
        print("Invalid Choice")
