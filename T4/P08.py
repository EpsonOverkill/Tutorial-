class Book:
    def __init__(self):
        self.title = ""
        self.author = ""
        self.price = 0.0
    def get_details(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
    def print_details(self):
        print(f"Title: {self.title}, Author: {self.author}, Price: {self.price}")
book1 = Book()
book1.get_details("Wings of Fire", "A.P.J. Abdul Kalam", 599)
book1.print_details()
