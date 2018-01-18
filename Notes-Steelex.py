import random
'''
# print("Hello World")

# i like pickles

# print(3+5)
# print(5-3)
# print(5*3)
# print(6/2)
# print(3 ** 2)

# print()
# Creates a blank line
print("See if you can figure this out")
print(15 % 5)

# Variables
car_name = "Mobile Legends"
car_type = "Tesla Model 3"
car_cylinders = 8
car_mpg = 9000.1

# inline printing
print("My car is the %s." % car_name)
print("My car is the %s. It is a %s" % (car_name, car_type))

# Taking Input
name = input("What is your name?")
print("Hello %s." % name)
# print(name)
age = input("What is your age? ")
print("%s?! That old? You belong in a museum." % age)
# Change to file

print()


def print_hw():

    print("Hello World")


print_hw()


def say_hi():

    print("Hello %s." % name)


print("I hope you have a fantastic day.")


print("Stranger Danger")


def birthday(age):
    age += 1

age = age + 1


print("Stranger Danger is 15. Next Year:")
birthday(15)

# birthday (15)

# press Ctrl-A and Ctrl /
# to comment old code

print()


def f(x):

    return x**5 + 4 * x ** 2 + 4-17 * x**2 + 4


print(f(3))
print(f(3) + f(5))

# if statements


def grade_calc(percentage):

    if percentage >= 90:
        return "A"
    elif percentage >= 80 and percentage < 90: # else if
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    else:
        return "F"

# Loops


# for num in range(5):
# print(num + 1)

# for mystery in "Hello World":
#    print(mystery)

a = 1
while a < 10:
    print(a)
    a += 1

    response = ""
# while response !="Hello":
#        response = input("Say \"Hello\"")

print()

print("Hello \nWorld")

# \n means newline

print(random.randint/(0, 6))

# comparisons
print(1 == 1) # Two equal signs compare
print(1!= 2) # One is not equal to 2
print(not False) # This prints true
print(1 == 1 and 4<=5)
print(1 < 0 or 5 > 1)

# Recasting
# c = '1'
# print(c == 1) # False is -C is a string, 1 is an int
# print(int(c) == 1) # True - Compares two ints
# print(c == str(1)) # True - Compares two strings
'''

# Lists
the_count = [1, 2, 3, 4, 5]
shopping_list = ["Noodles", "Eggrolls", "Milk", "Rice", "Soda"]

print(shopping_list[2])


print(len(shopping_list))

# Going through a list
for item in shopping_list:
    print(item)

for num in the_count:
    print(num * 2)

    len(shopping_list)  # GIves me the length of the list
    range(3) # Gives a list of the numbers 0 thourg 2
    range(len(shopping_list)) #A list of every indix in a list

    for num in range(len(Shopping_list)):
        item = shopping_list [num]
        print ("The item %d is @d" % (num, item))

# turn ino a list
strl = "Hello Class"
listOne = list(strl)
print(listOne)
listOne[11] = '.'
print(listOne)
print(listOne)