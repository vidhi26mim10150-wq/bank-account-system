from .account import BankAccount
from .transaction import Transaction
from .validation import validate_name, validate_account_number, validate_pin, validate_amount
from .storage import save_data, load_data
from .security import authenticate
from .analytics import financial_summary, display_summary

def create_account():
    print("\n========== CREATE ACCOUNT ==========")
    if (existing := load_data()) is not None and existing.get("account"):
        print("An account already exists. This project supports one account.")
        return
    account_number = validate_account_number(input("Enter 10-digit account number: "))
    name = validate_name(input("Enter account holder name: "))
    pin = validate_pin(input("Create 4-digit PIN: "))
    account = BankAccount(account_number, name, pin)
    save_data({
        "account": {
            "account_number": account.account_number,
            "name": account.name,
            "pin": account.pin,
            "balance": account.balance,
        },
        "transactions": [],
    })
    print("\nAccount created successfully!")

def login():
    data = load_data()
    if data is None or not data.get("account"):
        print("\nNo account found. Please create an account first.")
        return None, None
    a = data["account"]
    account = BankAccount(a["account_number"], a["name"], a["pin"], a["balance"])
    if not authenticate(account, input("Enter your PIN: ")):
        print("\nIncorrect PIN.")
        return None, None
    print(f"\nWelcome, {account.name}!")
    return account, data

def update_account_data(account, data):
    data["account"]["balance"] = account.balance
    data["account"]["pin"] = account.pin
    save_data(data)

def deposit(account, data):
    amount = validate_amount(input("Enter deposit amount: ₹"))
    account.deposit(amount)
    data["transactions"].append(Transaction("Deposit", amount, account.balance).to_dict())
    update_account_data(account, data)
    print(f"\n₹{amount:.2f} deposited successfully.")
    print(f"Current balance: ₹{account.balance:.2f}")

def withdraw(account, data):
    amount = validate_amount(input("Enter withdrawal amount: ₹"))
    account.withdraw(amount)
    data["transactions"].append(Transaction("Withdrawal", amount, account.balance).to_dict())
    update_account_data(account, data)
    print(f"\n₹{amount:.2f} withdrawn successfully.")
    print(f"Current balance: ₹{account.balance:.2f}")

def transfer(account, data):
    print("\n========== TRANSFER MONEY ==========")
    receiver = input("Enter receiver name/account number: ").strip()
    if not receiver:
        print("Receiver cannot be empty.")
        return
    amount = validate_amount(input("Enter transfer amount: ₹"))
    account.withdraw(amount)
    data["transactions"].append(
        Transaction("Transfer", amount, account.balance, f"To: {receiver}").to_dict()
    )
    update_account_data(account, data)
    print(f"\n₹{amount:.2f} transferred successfully.")
    print(f"Receiver: {receiver}")
    print(f"Current balance: ₹{account.balance:.2f}")

def show_transactions(data):
    if not data["transactions"]:
        print("\nNo transactions found.")
        return
    print("\n========== TRANSACTION HISTORY ==========")
    for number, t in enumerate(data["transactions"], 1):
        print(f"\nTransaction {number}")
        print(f"Type        : {t['type']}")
        print(f"Amount      : ₹{t['amount']:.2f}")
        print(f"Balance     : ₹{t['balance_after']:.2f}")
        print(f"Description : {t.get('description', '')}")
        print(f"Date        : {t['date']}")

def change_pin(account, data):
    old_pin = input("Enter current PIN: ")
    new_pin = validate_pin(input("Enter new 4-digit PIN: "))
    account.change_pin(old_pin, new_pin)
    update_account_data(account, data)
    print("\nPIN changed successfully.")

def user_menu(account, data):
    while True:
        print("\n======================================")
        print("      PERSONAL BANK ACCOUNT SYSTEM")
        print("======================================")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Transfer Money")
        print("5. Transaction History")
        print("6. Financial Summary")
        print("7. Change PIN")
        print("8. Logout")
        choice = input("\nEnter your choice: ").strip()
        try:
            if choice == "1":
                print(f"\nCurrent Balance: ₹{account.balance:.2f}")
            elif choice == "2":
                deposit(account, data)
            elif choice == "3":
                withdraw(account, data)
            elif choice == "4":
                transfer(account, data)
            elif choice == "5":
                show_transactions(data)
            elif choice == "6":
                display_summary(financial_summary(data["transactions"]), account.balance)
            elif choice == "7":
                change_pin(account, data)
            elif choice == "8":
                print("\nLogged out successfully.")
                break
            else:
                print("\nInvalid choice. Please select 1-8.")
        except ValueError as error:
            print(f"\nError: {error}")

def run():
    while True:
        print("\n======================================")
        print("       PERSONAL BANK MANAGEMENT")
        print("======================================")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")
        choice = input("\nEnter your choice: ").strip()
        try:
            if choice == "1":
                create_account()
            elif choice == "2":
                account, data = login()
                if account is not None:
                    user_menu(account, data)
            elif choice == "3":
                print("\nThank you for using Personal Bank Management System.")
                break
            else:
                print("\nInvalid choice.")
        except ValueError as error:
            print(f"\nError: {error}")
