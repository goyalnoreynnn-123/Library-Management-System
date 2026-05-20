"""Main entry point for the Library Management System."""
from library_service import LibraryService
from exceptions import (
    BookNotFoundError,
    MemberNotFoundError,
    BookUnavailableError,
    InvalidLoanError,
    LibraryException
)


def display_menu():
    """Display the main menu."""
    print("\n" + "="*50)
    print("   LIBRARY MANAGEMENT SYSTEM")
    print("="*50)
    print("1. Add Book")
    print("2. Register Member")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. View Books")
    print("6. View Members")
    print("7. View Loans")
    print("8. Exit")
    print("="*50)
    choice = input("Enter your choice (1-8): ").strip()
    return choice


def add_book(service):
    """Feature 1: Add a new book to the library."""
    print("\n--- Add Book ---")
    try:
        book_id = input("Enter Book ID: ").strip()
        title = input("Enter Book Title: ").strip()
        author = input("Enter Book Author: ").strip()
        
        message = service.add_book(book_id, title, author)
        print(f"✓ {message}")
    except Exception as e:
        print(f"✗ Error: {e}")


def register_member(service):
    """Feature 2: Register a new member."""
    print("\n--- Register Member ---")
    try:
        member_id = input("Enter Member ID: ").strip()
        name = input("Enter Member Name: ").strip()
        email = input("Enter Member Email: ").strip()
        
        message = service.register_member(member_id, name, email)
        print(f"✓ {message}")
    except Exception as e:
        print(f"✗ Error: {e}")


def borrow_book(service):
    """Feature 3: Borrow a book."""
    print("\n--- Borrow Book ---")
    try:
        book_id = input("Enter Book ID: ").strip()
        member_id = input("Enter Member ID: ").strip()
        
        message = service.borrow_book(book_id, member_id)
        print(f"✓ {message}")
    except (BookNotFoundError, MemberNotFoundError, BookUnavailableError) as e:
        print(f"✗ Error: {e}")
    except Exception as e:
        print(f"✗ Unexpected Error: {e}")


def return_book(service):
    """Feature 4: Return a borrowed book."""
    print("\n--- Return Book ---")
    try:
        book_id = input("Enter Book ID: ").strip()
        member_id = input("Enter Member ID: ").strip()
        
        message = service.return_book(book_id, member_id)
        print(f"✓ {message}")
    except (BookNotFoundError, MemberNotFoundError, InvalidLoanError) as e:
        print(f"✗ Error: {e}")
    except Exception as e:
        print(f"✗ Unexpected Error: {e}")


def view_books(service):
    """Feature 5: View all books."""
    print("\n--- View Books ---")
    books = service.view_books()
    if not books:
        print("No books found.")
    else:
        print("\nBooks:")
        for book in books:
            print(f"  {book}")


def view_members(service):
    """Feature 6: View all members."""
    print("\n--- View Members ---")
    members = service.view_members()
    if not members:
        print("No members found.")
    else:
        print("\nMembers:")
        for member in members:
            print(f"  {member}")


def view_loans(service):
    """Feature 7: View all loans."""
    print("\n--- View Loans ---")
    loans = service.view_loans()
    if not loans:
        print("No loans found.")
    else:
        print("\nLoans:")
        for loan in loans:
            print(f"  {loan}")


def main():
    """Main application loop."""
    service = LibraryService()
    
    while True:
        choice = display_menu()
        
        if choice == "1":
            add_book(service)
        elif choice == "2":
            register_member(service)
        elif choice == "3":
            borrow_book(service)
        elif choice == "4":
            return_book(service)
        elif choice == "5":
            view_books(service)
        elif choice == "6":
            view_members(service)
        elif choice == "7":
            view_loans(service)
        elif choice == "8":
            print("\nThank you for using the Library Management System. Goodbye!")
            break
        else:
            print("✗ Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
