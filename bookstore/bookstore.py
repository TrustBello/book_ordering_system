class BookStore:
    def __init__(self):
        self._invoices = []

    @property
    def invoices(self):
        return self._invoices

    def add_invoice(self, invoice):
        self._invoices.append(invoice)

    def search_invoice(self, invoice_nbr):
        for invoice in self._invoices:
            if invoice.invoice_nbr == invoice_nbr:
                return invoice
        return "Invoice not found."
