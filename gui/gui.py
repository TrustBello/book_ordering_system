import sys
import os

# Add the project root directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import tkinter as tk
from tkinter import ttk, messagebox
from core.customer import Customer
from core.stock import Stock
from core.order import Order
from core.shipping import Shipping
from core.invoice import Invoice
from bookstore.bookstore import BookStore


class BookOrderingGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Book Ordering System By 'put_your_name'")

        # Data Storage
        self.customers = []
        self.stocks = []
        self.orders = []
        self.bookstore = BookStore()

        # UI Components
        self.create_main_layout()

    def create_main_layout(self):
        # Customer Input Form
        tk.Label(self.master, text="Customer Details").grid(
            row=0, column=0, columnspan=2, pady=5
        )
        tk.Label(self.master, text="Name:").grid(row=1, column=0)
        self.customer_name = tk.Entry(self.master)
        self.customer_name.grid(row=1, column=1)

        tk.Label(self.master, text="Phone:").grid(row=2, column=0)
        self.customer_phone = tk.Entry(self.master)
        self.customer_phone.grid(row=2, column=1)

        tk.Label(self.master, text="Email:").grid(row=3, column=0)
        self.customer_email = tk.Entry(self.master)
        self.customer_email.grid(row=3, column=1)

        tk.Button(self.master, text="Add Customer", command=self.add_customer).grid(
            row=4, column=0, columnspan=2, pady=5
        )

        # Book Input Form
        tk.Label(self.master, text="Book Details").grid(
            row=0, column=2, columnspan=2, pady=5
        )
        tk.Label(self.master, text="Book Name:").grid(row=1, column=2)
        self.book_name = tk.Entry(self.master)
        self.book_name.grid(row=1, column=3)

        tk.Label(self.master, text="Author:").grid(row=2, column=2)
        self.book_author = tk.Entry(self.master)
        self.book_author.grid(row=2, column=3)

        tk.Label(self.master, text="Price:").grid(row=3, column=2)
        self.book_price = tk.Entry(self.master)
        self.book_price.grid(row=3, column=3)

        tk.Button(self.master, text="Add Book", command=self.add_book).grid(
            row=4, column=2, columnspan=2, pady=5
        )

        # Order Placement
        tk.Label(self.master, text="Place Order").grid(
            row=5, column=0, columnspan=2, pady=5
        )
        tk.Label(self.master, text="Select Customer:").grid(row=6, column=0)
        self.customer_dropdown = ttk.Combobox(self.master, state="readonly", values=[])
        self.customer_dropdown.grid(row=6, column=1)

        tk.Label(self.master, text="Select Book:").grid(row=7, column=0)
        self.book_dropdown = ttk.Combobox(self.master, state="readonly", values=[])
        self.book_dropdown.grid(row=7, column=1)

        tk.Button(self.master, text="Place Order", command=self.place_order).grid(
            row=8, column=0, columnspan=2, pady=5
        )

        # Shipping Options
        tk.Label(self.master, text="Shipping Options").grid(
            row=5, column=2, columnspan=2, pady=5
        )
        self.is_urgent_var = tk.BooleanVar()
        tk.Checkbutton(
            self.master, text="Urgent Shipping", variable=self.is_urgent_var
        ).grid(row=6, column=2, columnspan=2)

        tk.Button(
            self.master, text="Calculate Shipping", command=self.calculate_shipping
        ).grid(row=7, column=2, columnspan=2, pady=5)

        # Invoice Generation
        tk.Label(self.master, text="Invoice Generation").grid(
            row=9, column=0, columnspan=2, pady=5
        )
        tk.Button(
            self.master, text="Generate Invoice", command=self.generate_invoice
        ).grid(row=10, column=0, columnspan=2, pady=5)

        # Invoice Search
        tk.Label(self.master, text="Search Invoice").grid(
            row=9, column=2, columnspan=2, pady=5
        )
        tk.Label(self.master, text="Invoice Number:").grid(row=10, column=2)
        self.invoice_search = tk.Entry(self.master)
        self.invoice_search.grid(row=10, column=3)
        tk.Button(self.master, text="Search", command=self.search_invoice).grid(
            row=11, column=2, columnspan=2, pady=5
        )

        # View All Invoices
        tk.Button(
            self.master, text="View All Invoices", command=self.view_all_invoices
        ).grid(row=12, column=0, columnspan=4, pady=5)

    # Methods
    def add_customer(self):
        name = self.customer_name.get().strip()
        phone = self.customer_phone.get().strip()
        email = self.customer_email.get().strip()

        # Check if any field is empty
        if not name or not phone or not email:
            messagebox.showerror("Error", "All customer fields must be filled.")
            return False

    # Check if the email format is valid
        if "@" not in email:
            messagebox.showerror("Error", "Invalid email format")
            return False

        customer = Customer(name, phone, email)
        self.customers.append(customer)
        self.customer_dropdown["values"] = [c.name for c in self.customers]
        messagebox.showinfo("Success", f"Customer {name} added.")

    def add_book(self):
        name = self.book_name.get().strip()
        author = self.book_author.get().strip()
        price = self.book_price.get().strip()

        if not name or not author or not price:
            messagebox.showerror("Error", "All book fields must be filled.")
            return

        try:
            price = float(price)
            if price <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Price must be a valid positive number.")
            return

        stock = Stock(name, author, price)
        self.stocks.append(stock)
        self.book_dropdown["values"] = [s.name for s in self.stocks]
        messagebox.showinfo("Success", f"Book '{name}' added.")

    def place_order(self):
        customer_name = self.customer_dropdown.get()
        book_name = self.book_dropdown.get()

        if not customer_name or not book_name:
            messagebox.showerror("Error", "Select both a customer and a book.")
            return

        customer = next(c for c in self.customers if c.name == customer_name)
        stock = next(s for s in self.stocks if s.name == book_name)
        order = Order(customer, stock)
        self.orders.append(order)
        messagebox.showinfo(
            "Success", f"Order placed for {book_name} by {customer_name}."
        )

    def calculate_shipping(self):
        if not self.orders:
            messagebox.showerror("Error", "No orders to calculate shipping for.")
            return

        last_order = self.orders[-1]
        self.shipping = Shipping(last_order, is_urgent=self.is_urgent_var.get())
        urgency = "Urgent" if self.shipping.is_urgent else "Standard"
        messagebox.showinfo(
            "Success", f"Shipping calculated: {urgency} - ${self.shipping.cost:.2f}"
        )

    def generate_invoice(self):
        if not hasattr(self, "shipping"):
            messagebox.showerror(
                "Error", "Calculate shipping before generating an invoice."
            )
            return

        invoice_nbr = f"INV{len(self.bookstore.invoices) + 1:03d}"
        invoice = Invoice(invoice_nbr, self.orders[-1], self.shipping)
        self.bookstore.add_invoice(invoice)
        messagebox.showinfo("Invoice Generated", str(invoice))

    def search_invoice(self):
        invoice_nbr = self.invoice_search.get().strip()
        if not invoice_nbr:
            messagebox.showerror("Error", "Enter an invoice number to search.")
            return

        result = self.bookstore.search_invoice(invoice_nbr)
        messagebox.showinfo("Invoice Search Result", str(result))

    def view_all_invoices(self):
        if not self.bookstore.invoices:
            messagebox.showinfo("No Invoices", "No invoices available.")
            return

        invoices = "\n".join(str(inv) for inv in self.bookstore.invoices)
        messagebox.showinfo("All Invoices", invoices)


if __name__ == "__main__":
    root = tk.Tk()
    app = BookOrderingGUI(root)
    root.mainloop()
