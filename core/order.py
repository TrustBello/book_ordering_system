import sys
import os

# Add the project root directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from core.customer import Customer
from core.stock import Stock


class Order:
    def __init__(self, customer, stock):
        self._customer = customer
        self._stock = stock

    @property
    def customer(self):
        return self._customer

    @property
    def stock(self):
        return self._stock

    def __str__(self):
        return f"Order for {self.stock.name} by {self.customer.name}"

