# Author --------- Asif
# date ---------- 10/04/2022

import time
import datetime

class Library():


    def __init__(self, booklist, ownername):
        self.books = booklist
        self.owner_name = ownername
        self.book_lst_dict = dict.fromkeys(self.books, f'owns {self.owner_name}')
    
    # Not tested (In case needed to add new books)
    @classmethod
    def New_books(cls, new_list):
        new_books = dict.fromkeys(new_list, f'owns {cls.owner_name}')
        cls.books_lst_dict.append(new_books)
    

    def list_books(self):
        self.book_amount = len(self.books)
        print(f'Books available:\nAmount: [{self.book_amount}]\nNames:')
        for book, owner in self.book_lst_dict.items():
            print(f'{book} : {owner}')
    
    def lend_book(self, bookname, lender_name):
        self.lendBook = str(bookname)
        self.lender = str(lender_name)
        print("working up")
        time.sleep(2)
        with open("lend_records.txt",'a') as file:
            file.write(f"[{datetime.datetime.now()}] |{self.lendBook}| --Lended By-- {self.lender}")
        self.book_lst_dict.update({self.lendBook:self.lender}) # updating data changes into the dict
        print("We are done here! Happy reading! :D")
        print(f"Your Lended Book: {self.lendBook}")
        

    def donate_book(self, bookname, donater):
        self.book_donat = str(bookname)
        self.name = str(donater)
        print("working up")
        time.sleep(2)
        with open("donate_records.txt",'a') as file:
            file.write(f"[{datetime.datetime.now()}] |{self.book_donat}| --- {self.name}\n")
        self.book_lst_dict[self.book_donat] = self.name # Adding data changes into the dict
        print("Thank you for donating. Hope you have a good day! :D")
        print(f"Your Book: {self.book_donat}")

    def retruning_book(self, bookname):
        self.book_name= str(bookname)
        print("working up")
        time.sleep(3)
        with open("book_return.txt",'a') as file:
            file.write(f"Book: {self.book_name}, Returned in: [{datetime.datetime.now()}]\n")
        self.book_lst_dict[self.book_name] = self.owner_name
        print("Thank you for returning the book! :D")
        print(f"Your Book: {self.book_name}")

    def __str__(self):
        return "Library(List_of_books, Owners_name)"

    def start(self):
        print(f'''----------WECOLME TO {self.owner_name}'S LIBRARY----------\n''')
        while True:
            usr_response = int(input("1.See all avilable books\n2.Lend book,\n3.Donate Book,\n4.Quit (q)\n (respond in numbers 1, 2 or 3)\n"))
            if usr_response == 2:
                self.book = input("Please name the book you want:\n")
                self.name = input("Please tell us your name:\n")
                self.lend_book(self.book, self.name)
            elif usr_response == 3:
                self.book = input("Please name the book you want to donate:\n")
                self.name = input("Please tell us your name:\n")
                self.donate_book(self.book, self.name)
            elif usr_response == 1:
                self.list_books()
            elif usr_response == 4:
                print("Thank you for using, See you later! :D")
                break
            else:
                print("something went wrong please re-enter the information correctly this time!")


booklist = []
with open("books.txt", 'r') as file:
    for line in file.readlines():
        booklist.append(line)
    
myLibrary = Library(booklist,'ASIF')




    