class Library:
    book_list = []  

    @classmethod
    def entry_book(cls, book):
        cls.book_list.append(book)

    @classmethod
    def view_all_books(cls):
        if not cls.book_list:
            print("No books available in the library.")
        for book in cls.book_list:
            book.view_book_info()

class Book:
    def __init__(self, book_id, title, author, availability=True):
        self.__book_id = book_id
        self.__title = title
        self.__author = author
        self.__availability = availability
        Library.entry_book(self)

    def borrow_book(self):
        if self.__availability:
            self.__availability = False
            print(f"The book '{self.__title}' has been borrowed.")
        else:
            print(f"The book '{self.__title}' is already borrowed.")

    def return_book(self):
        if not self.__availability:
            self.__availability = True
            print(f"The book '{self.__title}' has been returned.")
        else:
            print(f"The book '{self.__title}' was not borrowed.")

    def view_book_info(self):
        availability_status = "Available" if self.__availability else "Not Available"
        print(f"Book ID: {self.__book_id}, Title: {self.__title}, Author: {self.__author}, Availability: {availability_status}")

    def get_book_id(self):
        return self.__book_id

def main_menu():
    while True:
        print("\nLibrary Menu:")
        print("1. View All Books")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            Library.view_all_books()
        elif choice == "2":
            book_id = input("Enter the Book ID to borrow: ")
            book = next((b for b in Library.book_list if b.get_book_id() == book_id), None)
            if book:
                book.borrow_book()
            else:
                print("Invalid Book ID. Please try again.")
        elif choice == "3":
            book_id = input("Enter the Book ID to return: ")
            book = next((b for b in Library.book_list if b.get_book_id() == book_id), None)
            if book:
                book.return_book()
            else:
                print("Invalid Book ID. Please try again.")
        elif choice == "4":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")


book1 = Book("101", "Python Programming", "John Doe")
book2 = Book("102", "Data Science Essentials", "Jane Smith")
book3 = Book("103", "Machine Learning Basics", "Alan Turing")


main_menu()


