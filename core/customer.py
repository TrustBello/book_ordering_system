import sys
import os

# Add the project root directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from core.person import Person


class Customer(Person):
    def __str__(self):
        return f"{self.name} ({self.email})"
