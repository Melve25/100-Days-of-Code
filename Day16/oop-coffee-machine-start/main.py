from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
maker = CoffeeMaker()
money = MoneyMachine()

# TODO: print report
maker.report()
print()
# TODO: check resources sufficient?
print(f"Here is menu: {menu.get_items()}")

drink = input("Write what do you want: ")

if menu.find_drink(drink):
    checkSufficient = maker.is_resource_sufficient(menu.find_drink(drink))
# TODO: Process coins
    transaction = money.make_payment(menu.find_drink(drink).cost)
# TODO: check transaction successful
    if transaction:
        money.report()
# TODO: Make coffee
        maker.make_coffee(menu.find_drink(drink))

