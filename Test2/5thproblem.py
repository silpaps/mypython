class Book():
    def show(self,name,author,year):
        self.n=name
        self.a=author
        self.y=year
        print(self.n,self.a,self.y)
class HarryPotter(Book):
    def show(self,name,author,year):
        self.n=name
        self.a=author
        self.y=year
        print("fav book is Harrypotter")
        print(self.n,self.a,self.y)

h=HarryPotter()
h.show("harry Potter","J K Rowling",1997)