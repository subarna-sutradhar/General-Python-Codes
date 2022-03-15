class libmast:
    accno = 0
    bookname = " "
    author = " "
    pages = 0
    price = 0
    def addata(self):
        self.accno = int(input("Enter the accession number: "))
        self.bookname = input("Enter the name of the book: ")
        self.author = input("Enter the name of the author: ")
        self.pages = int(input("Enter the number of pages: "))
        self.price = int(input("Enter the price: "))

    def shdata(self):
        print("The accno number is ",self.accno)
        print("The bookname is ",self.bookname)
        print("The author_name is ",self.author)
        print("The number of pages is ",self.pages)
        print("The price is ",self.price)

lib = libmast()
lib.addata()#after this we can also write lib.shdata()
print(lib.accno, lib.bookname, lib.author, lib.pages, lib.price)