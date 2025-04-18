from tkinter import *

# Library catalog class
class LibraryCatalog:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        self.books.remove(book)

    def search_books(self, keyword):
        matching_books = []
        for book in self.books:
            if keyword.lower() in book.title.lower() or keyword.lower() in book.author.lower() or keyword.lower() in book.subject.lower():
                matching_books.append(book)
        return matching_books

    def sort_books_by_title(self):
        n = len(self.books)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if self.books[j].title > self.books[j + 1].title:
                    self.books[j], self.books[j + 1] = self.books[j + 1], self.books[j]

    def sort_books_by_author(self):
        n = len(self.books)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if self.books[j].author > self.books[j + 1].author:
                    self.books[j], self.books[j + 1] = self.books[j + 1], self.books[j]


# Book class
class Book:
    def __init__(self, title, author, subject):
        self.title = title
        self.author = author
        self.subject = subject
        self.available = True


# GUI class
class LibraryGUI:
    def __init__(self, root, library):
        self.root = root
        self.library = library

        # Login screen
        self.login_frame = Frame(root)
        self.login_frame.pack()

        self.login_label = Label(self.login_frame, text="Login to access the catalog system",fg="red",bg="green")
        self.login_label.pack()

        self.login_button = Button(self.login_frame, text="Login", command=self.show_login_window,fg="red",bg="green")
        self.login_button.pack()

    def show_login_window(self):
        # Create a new window for login
        login_window = Toplevel(self.root)
        login_window.title("Login")

        username_label = Label(login_window, text="Username:",fg="red",bg="green")
        username_label.pack()
        username_entry = Entry(login_window)
        username_entry.pack()

        password_label = Label(login_window, text="Password:",fg="red",bg="green")
        password_label.pack()
        password_entry = Entry(login_window, show="*")  # Show "*" instead of actual password characters
        password_entry.pack()

        def login():
            # Check username and password here
            username = username_entry.get()
            password = password_entry.get()

            if username == "Khurram" and password == "3182":
                login_window.destroy()
                self.show_main_menu()
            else:
                error_label = Label(login_window, text="Invalid username or password")
                error_label.pack()

        login_button = Button(login_window, text="Login", command=login,fg="red",bg="green")
        login_button.pack()

        # Main menu screen
        self.main_menu_frame = Frame(root)

        self.add_book_button = Button(self.main_menu_frame, text="Add Book", command=self.add_book,fg="red",bg="green")
        self.add_book_button.pack()

        self.all_books_button = Button(self.main_menu_frame, text="All Book List", command=self.show_all_books,fg="red",bg="green")
        self.all_books_button.pack()

        self.search_book_button = Button(self.main_menu_frame, text="Search Book", command=self.search_book,fg="red",bg="green")
        self.search_book_button.pack()

        self.delete_book_button = Button(self.main_menu_frame, text="Delete Book", command=self.delete_book,fg="red",bg="green")
        self.delete_book_button.pack()

        self.sort_book_button = Button(self.main_menu_frame, text="Sort Book", command=self.sort_book,fg="red",bg="green")
        self.sort_book_button.pack()

    def show_main_menu(self):
        self.login_frame.pack_forget()
        self.main_menu_frame.pack()

    def add_book(self):
        # Create a new window for adding a book
        add_book_window = Toplevel(self.root)
        add_book_window.title("Add Book")

        title_label = Label(add_book_window, text="Title:",fg="red",bg="green")
        title_label.grid(row=0, column=0)
        title_entry = Entry(add_book_window)
        title_entry.grid(row=0, column=1)

        author_label = Label(add_book_window, text="Author:",fg="red",bg="green")
        author_label.grid(row=1, column=0)
        author_entry = Entry(add_book_window)
        author_entry.grid(row=1, column=1)

        subject_label = Label(add_book_window, text="Subject:",fg="red",bg="green")
        subject_label.grid(row=2, column=0)
        subject_entry = Entry(add_book_window)
        subject_entry.grid(row=2, column=1)

        def add():
            title = title_entry.get()
            author = author_entry.get()
            subject = subject_entry.get()

            book = Book(title, author, subject)
            self.library.add_book(book)
            add_book_window.destroy()

        add_button = Button(add_book_window, text="Add", command=add,fg="red",bg="green")
        add_button.grid(row=3, columnspan=2)

    def show_all_books(self):
        # Create a new window to display all books
        all_books_window = Toplevel(self.root)
        all_books_window.title("All Books")

        for book in self.library.books:
            book_label = Label(all_books_window, text=f"Title: {book.title}, Author: {book.author}, Subject: {book.subject}",fg="red",bg="green")
            book_label.pack()

    def search_book(self):
        # Create a new window for searching a book
        search_book_window = Toplevel(self.root)
        search_book_window.title("Search Book")

        keyword_label = Label(search_book_window, text="Keyword:",fg="red",bg="green")
        keyword_label.pack()
        keyword_entry = Entry(search_book_window)
        keyword_entry.pack()

        def search():
            keyword = keyword_entry.get()
            matching_books = self.library.search_books(keyword)

            # Display matching books
            for book in matching_books:
                book_label = Label(search_book_window, text=f"Title: {book.title}, Author: {book.author}, Subject: {book.subject}",fg="red",bg="green")
                book_label.pack()

        search_button = Button(search_book_window, text="Search", command=search)
        search_button.pack()

    def delete_book(self):
        # Create a new window for deleting a book
        delete_book_window = Toplevel(self.root)
        delete_book_window.title("Delete Book")

        book_label = Label(delete_book_window, text="Enter the title of the book to delete:",fg="red",bg="green")
        book_label.pack()
        book_entry = Entry(delete_book_window)
        book_entry.pack()

        def delete():
            title = book_entry.get()
            matching_books = self.library.search_books(title)

            if len(matching_books) > 0:
                book = matching_books[0]
                self.library.remove_book(book)
                delete_book_window.destroy()
            else:
                error_label = Label(delete_book_window, text="Book not found.",fg="red",bg="green")
                error_label.pack()

        delete_button = Button(delete_book_window, text="Delete", command=delete,fg="red",bg="green")
        delete_button.pack()

    def sort_book(self):
        # Create a new window for sorting books
        sort_book_window = Toplevel(self.root)
        sort_book_window.title("Sort Book")

        sort_label = Label(sort_book_window, text="Sort by:",fg="white",bg="green")
        sort_label.pack()

        def sort_by_title():
            self.library.sort_books_by_title()
            sort_book_window.destroy()

        def sort_by_author():
            self.library.sort_books_by_author()
            sort_book_window.destroy()

        sort_by_title_button = Button(sort_book_window, text="Title", command=sort_by_title,fg="red",bg="green")
        sort_by_title_button.pack()

        sort_by_author_button = Button(sort_book_window, text="Author", command=sort_by_author,fg="red",bg="green")
        sort_by_author_button.pack()


# Create library catalog and sample books
library = LibraryCatalog()


# Create main window
root = Tk()
root.title("Library Catalog System")

# Create LibraryGUI instance
gui = LibraryGUI(root, library)

root.mainloop()
