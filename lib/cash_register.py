#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []

    def add_item(self, title, price, quantity=1):
        self.total += price * quantity
        self.items.extend([title] * quantity)

    def apply_discount(self):
        if self.discount == 0:
            print("There is no discount to apply.")
        else:
            discount_amount = self.total * (self.discount / 100)
            self.total -= discount_amount
            print(f"After the discount, the total comes to ${int(self.total)}.")

    def void_last_transaction(self, price):
        if self.items:
            last_item_price = self.total - (self.items.count(self.items[-1]) * price)  # Use the correct price here
            self.total = last_item_price if last_item_price >= 0 else 0

    def reset_register_totals(self):
        self.total = 0
        self.items = []