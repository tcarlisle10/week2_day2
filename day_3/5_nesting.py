from helper import div

# Nesting dictionaries and list

# Lists inside of dictionaries 

pet_names = {
    "Dog" : ["Toast", "Oreo", "Punkin", "Pinky", 'Dogue', 'Rover', 'Rex', 'Pluto', 'Fido', 'Trouble'],
    "Cats" : ["Mittens", 'Ziggy', 'Hot Pocket', 'Miso', 'Cat Keisha', 'Randolf', 'Snowball', 'Smokey'],
    "Hamsters" : ['Hamtarro', 'Lightening', 'Nugget', 'Cheddar', 'Hammie', 'Turbo'],
    "Lizard" : 'Lizzy'
}

# pet_names['Lizard'] = ['Lizzy', 'Izzy'] # added Izzy to Lizards

# print(pet_names['Cats'][3])

miso_index = pet_names['Cats'].index("Miso") # finding the index of Miso
print(miso_index)
print(pet_names['Cats'][3]) # we can chain keys and indices together, similar to nested lists

div()

for pet, names in pet_names.items():
    print(f"\nCommon {pet} names: ")
    if isinstance(names, list):
        for name in names:
            print(name)
    else:
        print(names)

div()

books = [
    {'Title': 'Diary of a Wimpy Kid', 'Author': 'Jeff Kiney', 'Genre': 'YAF'},
    {'Title': 'Rich Dad Poor Dad', 'Author': 'Robert Kiwaske', 'Genre': 'Self Help'},
    {'Title': 'Dune', 'Author': 'Frank Herbert', 'Genre': 'Science Fiction'}
]

# We can chain indices and keys after one another
print(books[0]['Author'])

div()

for book in books:
    # print(book)
    print(f"{book['Title']} is written by {book['Author']}")

div()

user = {
    'dk@email.com' : {'username': 'dylank', 'password': '12345', 'likes': ['dogs', 'tacos']},
    'tp@email.com' : {'username': 'traviicii', 'password': '67890', 'likes': ['key lime pie', 'long walks on the beach']},
    'toast@email.com' : {'username': 'toaster-struddle', 'password': 'imadawg', 'likes': ['treats', 'walks']}
}

print(user['tp@email.com']['likes'][0])


# Creating a login function using the user 'database' dictionary above.
def login(user_dict):
    while True:
        try:
            email = input("What's your email: ")
            password = input("Enter your password: ")
            user = user_dict[email]
            if password != user['password']:
                raise ValueError
        except Exception as e:
            print(e)
            print('Invalid email or password')
        else:
            print(f"Welcome back {user['username']}")
            break

login(user)