# User Defined Functions!

# They give us repeatable power

# syntax
# def function_name():
#   code block to be executed on function call

# Simple function

def divi():
    print('='*50)

# def divi():
#     return '='*50
                        # only will print '=' because we are specifying in print(divi()) which is returning '='
# print(divi())
divi()

def greeting():
    print("Hello there traveler!!")

greeting()

#----------------------#

# ---- functions with parameters
# establish a required variable/value for our function

def personal_greeting(name):
    if isinstance(name, str):
        print(f"Hello, {name}, welcome to user defined functions!!")
    elif isinstance(name, int):
        print("This function is meant to be a greeting, please enter a real name")

personal_greeting("James")
personal_greeting(123546)

def get_username():
    user_input = input("What's your username? ")
    return user_input

# username = get_username()

# print(f"Welcome to our text based adventure game, {username}!! Get ready for an adventure")

# this function accepts no parameters, an we ask for user input inside of the function, this will only occur when the funtion is called

def whats_your_name():
    thing = input("What's your name traveler?")
    print(f"Let's welcome {thing}, the mysterious adventurer!")

# whats_your_name()
# print(whats_your_name()) # our print statement prints None to the screen because I haven't specified for my function to return anything, and so by default it returns a None value


# This function requires a parameter, instead of asking the user for that data inside of the function, we're expecting it to be given the function

def whats_ur_name2(thing):
    print(f"Let's welcome {thing}, the mysterious adventure")

# name = input("What's your name? ")
# whats_ur_name2(name)

def greet(anything):
    print(f"Hello, {anything}")

greet('tyler')

divi()

# --- more complex example

def class_info(instructor, students):
    print(f"This class us taught by {instructor}")
    class_size = len(students)
    print(f"It has {class_size} students")
    for student in students:
        print(student)

students_152 = ["Gamal", "Jeremaine", "Jasmine", "Vincent", "Eric", "Brian", "Liz", "Tyler"]

class_info("Travis", students_152)

def book_info(thing1, thing2): #(Author, title)
    print(f"this author is: {thing1}") # {Author}
    print(f"the title is: {thing2}") #{Title}

book_info("Neil Geiman", "Smoke and mirrors")

