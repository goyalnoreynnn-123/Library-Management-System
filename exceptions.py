"""Custom exceptions for the Library Management System."""


class LibraryException(Exception):
    """Base exception for library operations."""
    pass


class BookNotFoundError(LibraryException):
    """Raised when a book is not found in the library."""
    pass


class MemberNotFoundError(LibraryException):
    """Raised when a member is not found in the system."""
    pass


class BookUnavailableError(LibraryException):
    """Raised when attempting to borrow a book that is already borrowed."""
    pass


class InvalidLoanError(LibraryException):
    """Raised when attempting invalid loan operations."""
    pass
