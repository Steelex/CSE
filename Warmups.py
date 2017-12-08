# New python file: Warmups.py

# 12.4.17
# Write a python program
# which accpets the user's
# first name and last name
# and print them in reverse order
# with a space between them

# name = input("What is your first name?")
# print("Oh your name is %s?" % name)
# name_2 = input("What is your last name?")
# print("So your name is %s, %s?" %( name_2, name))
# print("Hello %s, %s. Have a good day." % ( name_2, name))
# works but there is a better way


# def reverse_order(first_name, last_name):
    # print("%s %s" % (last_name, first_name))
#     print(last_name + " " + first_name) # Concatenation

#   def reverse_order():
#   first_name = input("What is your first name?")
#   last_name = input("What is your last name?")
#   print("%s %s" % (last_name, first_name))


# ""Warmup #2
# Write a function called "Happy_bday"
# that "sings" (prints)
# the Happy Birthday Song
#
# It must take one parameter called "name"
#"""

# def happy_bday(name):
#    print("Happy Birthday to you,")
#    print("Happy Birthday to you,")
#    print("Happy Birthday dear" % name)
#    print("Happy Birthday to you!")

# 12.5.17
# """Write a function called add_py
# that takes one parameter called "name"
# and prints out name.py
# example:
# add_py("I_ate_some") == "I_ate_some.py"
# """

#def add_py(name):
#    print("%s.py" % name)
# Solution One
#    print(name + ".py")
# Solution Two


# 12.6.17
# """Write a function called "add"
# which takes three parameters
# and prints the sum of the numbers
# """


# def add(num1,num2,num3):
#     print(num1 + num2 + num3)


# add(90, 900, 9000)


# 12.7.16
# Write a function called "repeat"
# that takes one parameter (string)
# and prints it three times.
#
# example:
# repeat("Hello") Prints:
# hello
# hello
# hello

# def repeat(string):
#     print(string)
#     print(string)
#     print(string)

#    for x in range(3):
#        print(string)

# 12.8.17

"""
Write a function called "date"
that takes in three parameters,
"month", "day", and "year" and
prints out the date, separated by a "/"

example:
date("12", "8", "17" == "12/8/17"
Expertmode:
date(12, 8, 17) == "12/8/17"
"""


def date(month, day, year):
    print(str(month) + "/" + str(day) + "/" + str(year))

print(12, 8, 17)