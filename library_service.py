"""Library Service - Core business logic for library operations."""
from typing import List, Dict
from models import Book, Member, Loan
from exceptions import (
    BookNotFoundError,
    MemberNotFoundError,
    BookUnavailableError,
    InvalidLoanError
)


class LibraryService:
    """Service class managing library operations."""
    
    def __init__(self):
        self._books: Dict[str, Book] = {}
        self._members: Dict[str, Member] = {}
        self._loans: List[Loan] = []
        self._loan_counter = 0
    
    # ============ FEATURE 1: Add Book ============
    def add_book(self, book_id: str, title: str, author: str) -> str:
        """
        Add a new book to the library.
        
        Args:
            book_id: Unique book identifier
            title: Book title
            author: Book author
        
        Returns:
            Success message
        
        Raises:
            ValueError: If book already exists
        """
        if book_id in self._books:
            raise ValueError(f"Book with ID {book_id} already exists.")
        
        book = Book(book_id, title, author)
        self._books[book_id] = book
        return f"Book added successfully: '{title}' by {author}"
    
    # ============ FEATURE 2: Register Member ============
    def register_member(self, member_id: str, name: str, email: str) -> str:
        """
        Register a new library member.
        
        Args:
            member_id: Unique member identifier
            name: Member name
            email: Member email
        
        Returns:
            Success message
        
        Raises:
            ValueError: If member already exists
        """
        if member_id in self._members:
            raise ValueError(f"Member with ID {member_id} already exists.")
        
        member = Member(member_id, name, email)
        self._members[member_id] = member
        return f"Member registered successfully: {name}"
    
    # ============ FEATURE 3: Borrow Book ============
    def borrow_book(self, book_id: str, member_id: str) -> str:
        """
        Borrow a book for a member.
        
        Args:
            book_id: ID of the book to borrow
            member_id: ID of the member borrowing
        
        Returns:
            Success message with loan details
        
        Raises:
            BookNotFoundError: If book doesn't exist
            MemberNotFoundError: If member doesn't exist
            BookUnavailableError: If book is already borrowed
        """
        # Check if book exists
        if book_id not in self._books:
            raise BookNotFoundError(f"Book not found: {book_id}")
        
        book = self._books[book_id]
        
        # Check if member exists
        if member_id not in self._members:
            raise MemberNotFoundError(f"Member not found: {member_id}")
        
        member = self._members[member_id]
        
        # Check if book is available
        if not book.available:
            raise BookUnavailableError(f"Book is already borrowed: {book.title}")
        
        # Borrow the book
        book.borrow()
        
        # Create loan record
        self._loan_counter += 1
        loan_id = f"L{self._loan_counter:03d}"
        loan = Loan(loan_id, book, member)
        self._loans.append(loan)
        
        return f"{member.name} borrowed '{book.title}' (Loan ID: {loan_id})"
    
    # ============ FEATURE 4: Return Book ============
    def return_book(self, loan_id: str) -> str:
        """
        Return a borrowed book.
        
        Args:
            loan_id: ID of the loan to close
        
        Returns:
            Success message
        
        Raises:
            InvalidLoanError: If loan doesn't exist or is already closed
        """
        # Find the loan
        loan = None
        for l in self._loans:
            if l.loan_id == loan_id:
                loan = l
                break
        
        if loan is None:
            raise InvalidLoanError(f"Loan not found: {loan_id}")
        
        if not loan.is_active:
            raise InvalidLoanError(f"Loan already closed: {loan_id}")
        
        # Return the book
        loan.book.return_book()
        loan.close_loan()
        
        return f"Book '{loan.book.title}' returned by {loan.member.name} (Loan ID: {loan_id})"
    
    # ============ FEATURE 5: View Books ============
    def view_books(self) -> List[Book]:
        """
        Get all books in the library.
        
        Returns:
            List of all books
        """
        return list(self._books.values())
    
    # ============ FEATURE 6: View Members ============
    def view_members(self) -> List[Member]:
        """
        Get all registered members.
        
        Returns:
            List of all members
        """
        return list(self._members.values())
    
    # ============ FEATURE 7: View Loans ============
    def view_loans(self) -> List[Loan]:
        """
        Get all loan records.
        
        Returns:
            List of all loans
        """
        return self._loans
