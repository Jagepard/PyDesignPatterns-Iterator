"""
author  : Jagepard <jagepard@yandex.ru>
license https://mit-license.org/ MIT
"""

class Item:
    name = ""
    price = 0
    description = ""

    def __init__(self, name, price, description = ""): 
        self.name = name
        self.price = price
        self.description = description

    def getName(self):
        return self.name

    def getPrice(self):
        return self.price

    def getDescription(self):
        return self.description
