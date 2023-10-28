import sys
from Account import Account

def print_header(text):
    print("=" * len(text))
    print(text)
    print("=" * len(text))

def create_account_ui():
    print_header("Create an Account")
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    email = input("Email: ")
    password = input("Password: ")
    account = Account(first_name, last_name, email, password)
    return account

def check_credentials_ui(account):
    print_header("New Account")
    print(f"Name: {account.firstName} {account.lastName}")
    print(f"Email: {account.email}")
    print(f"Password: {'*' * len(account.password)}")
    print("\nCredentials check...")
    while True:
        answer = input("Are your credentials correct? (Y/N): ").strip().lower()
        if answer in ["y", "yes"]:
            check_answer(answer, account)
            return True
        elif answer in ["n", "no"]:
            return False
        else:
            print("Invalid input. Please enter 'Y' for (YES) or 'N' for (NO).")

def check_answer(answer, account):
    if answer:
        save_account_to_file(account)
        print("NEW ACCOUNT CREATED!")
    else:
        credentials_ui()

def save_account_to_file(account):
    with open("accounts.txt", "a") as file:
        file.write(f"{account.firstName},{account.lastName},{account.email},{account.password}\n")

def credentials_ui():
    account = create_account_ui()
    if check_credentials_ui(account):
        return account
    else:
        return None

def login_ui():
    print_header("Login")
    while True:
        email = input("Email: ")
        password = input("Password: ")

        with open("accounts.txt", "r") as file:
            lines = file.readlines()

        for line in lines:
            fields = line.strip().split(",")
            if len(fields) == 4:
                first_name, last_name, saved_email, saved_password = fields
                if saved_email == email and saved_password == password:
                    return Account(first_name, last_name, saved_email, saved_password)

        print("Invalid email or password. Please try again.")

def main_ui():
    while True:
        print_header("Welcome to the Login System")
        print("1. Register a New Account")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            account = credentials_ui()
            if account:
                print("You are now registered.")
        elif choice == "2":
            account = login_ui()
            if account:
                print("You are now logged in.")
                sys.exit(0)  # Exit when the user is logged in
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main_ui()
