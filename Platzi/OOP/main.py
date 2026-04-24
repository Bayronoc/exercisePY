class Book:
    def __init__(self, title, author, ISBN, available):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.available = available


    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.ISBN}) - {'Available' if self.available else 'Not Available'}"

if __name__ == "__main__":
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "978-0-7432-7356-5", True)
    book2 = Book("To Kill a Mockingbird", "Harper Lee", "978-0-06-112008-4", True)
    book3 = Book("1984", "George Orwell", "978-0-452-28423-4", False)
    book4 = Book("Pride and Prejudice", "Jane Austen", "978-0-19-953556-9", True)

    catalog = [book1, book2, book3, book4]

    for book in catalog:
        print(book)