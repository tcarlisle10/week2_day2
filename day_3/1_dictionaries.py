# Python Dictionaries

# Mutable data type: we can add, mutate, and remove data from them
# collection of key-value pairs : like a labeled drawer - each drawer has it's own contents

# key
# --- must be unique
# --- typically keys are string, but they can be IMMUTABLE data types (strings, numbers, tuples)

# values : can be any data type

# dictionaries are flexible and can be changed over time

# we can use keys to access the data contained in it's value

# Empty dictionary
# empty_list = []

student_grades = {
    "Alice" : 85,
    "Bob" : 92,
    "Charlie" : 78
}

# Accessing elements within a dictionary

# we access values in a dictionary by specifying the key in square brackets
print(student_grades["Alice"])

alice_grade = student_grades["Alice"]
print(alice_grade)

# KeyErrors can occur when trying to access a dictionary at a key that doesn't exist
# tyler_grade = student_grades['tyler']

# can also access dictionaries with .get()

# syntax for .get(<key>, <default return if the key we're looking for isn't found>)

david_grade = student_grades.get("David", "Not found")
print(david_grade)

# using the .get() method prevents us from getting a KeyError