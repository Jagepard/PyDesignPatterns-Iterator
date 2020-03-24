"""
author  : Jagepard <jagepard@yandex.ru>
license https://mit-license.org/ MIT
"""

class Iterator:
    def __init__(self, bucket): 
        self.bucket = bucket

    def iterateItems(self):
        for element in self.bucket:
            print(element.getName() + ' ' + str(element.getPrice()) + ' ' + element.getDescription())
