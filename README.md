# Python Practice Questions

### 1. Declare a function called Username, that takes one arg as str, and return the name
```python
def username(name):
    return name

name_input = input("What is your name?  ")
print(username(name_input))
```
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