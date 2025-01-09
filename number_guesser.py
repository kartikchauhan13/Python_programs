import random

low =0
high=100
number = random.randint(low,high)

guesses=0

print("Number Guessing game")
while True:
    guess =int(input(f"Enter a number between {low} - {high} :"))
    if guess < number:
        print(f"{guess} is too low")
        guesses+=1
    elif guess > number :
        print(f"{guess} is too high")
        guesses+=1
    else :
        print(f"{guess} is correct")
        break
print(f"This round took you {guesses} guesses ")