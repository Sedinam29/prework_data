#  RETURN VALUES: function does a lot combing. the return stat. takes a value 
#from inside a function and sends it back to the line that called the function.
# allows you to move alot of program work into functions for simplification
def get_formatted_name(first_name, last_name):
    """returns a full name, neatly formatted"""
    full_name = first_name + ' ' + last_name
    return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print(musician)
# when you call a function that returns a value, you need to provide a 
# variable where the return value can be stored. In this case, the returned value is stored in the variable musician

# MAKING AN ARGUMENT OPTIONAL
def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
       full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
       full_name = first_name + ' ' + last_name
    return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print(musician)
