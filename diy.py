def display_message():
    """What chapet 8 is about"""
    print("defining functions".title())
display_message()

def favorite_book(title):
    """titles of my favorite books"""
    print("One of my favorite books is " + title.upper())
favorite_book("the infinite game")
favorite_book("seven habits of highly effective people")
favorite_book("the goal")
favorite_book("twisted series (love, hate, game)")
# TIY 2
def make_shirt(size, text):
    """tells preferred shirt size and text prints"""
    print("\nI prefer " + size.title() + " and I want the front to have " + text.upper() + " printed on it")
make_shirt('medium', 'go big, or go home!')
# 8.1
def make_shirt(size= 'medium', text= 'Great!'):
    """tells preferred shirt size and text prints"""
    print("\nI prefer " + size.title() + " and I want the front to have " + text.upper() + " printed on it")
make_shirt()
# 8.2
def make_shirt(text, size= 'large'):
    """tells preferred shirt size and text prints"""
    print("\nI prefer " + size.title() + " and I want the front to have " + text.upper() + " printed on it")
make_shirt(text= 'I love Python!')
# 8.3
def make_shirt(size, text= 'I love python!'):
    """tells preferred shirt size and text prints"""
    print("\nI prefer " + size.title() + " and I want the front to have " + text.upper() + " printed on it")
make_shirt(size= 'medium')
make_shirt(size= 'large')
make_shirt(size= 'small', text= 'Go high!')
# 8.4
def describe_city(city, country= 'usa'):
    """naming cities and countries"""
    print(city.title() + " is in " + country.upper())
describe_city('new York')
describe_city('chicago')
describe_city('gatlinburg')
describe_city(city= 'arbedeen', country= 'Scotland')
