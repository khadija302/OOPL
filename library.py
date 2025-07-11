class Library:
    def _init_(self, list_of_books, name):
        self.booksList = list_of_books
        self.name= name
        self.lendDict = {}

    def displayBooks(self):
        print(f"we have the following books in our library:{self.name}")
        for books in self.booksList:
            print(books)

    def lendBook(self, user, book):
        if book not in self.booksList:
            print("sorry, we do not have that book")
        elif book in self.lendDict:
            print("the book is already being used by {self.lendDict[book]}")
        else:
            self.lendDict[book] = user
            print("you can take the book now")

    def addBook(self, book):
        self.booksList.append(book)
        print(f"{book} has been added to thr book list")
        
    def returnBook(self, book):
        if book in self.lendDict:
            del self.lendDict[book]
            print("book has been returned")
        else:
            print("that book wasnt borrowed from us")

if __name__ == '__main__':
 books = Library([
     'python', 'kite runner', 'silent patient', 'harry potter', 'man called ove'
 ], "Let's Upskill")
 user_name = input("welcome to our library! please enter your name:")

 while True:
     print(f"\nHello {user_name}, welcome to the {books.name} library. please choose anoption:")
     print("1.Display Books\n2. lend a book\n3. add a book\n4. return a book\n5. quit")
     user_choice = input("enter your choice to continue:")

     if user_choice not in ['1', '2', '3', '4', '5']:
         print("please enter a valid option")
         continue

     if user_choice == '1':
      books.displayBooks()
     elif user_choice == '2':
      book = input("enter the name of the book you want to lend:")
      books.lendBook(user_name, book)
     elif user_choice == '3':
      book = input("enter the name of the book you want to add:")
      books.addBook(book)
     elif user_choice == '4':
      book = input("enter the name of the book you want to return:")
      books.returnBook(book)
     elif user_choice == '5':
      print(f"thank you for using the library, {user_name}. Goodbye!")
      break
 
 
        