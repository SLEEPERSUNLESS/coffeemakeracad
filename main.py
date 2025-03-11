from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

choice = input("What would you like? (espresso/latte/cappuccino): ")
coffee = CoffeeMaker()
menu = Menu()
currency = MoneyMachine()

if choice == "report":
    print(coffee.report())