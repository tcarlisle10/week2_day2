# In python we have two different types of scope. Global scope and local scope

# the scope determines what variables are accessible

# Global scope is anywhere outside of a function or a for loop

# Global Variable
x = 7 # Variables defined on a global scope can be accessed from anywhere within our code
a = "words"
alist = ["item1", "item2", "item3"]

if x:
    print(x)

# Local scope is created inside of a function (or a for loop)

def local_func():
    y = 10 # local variable, only accessible inside of this function

    # print(x) can be accessed because 'x' is a global variable

local_func()
# print(y)  'y' is not defined because it is only in the function

books = []

def add_to_library(author, title):
    book = [author, title]
    books.append(book)
    print(books)

add_to_library("J.K. Rowling", "Harry Potter")

def display_books():
    for book in books:
        # div()
        print(f"title: {book[1]}")
        print(f"Author: {book[2]}")
        # div()