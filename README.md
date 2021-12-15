# 💻 LibraryX Documentation
## Informations:
- It's used the simple feature-driven development.
- The program provides a menu-driven console-based user interface and graphical user interface. The user can start it either by the UI, GUI (Python must be installed).
- Implementation employs layered architecture and classes.
- The repositories have 20 procedurally generated items at startup.
- Provides specification and tests for all non-UI classes and methods(PyUnit test cases).
- Implemented and used own exception classes.


### Details
LibraryX is an application for a book library. The application will store:
- **Book**: `book_id`, `title`, `author`
- **Client**: `client_id`, `name`
- **Rental**: `rental_id`, `book_id`, `client_id`, `rented_date`, `returned_date`

## Functionalites
1. Manage clients and books. The user can add, remove, update, and list both clients and books.
2. Rent or return a book. A client can rent an available book. A client can return a rented book at any time. Only available books (those which are not currently rented) can be rented.
3. Search for clients, books or rentals using any one of their fields (e.g. books can be searched for using id, title or author). The search works using case-insensitive, partial string matching, and returns all matching items.
4. Statistics:
    - Most rented books. This will provide the list of books, sorted in descending order of the number of times they were rented.
    - Most active clients. This will provide the list of clients, sorted in descending order of the number of book rental days they have (e.g. having 2 rented books for 3 days each counts as 2 x 3 = 6 days).
    - Most rented author. This provides the list of book authors, sorted in descending order of the number of rentals their books have.
5. Unlimited undo/redo functionality. Each step will undo/redo the previous operation performed by the user. Undo/redo operations cascade and have a memory-efficient implementation(no superfluous list copying).
6. 3 types of repositories: in memmory, text files and binary files. The decision of which type of repositories are used is made by setting.properties from the package 'files'. By default are used text files repositories.
