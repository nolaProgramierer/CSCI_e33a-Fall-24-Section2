
cars = [
    {"brand": "BMW", "trim": "328i", "color": "gray", "price": 38900},
     {"brand": "Mercedes", "trim": "350E", "color": "white", "price": 89000},
      {"brand": "Porsche", "trim": "911", "color": "orange", "price": 95000},
       {"brand": "Kia", "trim": "Sorento", "color": "blue", "price": 30900},
        {"brand": "Toyota", "trim": "Sienna", "color": "gray", "price": 51200},
]

#Find orange car
def find_orange1(obj_list):
    for obj in obj_list:
        if obj["color"] == "orange":
            print(obj)

find_orange1(cars)

# -OR-

#Find orange car
def find_orange2(obj_list):
    for obj in obj_list:
        if obj.get("color") == "orange":
            print(obj)

find_orange2(cars)

# Find cars that are less than $40000 (comprehension list)

# Find most expensive car

#------------------------------------------------------

pianos = {"Steinway": 85000, "Bechstein": 95000, "Steingräber": 105000, "Rönisch": 65000, "Blüthner": 92000}
my_pianos = []

#1 Return a list of dictionary keys

#2 Return a list of dictionary keys (another way)
# Return a list of all piano brands

# 3 Iterate through all the values
# Return a list of all piano prices

#4 Iterate through all the values
# Return a list of all piano prices (most common method)

#5 Print key-value pairs as tuples using items()

#6 Return all key, value pairs without using items()

#7 Unpacking dictionary keys into a list

#8 Unpacking dictionary values into a list

#9 Unpacking dictionary items into a list

# 10 Find list of pianos above 85000

# 11 Find list of pianos above 85000

#12 List all pianos above 85000 using list comprehension

#13 Find the brand name of the most expensive piano

# 14 Find piano brand without an umlaut
# umlauts = "[ü]"

# 15 Using a List comprehension




    
