#!/usr/bin/env python3

# class CashRegister:
#     def __init__(self, discount=0):
#         self.total = 0
#         self.discount = discount
#         self.items = []

class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.discount = discount
        self.items = []

    def add_item(self, title, price, quantity=1):
        if not isinstance(title, str):
            raise TypeError("Title should be a string")
        if not isinstance(price, (int, float)):
            raise TypeError("Price should be a number")
        if price <= 0:
            raise ValueError("Price should be positive")
        if not isinstance(quantity, int):
            raise TypeError("Quantity should be an integer")
        if quantity < 0:
            raise ValueError("Quantity should be non-negative")
        self.items.append(title)
        self.total += price * quantity

    def apply_discount(self):
        if self.discount == 0:
            print("There is no discount to apply.")
            return
        discount_amount = self.total * self.discount / 100
        self.total -= discount_amount
        print(f"After the discount, the total comes to ${self.total}.")

    def void_last_transaction(self):
        if not self.items:
            print("There are no items to void.")
            return
        last_item = self.items.pop()
        self.total -= self.get_item_price(last_item)

    def get_item_price(self, title):
        for item in self.items:
            if item == title:
                return self.get_item_price(item)
        return 0

    def get_items(self):
        return self.items