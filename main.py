from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()

is_on = True

while is_on:
    choice = input(f"What would you like? {menu.get_items()}: ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(coffee_maker.report())
        print(money_machine.report())
    else:
       drink = menu.find_drink(order_name=choice)
       """need to verify that line 20 properly checks resources"""
       if coffee_maker.is_resource_sufficient(drink):
           if money_machine.make_payment(drink.cost):
               coffee_maker.make_coffee(drink)


