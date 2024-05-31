
#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount = 0, total = 0):
        self.discount = discount
        self.total = total
        self.items = []
        self._prices = []
    
    def add_item(self, title, price, quantity = 1):
        self.total += (price * quantity)
        self._prices.append(price * quantity)
        for _ in range(quantity):
            self.items.append(title)
        return self.items
    
    def apply_discount(self):
        if self.discount == 0:
           print ("There is no discount to apply.")
        else:   
          discount = self.discount / 100 * self.total
          discount_amount = self.total - discount
          self.total = discount_amount
          print(f"After the discount, the total comes to ${int(discount_amount)}.")
          return discount_amount
    
    def void_last_transaction(self):
        length_of_prices_array = len(self._prices)
        access_last_price = self._prices[length_of_prices_array - 1]
        self.total -= access_last_price

