"""Service layer for library operations."""
from models import Book, Member, Loan
from exceptions import (
    BookNotFoundError,
    MemberNotFoundError,
    BookUnavailableError,
    InvalidLoanError
)


class LibraryService:
    """Service class handling all library operations."""
    
    def __init__(self):
        self._books = {}  # Dictionary: book_id -> Book
        self._members = {}  # Dictionary: member_id -> Member
        self._loans = []  # List of Loan objects
        self._loan_counter = 0
    
    # Feature 1: Add Book
    def add_book(self, book_id, title, author):
        """Add a new book to the library.
        
        Args:
            book_id: Unique identifier for the book
            title: Title of the book
            author: Author of the book
        
        Returns:
            str: Success message
        """
        if book_id in self._books:
            raise Exception(f"Book with ID {book_id} already exists.")
        
        book = Book(book_id, title, author)
        self._books[book_id] = book
        return f"Book added: {title}"
    
    # Feature 2: Register Member
    def register_member(self, member_id, name, email):
        """Register a new member to the library.
        
        Args:
            member_id: Unique identifier for the member
            name: Full name of the member
            email: Email address of the member
        
        Returns:
            str: Success message
        """
        if member_id in self._members:
            raise Exception(f"Member with ID {member_id} already exists.")
        
        member = Member(member_id, name, email)
        self._members[member_id] = member
        return f"Member registered: {name}"
    
    # Feature 3: Borrow Book
    def borrow_book(self, book_id, member_id):
        """Member borrows a book from the library.
        
        Args:
            book_id: ID of the book to borrow
            member_id: ID of the member borrowing
        
        Returns:
            str: Success message
        
        Raises:
            BookNotFoundError: If book not found
            MemberNotFoundError: If member not found
            BookUnavailableError: If book is already borrowed
        """
        # Lookup book
        book = self._books.get(book_id)
        if book is None:
            raise BookNotFoundError("Book not found.")
        
        # Lookup member
        member = self._members.get(member_id)
        if member is None:
            raise MemberNotFoundError("Member not found.")
        
        # Check if book is available
        if not book.available:
            raise BookUnavailableError("Book is already borrowed.")
        
        # Borrow the book
        book.borrow()
        
        # Create loan record
        self._loan_counter += 1
        loan_id = f"L{self._loan_counter:03d}"
        loan = Loan(loan_id, book, member)
        self._loans.append(loan)
        
        return f"{member.name} borrowed {book.title}"
    
    # Feature 4: Return Book
    def return_book(self, book_id, member_id):
        """Member returns a borrowed book to the library.
        
        Args:
            book_id: ID of the book being returned
            member_id: ID of the member returning
        
        Returns:
            str: Success message
        
        Raises:
            BookNotFoundError: If book not found
            MemberNotFoundError: If member not found
            InvalidLoanError: If no active loan exists
        """
        # Lookup book
        book = self._books.get(book_id)
        if book is None:
            raise BookNotFoundError("Book not found.")
        
        # Lookup member
        member = self._members.get(member_id)
        if member is None:
            raise MemberNotFoundError("Member not found.")
        
        # Find active loan
        active_loan = None
        for loan in self._loans:
            if (loan.book.book_id == book_id and 
                loan.member.member_id == member_id and 
                loan.is_active):
                active_loan = loan
                break
        
        if active_loan is None:
            raise InvalidLoanError(f"No active loan found for {member.name} and {book.title}.")
        
        # Return the book
        book.return_book()
        active_loan.close_loan()
        
        return f"{member.name} returned {book.title}"
    
    # Feature 5: View Books
    def view_books(self):
        """Get list of all books in the library.
        
        Returns:
            list: List of Book objects
        """
        return list(self._books.values())
    
    # Feature 6: View Members
    def view_members(self):
        """Get list of all registered members.
        
        Returns:
            list: List of Member objects
        """
        return list(self._members.values())
    
    # Feature 7: View Loans
    def view_loans(self):
        """Get list of all loans (active and closed).
        
        Returns:
            list: List of Loan objects
        """
        return list(self._loans)
