class Library:

    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print("Book added successfully!")

    def display_books(self):
        if len(self.books) == 0:
            print("No books available.")
        else:
            print("\nAvailable Books:")
            for book in self.books:
                print(book)

    def search_book(self, name):
        if name in self.books:
            print(f"{name} is available.")
        else:
            print(f"{name} is not available.")

    def issue_book(self, name):
        if name in self.books:
            self.books.remove(name)
            print(f"{name} issued successfully.")
        else:
            print("Book not available.")

    def return_book(self, name):
        self.books.append(name)
        print(f"{name} returned successfully.")


library = Library()

while True:

    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        book = input("Enter book name: ")
        library.add_book(book)

    elif choice == 2:
        library.display_books()

    elif choice == 3:
        book = input("Enter book name to search: ")
        library.search_book(book)

    elif choice == 4:
        book = input("Enter book name to issue: ")
        library.issue_book(book)

    elif choice == 5:
        book = input("Enter book name to return: ")
        library.return_book(book)

    elif choice == 6:
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")