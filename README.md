# Library Management System

A comprehensive Python-based library management system that handles book inventory, member registration, and loan tracking.

## Features

### 1. **Add Book** (Feature 1)
- Add new books to the library database
- Each book has:
  - Unique book ID
  - Title
  - Author
  - Availability status (initially True)
- Duplicate book IDs are rejected

### 2. **Register Member** (Feature 2)
- Register new library members
- Each member has:
  - Unique member ID
  - Full name
  - Email address
- Duplicate member IDs are rejected

### 3. **Borrow Book** (Feature 3)
- Members can borrow available books
- Validations:
  - Book must exist in library
  - Member must be registered
  - Book must be available (not already borrowed)
- Creates a loan record with auto-generated loan ID (L001, L002, etc.)
- Updates book availability to False

### 4. **Return Book** (Feature 4)
- Members can return borrowed books
- Validations:
  - Book must exist
  - Member must be registered
  - Active loan must exist for the member-book pair
- Closes the loan record
- Updates book availability back to True

### 5. **View Books** (Feature 5)
- Display all books in the library
- Shows book ID, title, author, and availability status
- Displays "Available" or "Borrowed" for each book

### 6. **View Members** (Feature 6)
- Display all registered members
- Shows member ID, name, and email

### 7. **View Loans** (Feature 7)
- Display all loans (active and closed)
- Shows loan ID, member name, book title, and loan status
- Displays "Active" or "Closed" for each loan

## Project Structure

```
Library-Management-System/
├── models.py              # Data models (Book, Member, Loan classes)
├── exceptions.py          # Custom exception classes
├── library_service.py     # Service layer with business logic
├── main.py                # Main application and CLI interface
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

## Installation

```bash
# Clone the repository
git clone https://github.com/goyalnoreynnn-123/Library-Management-System.git
cd Library-Management-System
```

## Usage

```bash
python main.py
```

The application will display an interactive menu:

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
Enter your choice (1-8): 
```

### Example Workflow

```
1. Add Book
   - Book ID: B001
   - Title: The Great Gatsby
   - Author: F. Scott Fitzgerald

2. Register Member
   - Member ID: M001
   - Name: John Doe
   - Email: john@example.com

3. Borrow Book
   - Book ID: B001
   - Member ID: M001
   → Output: "John Doe borrowed The Great Gatsby"

5. View Books
   → B001 - The Great Gatsby by F. Scott Fitzgerald [Borrowed]

7. View Loans
   → L001 - John Doe borrowed The Great Gatsby [Active]

4. Return Book
   - Book ID: B001
   - Member ID: M001
   → Output: "John Doe returned The Great Gatsby"

5. View Books
   → B001 - The Great Gatsby by F. Scott Fitzgerald [Available]

7. View Loans
   → L001 - John Doe borrowed The Great Gatsby [Closed]
```

## Architecture

### Models (`models.py`)
- **Book**: Represents a book with ID, title, author, and availability
- **Member**: Represents a library member with ID, name, and email
- **Loan**: Represents a borrowing transaction with loan ID, book, member, dates, and status

### Service Layer (`library_service.py`)
- **LibraryService**: Main service class managing:
  - Book inventory (dictionary)
  - Member registry (dictionary)
  - Loan records (list)
  - Business logic for all operations

### Exceptions (`exceptions.py`)
- Custom exception hierarchy for better error handling:
  - `LibraryException`: Base exception
  - `BookNotFoundError`: Book lookup failed
  - `MemberNotFoundError`: Member lookup failed
  - `BookUnavailableError`: Book is already borrowed
  - `InvalidLoanError`: Loan operation invalid

### UI (`main.py`)
- Interactive command-line interface
- Menu-driven navigation
- Error handling and user feedback
- Input validation and error messages

## Error Handling

The system includes comprehensive error handling:

- **Duplicate entries**: Prevents duplicate book/member IDs
- **Not found errors**: Validates book and member existence
- **Availability checks**: Ensures books can only be borrowed if available
- **Loan validation**: Ensures valid loan operations
- **User feedback**: Clear error messages for all failures

## Data Flow

### Borrow Book Flow
1. User inputs book ID and member ID
2. Lookup book and member in respective dictionaries
3. Validate both exist
4. Check book availability
5. Mark book as unavailable
6. Generate loan ID
7. Create loan record with timestamp
8. Return success message

### Return Book Flow
1. User inputs book ID and member ID
2. Lookup book and member
3. Find active loan matching both
4. Mark book as available
5. Close loan record with return timestamp
6. Return success message

## Future Enhancements

- Persistent storage (database integration)
- User authentication and authorization
- Loan due dates and overdue tracking
- Fine calculations for late returns
- Book search and filtering
- Member borrowing history
- Reports and analytics
- Email notifications
- Web interface
- API endpoints

## License

MIT License

## Author

Library Management System - Mini Project
