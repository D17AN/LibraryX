# 💻 LibraryX
A book rental application
### Informations:
- It's used the simple feature-driven development.
- The program provides a menu-driven console-based user interface and graphical user interface. The app is started by running main.py, either by running the executable.
- Implementation employs layered architecture and classes.
- The repositories have 20 procedurally generated items at startup.
- Provides specification and tests for all non-UI classes and methods(PyUnit test cases).
- Implemented and used own exception classes.

### Requirements:
- A version of Python 3 must be installed. Recommended a version above 3.9.7.
- To run the app I would recommend using an IDE, recommended PyCharm (Community Edition, which is the free version, is more than enough).

### Details
LibraryX is an application for a book library. The application will store:
- **Book**: `book_id`, `title`, `author`
- **Client**: `client_id`, `name`
- **Rental**: `rental_id`, `book_id`, `client_id`, `rented_date`, `returned_date`

### Functionalites
1. Manage clients and books. The user can add, remove, update, and list both clients and books.
2. Rent or return a book. A client can rent an available book. A client can return a rented book at any time. Only available books (those which are not currently rented) can be rented.
3. Search for clients, books or rentals using any one of their fields (e.g. books can be searched for using id, title or author). The search works using case-insensitive, partial string matching, and returns all matching items.
4. Statistics:
    - Most rented books. This will provide the list of books, sorted in descending order of the number of times they were rented.
    - Most active clients. This will provide the list of clients, sorted in descending order of the number of book rental days they have (e.g. having 2 rented books for 3 days each counts as 2 x 3 = 6 days).
    - Most rented author. This provides the list of book authors, sorted in descending order of the number of rentals their books have.
5. Unlimited undo/redo functionality. Each step will undo/redo the previous operation performed by the user. Undo/redo operations cascade and have a memory-efficient implementation(no superfluous list copying).
6. 3 types of repositories: in memmory, text files and binary files. The decision of which type of repositories are used is made by setting.properties from the package 'files'. By default are used text files repositories.

### Showcase
![1](https://user-images.githubusercontent.com/9745845/236555765-f416ab50-1978-41bd-9f3b-cddadac68dff.PNG)
![2](https://user-images.githubusercontent.com/9745845/236555767-4bc5ff63-0c93-4136-b485-3458e58a31a5.PNG)
![3](https://user-images.githubusercontent.com/9745845/236555769-f8d6913b-6f1c-449e-bdf3-645dea649d74.PNG)
![4](https://user-images.githubusercontent.com/9745845/236555770-ff09362e-f8f5-4ced-bae3-3f3ec3c46d7d.PNG)
![7](https://user-images.githubusercontent.com/9745845/236555774-c8779ac0-9cbe-48a3-ba2e-a6d024df10af.PNG)
![6](https://user-images.githubusercontent.com/9745845/236555773-cfea16a1-aecf-48af-9b0b-402ae0848753.PNG)
![5](https://user-images.githubusercontent.com/9745845/236555771-ba03e82c-ff15-4277-bec6-b8c6b5b0e183.PNG)


