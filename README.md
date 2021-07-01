# Python Practice Questions

### 1. Declare a function called Username, that takes one arg as str, and return the name
```python
def username(name):
    return name

name_input = input("What is your name?  ")
print(username(name_input))
```
- Doesn't **need** the user prompt, just hard code a name in the print line.
### 2. Declare a list with numbers 1 to 5. iterate through the list and display the list
```python
num_list = [1, 2, 3, 4, 5]
for i in num_list:
    print(i)
```
### 3. AND, &&, & or ==. Which returns the Boolean value?
`==`
### 4. What is the difference between a list and a tuple?
A list [ ] is mutable and a tuple ( ) is immutable
### 5. Can we add an element to a list? Can we add an element to a tuple? Can the elements in tuples be different types?
Yes to a list (mutable), no to a tuple (immutable), yes to different types
### 6. Create a dict with key:value pairs of first_name and last_name
```python
dict = {
    'first_name': 'Tom',
    'last_name': 'Williams'
}
```
### 7. Add course to the below dictionary.
```python
dict = {
    'first_name': 'Tom',
    'last_name': 'Williams'
}

dict['Course'] = 'DevOps'
```
### 8. Create a class called student, initialise the class and create an object of the class
```python
class Student():
    def __init__(self):
        pass

student = Student()
```
### 9. Create 2 functions that take 2 args each. Function one called add_values, function 2 called subtract_values. Return operations + and -
```python
def add_values(a, b):
    return a + b

def subtract_values(a, b):
    return a - b
```
### 10. Declare a dictionary with three shopping items, with cost - eggs: £1.20, milk: £2.30 and bread: £1.00. Write a function that returns the total value
```python
shopping_list = {
    'eggs': 1.2,
    'milk': 2.3,
    'bread': 1.0
}

def total_value(dict):
    list = dict.values()
    total = sum(list)
    return f"The total value is £{total:.2f}."

print(total_value(shopping_list))
```
### 11. Prompt the user to enter an integer, declare a function that checks if the number is odd or even. Display back to the user with the message "the number you chose is odd/even"
```python
num = int(input("Please input an integer.  "))

def odd_check(num):
    if num % 2 == 0:
        print(f"Your number {num} is even.")
    else:
        print(f"Your number {num} is odd.")

odd_check(num)
```
### 12. select the correct syntax- 1 -super.__init(). 2- super()__init(). 3 super().__init(). 4 - Super().__init __()
- 4 `super().__init__()`
### 13. Declare a tuple with three vals of choice. Iterate through tuple and display values.
```python
list = (1, 2, 'three')

for i in list:
    print(i)
```
### 14. Create a class called Student, with one method called student_data which returns student name. Create a class called DevOpsStudent to inherit student class and print student name
```python
class Student():
    def __init__(self):
        self.name = "Tom"

    def student_data(self):
        return self.name

class DevOpsStudent(Student):
    def __init__(self):
        super().__init__()

smart_student = DevOpsStudent()
print(smart_student.student_data())
```
### 15. Declare a variable called city, declare a method that takes 'city' as an arg and value of city is "London". The method returns True for London and False for anything else
```python
city = "London"

def city_check(city):
    if city == "London":
        return True
    else:
        return False

print(city_check(city))
```
### 16. import sys, import math. Print random method. Create function that takes two args and gives %
```python
import random
import sys
import math

print(random.randint(0, 10))

def percent(a, b):
    return a / b * 100

print(percent(5, 10))
```