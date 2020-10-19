from user.models import TBook
class Book:
    def __init__(self,id,count):
        self.id = id
        book = TBook.objects.get(book_id=id)
        self.count = count
        self.name = book.book_name
        self.image_path = book.book_image_path
        self.price = book.book_dprice
class Car:
    def __init__(self):
        self.book_List = []
    def add_book(self, id, count=1):

        for i in self.book_List:
            if id == i.id:
                i.count = int(count)+int(i.count)
                break
        else:
            book = Book(id,count)
            self.book_List.append(book)
    def remove_book(self,id):
        for i in self.book_List:
            if id == i.id:
                self.book_List.remove(i)
    def update_book(self,id,count):
        for i in self.book_List:
            if id == i.id:
                i.count = count
            break


