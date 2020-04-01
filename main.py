# coding: utf-8

"""
author  : Jagepard <jagepard@yandex.ru>
license https://mit-license.org/ MIT
"""

from Item import Item
from Client import Client
from Iterator import Iterator

client = Client()

client.addItemToTheBucket(Item("Колготки", 150, "штопаные"))
client.addItemToTheBucket(Item("Мясо", 250, "тухлое"))
client.addItemToTheBucket(Item("Батон", 40))

employee = Iterator(client.getBucket())

try:
    employee.iterateItems()
except:
    print('An error occured.')
