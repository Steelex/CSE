print("Hello World")

# i like pickles

print(3+5)
print(5-3)
print(5*3)
print(6/2)
print(3 ** 2)

print() # Creates a blank line
print("See if you can figure this out")
print(15 % 5)

# Variables
car_name = "Mobile Legends"
car_type = "Tesla Model 3"
car_cylinders = 8
car_mpg = 9000.1

#inline printing
print("My car is the %s." % car_name)
print("My car is the %s. It is a %s" % (car_name, car_type))

# Taking Input
name = input("What is your name?")
print("Hello %s." % name)
#print(name)
age = input("What is your age? ")
print("%s?! That old? You belong in a museum." % age)

# Change to file

def print_hw():
    print("Hello World")


print_hw()


def say_hi(name):
    print("Hello %s." % name)
    print("I hope you have a fantastic day.")


say_hi("Stanger Danger")


def birhtday(age):
    age += 1    # age = age + 1


say_hi("Stranger Danger")
print("Stranger Danger is 15. Next Year:")
birthday(15)
