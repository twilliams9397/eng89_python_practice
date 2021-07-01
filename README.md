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
### 12 select the correct syntax- 1 -super.__init(). 2- super()__init(). 3 super().__init(). 4 - Super().__init __()
- 4 `super().__init__()`
### 13 Declare a tuple with three vals of choice. Iterate through tuple and display values.
```python
list = (1, 2, 'three')

for i in list:
    print(i)
```