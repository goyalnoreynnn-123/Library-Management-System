# Library Management System

A comprehensive Python-based library management system with interactive CLI interface. This project implements all 7 core features for managing books, members, and loans.

## Features

### 1. ✅ Add Book
- Add new books to the library inventory
- Each book has: ID, Title, Author
- Prevents duplicate book IDs
- Books are marked as available by default

### 2. ✅ Register Member
- Register new library members
- Each member has: ID, Name, Email
- Prevents duplicate member IDs
- Tracks registration date automatically

### 3. ✅ Borrow Book
- Members can borrow available books
- Creates a loan record with unique Loan ID
- Validates:
  - Book exists in the system
  - Member exists in the system
  - Book is currently available
- Updates book availability status
- Error handling for all validation failures

### 4. ✅ Return Book
- Members can return borrowed books using Loan ID
- Closes the loan record
- Marks book as available again
- Validates:
  - Loan exists in the system
  - Loan is currently active
- Tracks return date automatically

### 5. ✅ View Books
- Display all books in the library
- Shows:
  - Book ID
  - Title
  - Author
  - Availability status (Available/Borrowed)
- Handles empty library gracefully

### 6. ✅ View Members
- Display all registered members
- Shows:
  - Member ID
  - Name
  - Email
  - Registration date (via model)
- Handles no members gracefully

### 7. ✅ View Loans
- Display all loan records
- Shows:
  - Loan ID
  - Member Name
  - Book Title
  - Loan Status (Active/Closed)
  - Borrow and return dates (via model)
- Handles no loans gracefully

## Project Structure

```
Library-Management-System/
├── models.py              # Data models: Book, Member, Loan
├── exceptions.py          # Custom exception classes
├── library_service.py     # Business logic layer (Service)
├── main.py                # CLI Application
├── README.md              # This file
└── flowcharts/            # Visual flowcharts for each feature
    ├── _01_add_book.svg
    ├── _02_register_member.svg
    ├── _03_borrow_book.svg
    ├── _04_return_book.svg
    ├── _05_view_book.svg
    ├── _06_view_member.svg
    └── _07_view_loan.svg
```

## Architecture

### Models (`models.py`)
- **Book**: Represents a library book with borrow/return functionality
- **Member**: Represents a library member with registration tracking
- **Loan**: Represents a book loan with active/closed status

### Exceptions (`exceptions.py`)
- **BookNotFoundError**: Raised when a book doesn't exist
- **MemberNotFoundError**: Raised when a member doesn't exist
- **BookUnavailableError**: Raised when a book is already borrowed
- **InvalidLoanError**: Raised when loan operations are invalid

### Service Layer (`library_service.py`)
- **LibraryService**: Core business logic with:
  - Dictionary storage for books and members
  - List storage for loan records
  - All 7 feature implementations
  - Comprehensive error handling
  - Automatic loan ID generation

### Application (`main.py`)
- **LibraryManagementApp**: Interactive CLI with menu-driven interface
- User-friendly input/output
- Error message display
- Formatted table outputs

## Installation

### Prerequisites
- Python 3.7+
- No external dependencies required

### Setup

```bash
# Clone the repository
git clone https://github.com/goyalnoreynnn-123/Library-Management-System.git
cd Library-Management-System

# Run the application
python main.py
```

## Usage

### Starting the Application
```bash
python main.py
```

### Menu Navigation
The application presents an interactive menu:
```
==================================================
  LIBRARY MANAGEMENT SYSTEM
==================================================
1. Add Book
2. Register Member
3. Borrow Book
4. Return Book
5. View Books
6. View Members
7. View Loans
8. Exit
==================================================
```

### Example Workflow

#### Step 1: Add Books
```
Choice: 1
Enter Book ID: B001
Enter Book Title: Python Programming
Enter Author: Guido van Rossum
✓ Book added successfully: 'Python Programming' by Guido van Rossum
```

#### Step 2: Register Members
```
Choice: 2
Enter Member ID: M001
Enter Member Name: John Doe
Enter Email: john@example.com
✓ Member registered successfully: John Doe
```

#### Step 3: Borrow Book
```
Choice: 3
Enter Book ID: B001
Enter Member ID: M001
✓ John Doe borrowed 'Python Programming' (Loan ID: L001)
```

#### Step 4: View Books
```
Choice: 5
--- View Books ---

Total Books: 1
────────────────────────────────────────────────────────────────────────────────
B001       | Python Programming       | Guido van Rossum | Borrowed
────────────────────────────────────────────────────────────────────────────────
```

#### Step 5: View Loans
```
Choice: 7
--- View Loans ---

Total Loans: 1
────────────────────────────────────────────────────────────────────────────────────────────────────
L001     | John Doe             | Python Programming               | Active
────────────────────────────────────────────────────────────────────────────────────────────────────
```

#### Step 6: Return Book
```
Choice: 4
Enter Loan ID: L001
✓ Book 'Python Programming' returned by John Doe (Loan ID: L001)
```

## Error Handling

The system provides comprehensive error handling:

### Add Book
```
✗ Error: Book with ID B001 already exists.
```

### Register Member
```
✗ Error: Member with ID M001 already exists.
```

### Borrow Book
```
✗ Error: Book not found: B999
✗ Error: Member not found: M999
✗ Error: Book is already borrowed: Python Programming
```

### Return Book
```
✗ Error: Loan not found: L999
✗ Error: Loan already closed: L001
```

## Technical Details

### Data Storage
- **Books**: Dictionary with book_id as key (O(1) lookup)
- **Members**: Dictionary with member_id as key (O(1) lookup)
- **Loans**: List for maintaining order and history

### Loan ID Generation
- Format: `L###` (e.g., L001, L002, L003)
- Automatically incremented counter
- Ensures uniqueness throughout session

### Availability Tracking
- Book.available: Boolean flag
- Updated on borrow/return operations
- Validated before borrowing

### Status Tracking
- Loan.is_active: Boolean flag
- Updated when loan is closed (book returned)
- Enables distinguishing active vs closed loans

## Flowcharts

Visual flowcharts for each feature are provided in the `flowcharts/` directory:

1. **Add Book** (`_01_add_book.svg`)
   - Start → Display menu → Input book details → Create object → Store in dict → Output success → End

2. **Register Member** (`_02_register_member.svg`)
   - Start → Display menu → Input member details → Create object → Store in dict → Output success → End

3. **Borrow Book** (`_03_borrow_book.svg`)
   - Start → Display menu → Input IDs → Lookup book → Check availability → Lookup member → Create loan → End
   - Error handling for missing book/member and unavailable book

4. **Return Book** (`_04_return_book.svg`)
   - Start → Display menu → Input loan ID → Find loan → Close loan → Update availability → Output success → End

5. **View Books** (`_05_view_book.svg`)
   - Start → Display menu → Get all books → Check empty → Display header → Loop through books → Display each → End

6. **View Members** (`_06_view_member.svg`)
   - Start → Display menu → Get all members → Check empty → Display header → Loop through members → Display each → End

7. **View Loans** (`_07_view_loan.svg`)
   - Start → Display menu → Get all loans → Check empty → Display header → Loop through loans → Display with status → End

## Features Highlights

✨ **Robust Error Handling**
- Custom exception hierarchy
- Meaningful error messages
- Graceful error recovery

✨ **Data Validation**
- Prevents duplicate entries
- Validates book/member existence
- Checks availability status
- Validates active loans

✨ **User-Friendly Interface**
- Clear menu system
- Formatted output tables
- Status indicators (✓/✗)
- Input prompts with guidance

✨ **Clean Architecture**
- Separation of concerns (Models, Service, Application)
- Reusable components
- Easy to extend

✨ **Production-Ready**
- Comprehensive documentation
- Type hints for clarity
- Docstrings for all methods
- Well-structured code

## Future Enhancements

Potential features for future versions:
- Database persistence (SQLite, PostgreSQL)
- User authentication and authorization
- Fine calculation for overdue books
- Search and filter functionality
- Email notifications
- Member and book reports
- Reservation system
- Web interface (Flask/Django)

## License

This project is open source and available under the MIT License.

## Author

Developed as a mini-project to demonstrate library management system implementation.

## Support

For issues, questions, or suggestions, please create an issue in the repository.
