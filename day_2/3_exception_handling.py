# Handling exceptions with Try and Except

# --- try : allows us to try a codeblock that will potentially raise an exception

# --- except : in the event that we do run into an exception(error), we can execute the code block without terminating our program with an error message

# try:
#     x = 1
#     print(x + 'person')
# except:
#     print("Hey we can't actually do that, I'm sorry to say")

# # Specific Exceptions : we can respond with a particular message for a specific kind of error

# try:
#     div = int(input("Give me a number to divide 10 by: "))
#     quotient = 10 / div
#     print(f"10 divided by {div} = {quotient}")
# except ValueError:
#     print("Make sure you enter a valid number! No letters!")
# except ZeroDivisionError:
#     print("Hey, you can't divide by 0!!")
# except:
#     print("Invalid input")

# --- else : additional code block that will only execute if the Try block is successful

while True:
    try:
        age = int(input("How old are you? "))
        birthday = age + 1
    except ValueError:
        print("Please respond with only numbers")
    except:
        print("Invalid response")
    else:
        print(f"On your birthday you will be {birthday} years old")
        break

# --- finally : additional code block that executes regardless of whether your try block succeeds or not

groceries = ['apples', 'bananas', 'walnuts', 'pear', 'bread']

while True:
    try:
        item = input('Which item would you like to remove? ')
        groceries.remove(item)
    except ValueError:
        print(f'It looks like you dont have item on list')
    except:
        print("Invalid input")
    else:
        print(f'Successfully removed {item} from the list!')
        break
    finally: # this block executes regardless of whether the try block succeeds or not
        print("Your current list")
        print('='*50)
        for item in groceries:
            print(item)