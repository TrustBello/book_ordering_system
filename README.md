# Book Ordering System

## Overview

The **Book Ordering System** is a Python-based application designed for managing customer orders, book inventory, shipping, and invoices. It provides a user-friendly **Graphical User Interface (GUI)** for interaction and a robust backend to handle core functionalities. This system is ideal for small bookstores or university projects to demonstrate end-to-end application development.

---

## Features

- **Customer Management**: Add and manage customer details, including name, phone number, and email.
- **Book Inventory**: Add and store book details such as name, author, and price.
- **Order Placement**: Enable customers to place orders for available books.
- **Shipping Options**: Calculate shipping costs based on urgency.
- **Invoice Management**: Generate invoices for orders and calculate total costs.
- **Invoice Search**: Search for specific invoices by number.
- **Invoice Repository View**: View all stored invoices.
- **User Interface**: An intuitive GUI built with `tkinter`.

---

## Project Structure

```plaintext
book_ordering_system/
|-- main.py                 # Entry point for CLI-based operations
|-- core/                   # Core business logic and classes
|   |-- __init__.py         # Indicates this directory is a package
|   |-- customer.py         # Handles customer-related operations
|   |-- invoice.py          # Manages invoice generation and details
|   |-- order.py            # Handles order placement logic
|   |-- person.py           # Base class for personal details
|   |-- product.py          # Defines book attributes
|   |-- shipping.py         # Calculates shipping costs
|   |-- stock.py            # Extends product with author information
|-- bookstore/              # Invoice repository and management
|   |-- __init__.py         # Indicates this directory is a package
|   |-- bookstore.py        # Tracks and searches invoices
|-- gui/                    # Graphical User Interface
|   |-- __init__.py         # Indicates this directory is a package
|   |-- gui.py              # Implements the GUI using tkinter
|-- tests/                  # Testing suite for backend logic
|   |-- __init__.py         # Indicates this directory is a package
|   |-- test.py             # Unit tests for core functionality
```

---

## Installation

### Prerequisites

- Python 3.7 or higher
- Libraries: `tkinter` (pre-installed with Python)

### Setup Steps

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-repo/book-ordering-system.git
   cd book-ordering-system
   ```

2. **Install dependencies**:
   If additional libraries are required, install them using `pip`:

   ```bash
   python -m venv env  # Create the virtual environment
    source env/bin/activate  # Activate the virtual environment
    # On Windows: env\Scripts\activate
   ```

3. **Install dependencies**:
   If additional libraries are required, install them using `pip`:

   ```bash
   pip install -r requirements.txt
   ```

4. **Verify functionality**:
   Run the test suite to confirm all components work as expected:

   ```bash
   python tests/test.py
   ```

5. **Launch the GUI**:
   ```bash
   python gui/gui.py
   ```

---

## Usage Guide

### Customer Management

- **Add a Customer**:
  - Fill in the fields with the appropriate values: `Name`, `Phone`, and `Email`.
  - Click **Add Customer** to save the details and add a new customer.

### Book Inventory

- **Add a Book**:
  - Fill in the fields the correct values: `Book Name`, `Author`, and `Price`.
  - Click **Add Book** to save the book and add a new book.

### Order Placement

- **Place an Order**:
  - Select a customer and a book from the dropdowns.
  - Click **Place Order** to confirm the order.

### Shipping Options

- **Calculate Shipping**:
  - Select the **Urgent Shipping** checkbox if needed.
  - Click **Calculate Shipping** to compute the cost.

### Invoice Management

- **Generate an Invoice**:
  - Ensure the order and shipping details are entered correctly.
  - Click **Generate Invoice** to create an invoice.

- **Search for an Invoice**:
  - Enter the `Invoice Number` and click **Search**.

- **View All Invoices**:
  - Click **View All Invoices** to list all generated invoices.

---

## Testing

The application includes a comprehensive suite of unit tests for backend validation:

```bash
python tests/test.py
```

---

## Future Enhancements

- **Database Integration**: Implement a database (e.g., SQLite) for persistent storage.
- **PDF Export**: Enable exporting invoices as PDF files.
- **Enhanced GUI**: Add advanced widgets and improve usability.
- **Online Orders**: Integrate with an e-commerce platform for online orders.

---

## License

This project is licensed under the **MIT License**. You are free to use, modify, and distribute the application.

---

## Author

For queries or contributions, contact:

- **Email**: your-email@example.com
- **GitHub**: [Your GitHub Profile](https://github.com/your-profile)

---
