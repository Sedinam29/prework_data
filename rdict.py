# def build_person(first_name, last_name):
#     """Return a dictionary of information about a person."""
#     person = {'first': first_name, 'last': last_name}
#     return person
# musician = build_person('jimi', 'hendrix')
# print(musician)

# def build_person(first_name, last_name, age= ''):
#     """Return a dictionary of information about a person."""
#     person = {'first': first_name, 'last': last_name}
#     if age:
#         person['age'] = age
#     return person
# musician = build_person('jimi', 'hendrix', age=27)
# print(musician)

# DICT FROM VIDEO
# def giveMeMyGroceries(thing_to_add):
#     grocery_list = ['grapes', 'oranges', 'banana']
#     grocery_list.append(thing_to_add)
#     return grocery_list
# print(giveMeMyGroceries('spaghetti'))

def giveMeMySports(name_to_add):
    Sport_dict = {'soccer': ['Real Madrid', 'Juventus', 'PSG'],
                  'basketball': 'Cavaliers',
                   'baseball': 'Marlins'}
    Sport_dict['wrestling']= name_to_add
    return Sport_dict
print(giveMeMySports(['Undertaker', 'The Rock', 'Roman Reigns']))