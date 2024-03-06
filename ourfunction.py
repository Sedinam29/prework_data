# # from video
# cars = ["audi", "ferrari", "honda", "Toyota"]

# # def car_adder(hot_wheels):
# #     """add cars to list with promo"""
# #     if hot_wheels[0].lower() in 'abcdefg':
# #         print('This car starts with A-G')
# #         cars.append(hot_wheels)
# #     else:
# #         print("This car starts with H-Z and we don't have promos for it")
    
# # car_adder('BMW')
# # car_adder('chrysler')
# # car_adder('mercedes')

# # print(cars)

# # def car_adder(hot_wheels):
# #     """add cars to list with promo"""
# #     if hot_wheels[0].lower() in 'abcdefg':
# #         print('This car starts with A-G')
# #         cars.append(hot_wheels)
# #     else:
# #         print("This car starts with H-Z and we don't have promos for it")
# #     for car in cars:
# #         if len(car) <= 5:
# #             cars.remove(car)
# #             print(f'{car} was not added because it has too few characters')

    
# # car_adder('BMW')
# # car_adder('chrysler')
# # car_adder('mercedes')

# # print(cars)
# groceries = ['apples', 'banana', 'orange', 'pear']
# def car_adder(hot_wheels, target_list):
#     """add cars to list with promo"""
#     if hot_wheels[0].lower() in 'abcdefg':
#         print('This car starts with A-G')
#         target_list.append(hot_wheels)
#     else:
#         print("This item starts with H-Z and we don't have promos for it")
#     # for car in cars:
#     #     if len(car) <= 5:
#     #         cars.remove(car)
#     #         print(f'{car} was not added because it has too few characters')

    
# car_adder('BMW', cars)
# car_adder('chrysler', cars)
# car_adder('mercedes', cars)
# car_adder('cinnamon', groceries)
# car_adder('pawpaw', groceries)

# print(cars)
# print(groceries)
# RETURNING THINGS: allows us to use the data 
# the part that the machine spits out 
def addTwo(num):
    return num + 2
print(addTwo(3))

def addTwo(num):
    return num + 2

def addThree(num):
    return num + 3
print(addThree(addTwo(4)))
# High order functions
def namePrinter(first, middle, last):
    return f"The name's {last}, {first} {middle} {last}"

print(namePrinter('Jes John', 'Selom', 'Tetedje'))
# defaulting to nothing makes it excusable if there are no arguments for a parameter
def namePrinter(first, last, middle= ''):
    return f"The name's {last}, {first} {middle} {last}"

print(namePrinter('Jes John', 'Tetedje'))

# using good variabke names helps you remember easily
# functions are everywhere in languages