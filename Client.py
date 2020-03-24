"""
author  : Jagepard <jagepard@yandex.ru>
license https://mit-license.org/ MIT
"""

class Client:
    bucket = []
    def addItemToTheBucket(self, item):
        self.bucket.append(item);

    def getBucket(self):
        return self.bucket
