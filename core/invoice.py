import sys
import os

# Add the project root directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from core.stock import Stock
from core.shipping import Shipping


class Invoice:
    def __init__(self, invoice_nbr: str, order, shipping):
        self._invoice_nbr = invoice_nbr
        self._order = order
        self._shipping = shipping

    @property
    def invoice_nbr(self):
        return self._invoice_nbr

    @property
    def total_cost(self):
        return self._order.stock.price + self._shipping.cost

    def __str__(self):
        return (
            f"Invoice #{self.invoice_nbr} | "
            f"Customer: {self._order.customer.name} | "
            f"Book: {self._order.stock.name} | "
            f"Total: ${self.total_cost:.2f}"
        )
