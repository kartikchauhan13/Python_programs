import random
import time

def spin_row():
    symbols = ['🍒','🍉','🍋','🔔','⭐']
    result =[]
    for symbol in range(3):
        result.append(random.choice(symbols))
    return result

def print_row(row):
    print("***********************")
    print("|".join(row))
    print("***********************")

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0]=='🍒':
            return bet*3
        elif row[0] == '🍉':
            return bet*5
        elif row[0] == '🍋':
            return bet*7
        elif row[0] == '🔔':
            return bet*10
        elif row[0] == '⭐':
            return bet*20
    return 0

def main():
    balance = 100

    print("*************************")
    print("Welcome to Python Slots ")
    print("Symbols: 🍒 🍉 🍋 🔔 ⭐")
    print("*************************")

    while balance > 0:
        print(f"Current Balance : ${balance}")

        bet = input("Enter your bet in $ : ")

        if not bet.isdigit():
            print("Invalid bet. Please enter a number.")
            continue
        bet = int(bet)
        if bet > balance:
            print("Insufficient funds.")
            continue
        if bet<= 0:
            print("Invalid bet. Please enter a positive number.")
            continue

        balance -= bet
        row = spin_row()
        print("Spinning 💫💫💫💫💫.....")
        time.sleep(2)
        print_row(row)

        payout = get_payout(row, bet)
        if payout > 0:
            print(f"Congratulations! You won ${payout}")
        else:
            print("Sorry, you lost your bet.")
        
        balance += payout
        print("==========================")
        print(f"Your new balance is ${balance:.2f} ")
        print("==========================")
        choice = input("Do you want to continue playing (Y/N) : ")
        if choice.lower()!= 'y':
            break
    print(f"Your final balance is : ${balance:.2f}")
    print("Thanks for playing! Goodbye.")

if __name__ == "__main__":
    main()

