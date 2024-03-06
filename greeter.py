# the text at 2 is a comment called a docstring. it describes what the function does.
# docstrings are enclosed in 2 triple quotes
# the 3 is the only actual code in the body of the function
# eg. greet_user has just one job: print hello
# the 4 is the function call. write the namde of the function, followed by any necessary info
def greet_user():
    """Display a simple greeting."""
    print("Hello!")
greet_user()
# Passing info to a function: username here is a parameter

def greet_user(username):
    """Display a simple greeting."""
    print("Hello, " + username.title() + "!")
greet_user('Jesse')
greet_user("Sedi")
greet_user("Bebe")
greet_user("Blesslord")
# Arguments and Parameters
# A parameter is a piece of information the function needs to do its job
# An Argument (Jesse) a piece of info passed from a function call to a function

# Passing Arguments
# positional arguments and Multiple function calls: 
def describe_pet(animal_type, pet_name):
    """Display information about a pet"""
    print("\nI have a " + animal_type)
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet('cat', 'lucy')
describe_pet('dog', 'lundi')
# pay attention to the ordering of terms as it may affect the meaning. Know what you're asking for and remember to order them as needed
# A Keyword Argument:they free you from having to worry about ordering ypur arguments
def describe_pet(animal_type= 'cat', pet_name= 'Lucy'):
    """Display information about a pet"""
    print("\nI have a " + animal_type)
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
# describe_pet()
# or
describe_pet(animal_type= 'cat', pet_name= 'Lucy')
# Default values: any parameter without a default value comes before the P with default value. allows correct interpretation
def describe_pet(pet_name, animal_type='dog'):
 """Display information about a pet."""
 print("\nI have a " + animal_type + ".")
 print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet(pet_name='willie')
