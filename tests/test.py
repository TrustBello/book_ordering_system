import sys
import os

# Add the project root directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from core.customer import Customer
from core.stock import Stock
from core.order import Order
from core.shipping import Shipping
from core.invoice import Invoice
from bookstore.bookstore import BookStore


def main():
    # Customers
    customer1 = Customer("Alice", "1234567890", "alice@example.com")
    customer2 = Customer("John", "0987654321", "john@example.com")
    customer3 = Customer("JDoe", "0912598739", "doe@example.com")

    # Books
    stock1 = Stock("Book1", "Author1", 10.0)
    stock2 = Stock("Book2", "Author2", 15.0)
    stock3 = Stock("Book3", "Author3", 20.0)

    # Orders
    order1 = Order(customer1, stock1)
    order2 = Order(customer2, stock2)
    order3 = Order(customer3, stock3)

    # Shipping
    shipping1 = Shipping(order1, is_urgent=True)
    shipping2 = Shipping(order2, is_urgent=False)
    shipping3 = Shipping(order3, is_urgent=True)

    # Invoices
    invoice1 = Invoice("INV001", order1, shipping1)
    invoice2 = Invoice("INV002", order2, shipping2)
    invoice3 = Invoice("INV003", order3, shipping3)

    # Bookstore
    bookstore = BookStore()
    bookstore.add_invoice(invoice1)
    bookstore.add_invoice(invoice2)
    bookstore.add_invoice(invoice3)

    print(bookstore.search_invoice("INV001"))
    print(bookstore.search_invoice("INV002"))
    print(bookstore.search_invoice("INV003"))
    print(bookstore.search_invoice("INV004"))


if __name__ == "__main__":
    main()
