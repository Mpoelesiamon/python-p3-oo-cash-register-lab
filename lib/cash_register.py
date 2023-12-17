#!/usr/bin/env python3

class CashRegister:
    def __init__(self):
        self.items = []
        self.last_transaction_amount = 0
        self.total_price = 0

    def add_item(self, item, price, quantity=1):
        for _ in range(quantity):
            self.items.append((item, price))
            self.total_price += price
            self.last_transaction_amount = price

    def apply_discount(self, discount_percentage):
        discount = (discount_percentage / 100) * self.total_price
        self.total_price -= discount
        return self.total_price

    def void_last_transaction(self):
        if self.last_transaction_amount != 0:
            self.items.pop()
            self.total_price -= self.last_transaction_amount
            self.last_transaction_amount = 0

# Example usage:
register = CashRegister()
register.add_item("Apple", 2, 3)  # Adding 3 apples at $2 each
register.add_item("Banana", 1.5)  # Adding 1 banana at $1.5
print(register.total_price)  # Output: 7.5

register.apply_discount(10)  # Applying a 10% discount
print(register.total_price)  # Output: 6.75

register.void_last_transaction()  # Voiding the last transaction (banana)
print(register.total_price)  # Output: 5.25
