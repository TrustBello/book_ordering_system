import sys
import os

# Add the project root directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from core.product import Product


class Stock(Product):
    def __init__(self, name: str, author: str, price: float):
        super().__init__(name, price)
        self._author = author

    @property
    def author(self):
        return self._author

    def __str__(self):
        return f"{self.name} by {self.author} - ${self.price:.2f}"
