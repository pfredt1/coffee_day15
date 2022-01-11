from coffee import MENU
from coffee import resources
choice = ""
def get_choice():
    choice = input("What would you like (e/l/c) espresso/latte/cappuccino? ")
    if choice == "off":
        exit()
    else:
        return choice
def check_supplies(choice):

    enough_water = True
    enough_milk = True
    enough_coffee = True
    if resources["water"] >= MENU[choice]["ingredients"]["water"]:
        enough_water = True
    else:
        enough_water = False
        out_of_stuff = "Water\n"
    if resources["milk"] >= MENU[choice]["ingredients"]["milk"]:
        enough_milk = True
    else:
        enough_milk = False
        out_of_stuff += "Milk \n"
    if resources["coffee"] >= MENU[choice]["ingredients"]["coffee"]:
        enough_coffee = True
    else:
        enough_coffee = False
        out_of_stuff += "Coffee \n"
    if enough_water == False or enough_milk == False or enough_milk == False:
        print(f"Sorry we don't have enough \n{out_of_stuff}")
        print(f"To complete your order.")
        return False
    else:
        return True

def make_drink(choice):

    resources["water"] -= MENU[choice]["ingredients"]["water"]
    resources["milk"] -= MENU[choice]["ingredients"]["milk"]
    resources["coffee"] -= MENU[choice]["ingredients"]["coffee"]
    print(f"We hope you enjoy your stupid {choice} have a great day!")

def get_money(choice):

    escrow_bal = float
    escrow_bal = 0.00
    change = float
    change = 0.00
    drink_price = MENU[choice]["cost"]
    while escrow_bal < drink_price:

        print(f"The {choice} has a cost of {drink_price} \n")
        new_money = input("please enter a quarter, dime, nickel or penny")
        if new_money == "off":
            exit()
        if new_money == "quarter":
            escrow_bal += .25
        elif new_money == "dime":
            escrow_bal += .1
        elif new_money == "nickel":
            escrow_bal += .05
        elif new_money == "penny":
            escrow_bal += .01
        print(f" Your balance is now {escrow_bal}")
        if drink_price - escrow_bal > 0:
            print(f" You still need to enter {drink_price - escrow_bal}")

        if escrow_bal > drink_price:
            change = escrow_bal - drink_price
            print(f"your change {change} is being despenced")
    return drink_price
    print(escrow_bal)


new_money = 0.00


while choice != "off":
    choice = get_choice()
    if check_supplies(choice):
        new_money += get_money(choice)
        make_drink(choice)
    print(resources["water"])
    print(f"water {resources['water']}")
    print(f"milk {resources['milk']}")
    print(f"coffee {resources['coffee']}")
    print(f"money in machiene = {new_money}")




## Prompt user by asking What would you like? (espresso/latte/cappuccino):"
# a. Check the user’s input to decide what to do next. done
# b. The prompt should show every time action has completed, e.g. once the drink is
# dispensed. The prompt should show again to serve the next customer.

# Turn off the Coffee Machine by entering  off to the prompt.
# a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off
# the machine. Your code should end execution when this happens.

# Print report.
#  a. When the user enters “report” to the prompt, a report should
#  be generated that shows the current resource values. e.g.
#  Water: 100ml
#  Milk: 50ml
#  Coffee: 76g Money: $2.5

# Check resources sufficient?
# a. When the user chooses a drink, the program should check if there are enough resources to make that drink.
# b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine.
# It should not continue to make the drink but print: Sorry there is not enough water.”
# c. The same should happen if another resource is depleted, e.g. milk or coffee.

# 5. Process coins.
#  a. If there are sufficient resources to make the drink selected,
#  then the program should prompt the user to insert coins.
#  b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
#  c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
#  pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52

# 6. Check transaction successful?
# a. Check that the user has inserted enough money to purchase the drink they selected.
# E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the
# program should say “​Sorry that's not enough money. Money refunded.​”.
#  . But if the user has inserted enough money, then the cost of the drink gets added to the
#  machine as the profit and this will be reflected
#  the next time “report” is triggered. E.g. Water: 100ml
#  Milk: 50ml
#  Coffee: 76g
#  Money: $2.5
#  c. If the user has inserted too much money, the machine should offer change.
#E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal places.

# 7. Make Coffee.
# a. If the transaction is successful and there are enough resources to make
# the drink the user selected, then the ingredients to make the drink should be
# deducted from the coffee machine resources.
#E.g. report before purchasing latte: Water: 300ml
#Milk: 200ml
#Coffee: 100g
#Money: $0
#Report after purchasing latte:
#Water: 100ml Milk: 50ml Coffee: 76g Money: $2.5
#b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”.
# If latte was their choice of drink.



