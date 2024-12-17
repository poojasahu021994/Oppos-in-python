class Book:
    price=150
    def __init__ (self,author,pages):
        self.author=author
        self.pages=pages
    @classmethod
    def update_price(cls,price):
        cls.price=price

    def show_details(self):
        print(self.author) 
        print(Book.price)
        print(self.pages)
obj=Book('Neeraj',450)
obj.show_details()
obj.update_price(200)
obj.show_details()              