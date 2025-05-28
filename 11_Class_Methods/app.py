# Create a class Book with a class variable total_books. Add a class method increment_book_count() to increase the count when a new book is added.

class Book:
    total_books = 0

    def __init__(self, title, author):
        self.title = title
        self.author = author
        Book.increment_book_count()

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

    def show_info(self):
        print(f"Title: {self.title}, Author: {self.author}")

book1 = Book("Jannat Kay Pattay", "Nemrah Ahmed")
book2 = Book("Peer-e-Kamil", "Nemrah Ahmed")

print("Total Books:", Book.total_books)
