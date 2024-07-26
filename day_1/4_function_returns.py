# the goal the many functions is produce something

# --- take something in as an argument
# --- manipulate it/do something to/with it
# --- return the output
def div():
    print('='*50)




name = "Travis"

data = type(name) # the value is returned but not printed to the screen, so we dont get to see it
print(data)

print(type(name))

#  simple function with a return statement

def addition(a, b):
    return a + b 

# def addition1(a, b):  # this will do the same thing, but the above is easier to write
#     ans = a + b
#     return ans

total = addition(5, 5)
print(total)

# this also works
print(addition(10, 10))

addition(1, 20) # here nothing prints to the screen because data is returned, but we're not doing anything with it
print(addition(25, 25)) # here we're doing something with the data. printing it

div()
#----------------------------------#

# doubler function that takes in a list of numbers and doubles each value in the list, then returns a new list

def doubler(nums):
    doubled_nums = []
    for num in nums:
        doubled_num = num * 2
        doubled_nums.append(doubled_num)

    return doubled_nums

my_nums = [1,2,3,4,5,6,7,8,9]
dnums = doubler(my_nums)
print(dnums)

#------------------------------#

# --- a function with no return

def greet_card(name): # a function wihtout a return statement by default returns None value
    print(f"Have a nice day, {name}!")

card_message = greet_card("Travis")
print(card_message)