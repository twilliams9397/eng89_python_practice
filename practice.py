# Q1

# def username(name):
#     return name
#
# name_input = input("What is your name?  ")
#
# print(username(name_input))

# Q2

# num_list = [1, 2, 3, 4, 5]
# for i in num_list:
#     print(i)

# Q3 in README
# Q4 in README
# Q5 in README

# Q6 Create a dict with key:value pairs of first_name and last_name

# dict = {
#     'first_name': 'Tom',
#     'last_name': 'Williams'
# }

# Q7 Add course to the below dictionary.
# dict = {
#     'first_name': 'Tom',
#     'last_name': 'Williams'
# }
#
# dict['Course'] = 'DevOps'

# Q8 Create a class called student, initialise the class and create an object of the class

# class Student():
#     def __init__(self):
#         pass
#
# student = Student()

# Q9 Create 2 functions that take 2 args each. Function one called add_values, function 2 called subtract_values. Return operations + and -

# def add_values(a, b):
#     return a + b
#
# def subtract_values(a, b):
#     return a - b

# Q10 Declare a dictionary with three shopping items, with cost - eggs: £1.20, milk: £2.30 and bread: £1.00. Write a function that returns the total value

# shopping_list = {
#     'eggs': 1.2,
#     'milk': 2.3,
#     'bread': 1.0
# }
#
# def total_value(dict):
#     list = dict.values()
#     total = sum(list)
#     return f"The total value is £{total:.2f}."
#
# print(total_value(shopping_list))

# Q11 Prompt the user to enter an integer, declare a function that checks if the number is odd or even. Display back to the user with the message "the number you chose is odd/even"

# num = int(input("Please input an integer.  "))
#
# def odd_check(num):
#     if num % 2 == 0:
#         print(f"Your number {num} is even.")
#     else:
#         print(f"Your number {num} is odd.")
#
# odd_check(num)

# Q12 in README

# Q13 Declare a tuple with three vals of choice. Iterate through tuple and display values.

list = (1, 2, 'three')

for i in list:
    print(i)
