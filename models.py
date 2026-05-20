from datetime import datetime
from typing import Optional

class Book:
    """Represents a book in the library."""
    def __init__(self, book_id: str, title: str, author: str):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True
    
    def borrow(self):
        """Mark book as borrowed."""
        if not self.available:
            raise ValueError("Book is already borrowed.")
        self.available = False
    
    def return_book(self):
        """Mark book as available."""
        self.available = True
    
    def __repr__(self):
        status = "Available" if self.available else "Borrowed"
        return f"Book(ID: {self.book_id}, Title: {self.title}, Author: {self.author}, Status: {status})"


class Member:
    """Represents a library member."""
    def __init__(self, member_id: str, name: str, email: str):
        self.member_id = member_id
        self.name = name
        self.email = email
        self.registered_date = datetime.now()
    
    def __repr__(self):
        return f"Member(ID: {self.member_id}, Name: {self.name}, Email: {self.email})"


class Loan:
    """Represents a book loan record."""
    def __init__(self, loan_id: str, book: Book, member: Member):
        self.loan_id = loan_id
        self.book = book
        self.member = member
        self.borrowed_date = datetime.now()
        self.return_date: Optional[datetime] = None
        self.is_active = True
    
    def close_loan(self):
        """Close the loan (book returned)."""
        self.return_date = datetime.now()
        self.is_active = False
    
    def __repr__(self):
        status = "Active" if self.is_active else "Closed"
        return f"Loan(ID: {self.loan_id}, Member: {self.member.name}, Book: {self.book.title}, Status: {status})"
