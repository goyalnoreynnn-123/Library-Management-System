"""Data models for the Library Management System."""
from datetime import datetime


class Book:
    """Represents a book in the library."""
    
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True
    
    def borrow(self):
        """Mark the book as borrowed."""
        if not self.available:
            raise Exception("Book is already borrowed.")
        self.available = False
    
    def return_book(self):
        """Mark the book as returned."""
        if self.available:
            raise Exception("Book is already available.")
        self.available = True
    
    def __repr__(self):
        status = "Available" if self.available else "Borrowed"
        return f"{self.book_id} - {self.title} by {self.author} [{status}]"


class Member:
    """Represents a library member."""
    
    def __init__(self, member_id, name, email):
        self.member_id = member_id
        self.name = name
        self.email = email
    
    def __repr__(self):
        return f"{self.member_id} - {self.name} ({self.email})"


class Loan:
    """Represents a book loan transaction."""
    
    def __init__(self, loan_id, book, member):
        self.loan_id = loan_id
        self.book = book
        self.member = member
        self.borrow_date = datetime.now()
        self.return_date = None
        self.is_active = True
    
    def close_loan(self):
        """Close the loan (book returned)."""
        self.return_date = datetime.now()
        self.is_active = False
    
    def __repr__(self):
        status = "Active" if self.is_active else "Closed"
        return f"{self.loan_id} - {self.member.name} borrowed {self.book.title} [{status}]"
