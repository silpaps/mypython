class Book:
    lib_name="vvvvvv"
    def __init__(self,book_name, author, pages):
        self.b=book_name
        self.a=author
        self.p=pages
    def printval(self):
        print("libraryname is",Book.lib_name)
        print("book is", self.b)
        print("author is", self.a)
        print("no of pages is", self.p)
b=Book("aaaaaa","ccccc",320)
b.printval()