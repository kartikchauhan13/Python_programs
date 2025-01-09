menu  ={"samosa" : 1.00,
        "pizza" : 3.00,
        "burger" : 2.50,
        "cola" : 2.00,
        "popcorn" : 3.00,
        "lemonade" : 1.00,
        "fries" : 2.50
                            }

cart=[]
total =0 

print("------ MENU ------")
for key,value in menu.items():
    print(f"{key:10} : ${value:.2f}")

print("------------------")
while True :
    food = input("Select a food item ( enter q to quit) : ").lower()
    if food.lower() == "q" :
        break
    elif menu.get(food) != None :
        cart.append(food)
print("-----YOUR ORDER----")
for food in cart:
    print(food,end = " ")
    total += menu.get(food)
print()
print(f"Your total : ${total}")