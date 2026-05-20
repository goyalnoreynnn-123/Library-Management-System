"""Custom exceptions for Library Management System."""

class LibraryException(Exception):
    """Base exception for library operations."""
    pass


class BookNotFoundError(LibraryException):
    """Raised when a book is not found."""
    pass


class MemberNotFoundError(LibraryException):
    """Raised when a member is not found."""
    pass


class BookUnavailableError(LibraryException):
    """Raised when a book is already borrowed."""
    pass


class InvalidLoanError(LibraryException):
    """Raised when loan operations are invalid."""
    pass
