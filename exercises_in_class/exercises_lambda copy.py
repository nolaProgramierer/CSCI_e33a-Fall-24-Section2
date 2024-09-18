
pianos = {"Steinway": 85000, "Bechstein": 95000, "Steingräber": 105000, "Rönisch": 65000, "Blüthner": 92000}
list1 = [1, 2, 3, 4]

#----------------------------------------------
# 1) Write a method to increase an argument by 10
def add_ten(num):
    return num + 10
print(add_ten(10))

#-----------------------------------------------
# 2) Write the same method as a lambda

#-----------------------------------------------
# 3) Write the above lambda without passing in an argument to the function variable

#-----------------------------------------------
# 4) Write a lambda which sums 3 arguments

#-----------------------------------------------
# 5) Write a lambda which multiplies the argument by 10

#-----------------------------------------------------
# What's going on with this function?
def my_func(n):
    return lambda a : a * n

mydoubler = my_func(2)
print(mydoubler(11))

#---------------------------------------------------
# 7) Finding expensive pianos with a conventional loop
def expensive_piano(list):
    result = []
    for piano in list:
        if list[piano] > 94000:
            result.append(piano)      
    return result
print(expensive_piano(pianos))

# 8) Write the above function using a lambda


