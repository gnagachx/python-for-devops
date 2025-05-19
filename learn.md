--> variables can be reassigned to values of different types of classes.
ex:
```python
big = 'large'
print(big)
big = 1000 * 1000
print(big)
big = {}
print(big)
```
--> if you notice, here same variable is set to string, number, dictionary, variable can be re-assigned to values of any type

--> for loops can be used to iterate through any of the Python sequence types.

--> while loops repeat a block as long as a condition evaluates to True

--> In oop, data or state and functionality appear together. The essential concept is to understand when working with objects are class instantiation (creating objects from classes) and dot syntax (the syntax for accessing the an object's attributes and methods)

--> A class defines attributes and methods shared by its objects. 

--> objects store data in attributes. These attributes are variable attached to the object or object class. 
--> objects define functionality in object methods (methods defined for all objects in a class) and class methods(methods attached to a class and shared by all objects in the class) which are functions attached to the object

--> These functions have access to the object's attributes and can modify and use object's data.  To call an object's method or access one of its attributes, we use dot syntax

--> sequences are a family of built-in types, including list, tuple, range, string, and binary types. Sequences represent ordered and finite collection of items.

>> There are many operations that work across all of the types of sequences.

>> in and not-in operations to test weather or not an item exists in a sequence

```python 
>>> 2 in [4, 1, 5]
False
>>> 'a' not in 'cat'
False
>>> 10 in range(13)
True
>>> 10 not in range(2, 4)
True

```
--> we can reference the sequence of a number 