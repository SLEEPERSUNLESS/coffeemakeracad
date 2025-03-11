from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()

while True:
    choice = input(f"What would you like? ({menu.get_items()}exit): ").lower()

    if choice == "report":
        coffee_maker.report()
        money_machine.report()

    elif choice == "exit":
        print("Shutting down. Have a great day!")
        break

    else:
        drink = menu.find_drink(choice)
        if drink:
            if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
