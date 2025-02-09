from helper import div

# Looping/Iterating over a dictionary

student_grades = {
    "Alice" : 85,
    "Bob" : 92,
    "Charlie" : 78
}

# Using .items() : return each key-value pair as a tuple

items = student_grades.items()
print(items)

# iterating over key-value pairs with .items()

for student, grade in student_grades.items():
    print(f"Key : {student}, Value : {grade}")

div()

for thing in student_grades.items():
    print(thing)
    print(f"{thing[0]}: {thing[1]}")

div()
# using .keys() : iterates over only the keys in a dictionary

for key in student_grades.keys():
    print(key)
    print(f"Key : {key}, Value : {student_grades[key]}")

div()

# using .values() : iterates over only the values stored in a dictionary

list_of_grades = []

for value in student_grades.values():
    print(value)
    list_of_grades.append(value)

print(sum(list_of_grades)/len(list_of_grades)) # This should give average

div()

chips = {
    "Cheeto" : "Flamin Hot",
    "Dorito" : "Cool Ranch",
    "Takis" : "Fuego",
    "Miss Vickies" : "Spicy Dill Pickle"
}

# looping over keys
# .key()

print("Major chip brands")
print("------------")
for key in chips.keys():
    print(f"Key: {key}")
    print(f"Value: {chips[key]}")

# looping over values
# .values()

print("\nFlavors")
print('---------')
for value in chips.values():
    print(f"Flavor: {value}")

div()

# looping over keys and values at the same time

print("\nMy favorite flavor per chip")
print("--------------")

for key, value in chips.items():
    print(f"My favorite {key} flavor is {value}")

