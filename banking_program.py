def show_balance(balance):
    print(f"Your current balance is: ${balance:.2f}")

def deposit():
    amount = float(input("Enter the amount to deposit: "))
    if amount < 0:
        print("Invalid amount. Please enter a positive number.")
        return 0
    else:
        return amount

def withdraw(balance):
    amount = float(input("Enter the amount to withdraw: "))
    if amount < 0:
        print("Invalid amount. Please enter a positive number.")
        return 0
    elif amount > balance:
        print("Insufficient funds.")
        return 0
    else:
        return amount

def main():
    balance = 0
    is_running = True
    while is_running:
        print("Banking Program")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance += deposit()
            print(f"Deposit successful. Your new balance is: ${balance:.2f}")
        elif choice == "3":
            balance -= withdraw(balance)
            print(f"Withdrawal successful. Your new balance is: ${balance:.2f}")
        elif choice == "4":
            is_running = False
            print("Thank you for using the banking program.")
        else:
            print("Invalid choice. Please try again.")
        
if __name__ =="__main__":
    main()