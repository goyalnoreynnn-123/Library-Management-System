"""Main entry point - Interactive CLI for Library Management System."""
from library_service import LibraryService
from exceptions import (
    BookNotFoundError,
    MemberNotFoundError,
    BookUnavailableError,
    InvalidLoanError,
    LibraryException
)


class LibraryManagementApp:
    """Interactive CLI application for library management."""
    
    def __init__(self):
        self.service = LibraryService()
    
    def display_menu(self):
        """Display main menu."""
        print("\n" + "="*50)
        print("  LIBRARY MANAGEMENT SYSTEM")
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
    
    def add_book(self):
        """Feature 1: Add a new book."""
        print("\n--- Add Book ---")
        book_id = input("Enter Book ID: ").strip()
        title = input("Enter Book Title: ").strip()
        author = input("Enter Author: ").strip()
        
        try:
            message = self.service.add_book(book_id, title, author)
            print(f"✓ {message}")
        except ValueError as e:
            print(f"✗ Error: {e}")
    
    def register_member(self):
        """Feature 2: Register a new member."""
        print("\n--- Register Member ---")
        member_id = input("Enter Member ID: ").strip()
        name = input("Enter Member Name: ").strip()
        email = input("Enter Email: ").strip()
        
        try:
            message = self.service.register_member(member_id, name, email)
            print(f"✓ {message}")
        except ValueError as e:
            print(f"✗ Error: {e}")
    
    def borrow_book(self):
        """Feature 3: Borrow a book."""
        print("\n--- Borrow Book ---")
        book_id = input("Enter Book ID: ").strip()
        member_id = input("Enter Member ID: ").strip()
        
        try:
            message = self.service.borrow_book(book_id, member_id)
            print(f"✓ {message}")
        except (BookNotFoundError, MemberNotFoundError, BookUnavailableError) as e:
            print(f"✗ Error: {e}")
    
    def return_book(self):
        """Feature 4: Return a book."""
        print("\n--- Return Book ---")
        loan_id = input("Enter Loan ID: ").strip()
        
        try:
            message = self.service.return_book(loan_id)
            print(f"✓ {message}")
        except InvalidLoanError as e:
            print(f"✗ Error: {e}")
    
    def view_books(self):
        """Feature 5: View all books."""
        print("\n--- View Books ---")
        books = self.service.view_books()
        
        if not books:
            print("No books found.")
            return
        
        print(f"\nTotal Books: {len(books)}")
        print("-" * 80)
        for book in books:
            status = "Available" if book.available else "Borrowed"
            print(f"{book.book_id:10} | {book.title:25} | {book.author:20} | {status}")
        print("-" * 80)
    
    def view_members(self):
        """Feature 6: View all members."""
        print("\n--- View Members ---")
        members = self.service.view_members()
        
        if not members:
            print("No members found.")
            return
        
        print(f"\nTotal Members: {len(members)}")
        print("-" * 80)
        for member in members:
            print(f"{member.member_id:10} | {member.name:25} | {member.email}")
        print("-" * 80)
    
    def view_loans(self):
        """Feature 7: View all loans."""
        print("\n--- View Loans ---")
        loans = self.service.view_loans()
        
        if not loans:
            print("No loans found.")
            return
        
        print(f"\nTotal Loans: {len(loans)}")
        print("-" * 100)
        for loan in loans:
            status = "Active" if loan.is_active else "Closed"
            print(f"{loan.loan_id:8} | {loan.member.name:20} | {loan.book.title:30} | {status}")
        print("-" * 100)
    
    def run(self):
        """Run the application."""
        print("\nWelcome to Library Management System!")
        
        while True:
            self.display_menu()
            choice = input("\nEnter your choice (1-8): ").strip()
            
            if choice == "1":
                self.add_book()
            elif choice == "2":
                self.register_member()
            elif choice == "3":
                self.borrow_book()
            elif choice == "4":
                self.return_book()
            elif choice == "5":
                self.view_books()
            elif choice == "6":
                self.view_members()
            elif choice == "7":
                self.view_loans()
            elif choice == "8":
                print("\nThank you for using Library Management System. Goodbye!")
                break
            else:
                print("\n✗ Invalid choice. Please enter a number between 1 and 8.")


if __name__ == "__main__":
    app = LibraryManagementApp()
    app.run()
