import sys
import os
import datetime

# Add the project root directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from core.order import Order


class Shipping:
    def __init__(self, order, is_urgent=False):
        self._order = order
        self._is_urgent = is_urgent

    @property
    def order(self):
        return self._order

    @property
    def is_urgent(self):
        return self._is_urgent

    @property
    def cost(self):
        return 5.45 if self.is_urgent else 3.95

    def __str__(self):
        urgency = "Urgent" if self.is_urgent else "Standard"
        return f"Shipping ({urgency}) - ${self.cost:.2f}"
