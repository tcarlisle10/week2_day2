def div():
    print('~'*50)

#------------------------------#
# Removing key-value pairs from a dictionary

student_grades = {
    "Alice" : 85,
    "Bob" : 92,
    "Charlie" : 78
}

# using .pop() : removes the specified key and return it's value. If the key doesn't exist it will return a default value the we specify

div()

bob_grade = student_grades.pop("Bob", "Not found")
print(bob_grade)
print(student_grades)

# Using .popitem() removes and returns the last key-value pair as a tuple
last_item = student_grades.popitem()
print(last_item)
print(student_grades)

div()

# using del
# delete key-value pair from the dictionary, with no return value

del student_grades["Charlie"]
print(student_grades)

# Using .clear() : removes all key-value pair from the dictionary, leaving it empty

student_grades.clear()
print(student_grades)