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

## Libraries and collections
- when you wanted to treat some data as a group, it would not be good to create individual variables for each data. you can store them together as a collection.

There are many collection data types which are supported by python:
    String
    Tuple
    List
    set
    Dictionary

**strings**
- Strings are immutable like tuples
- In python, string is a data type and anything enclosed in a single quote or double quote is considered to be a string. all the remaining operations are simmilar to lists
- Each value in a string is called a character. jst like elements, we can access the characters in a string based on index position

string --> "AABT6715H"
character --> A A B T 6 7 1 5 H
index --> 0 1 2 3 4 5 6 7 8 9

**string functions: **
1. name.count("a") --> To return the count of a given set of characters. Returns 0 if not found
2. name.replace("a","A") --> Returns new string by replacing a set of characters with another set of characters. it doesnot modify the original string
3. name.find("a") --> Returns the first index position of a given set of characters
4. name.startwith("Ra") --> checks if a string starts with a specific set of characters, returns true or false accordingly
5. name.endswith("ha") --> checks if a string ends with a specific set of characters, returns true or false accordingly
6. name.isdigit() --> checks if all the characters in the string are numbers, returns true or false accordingly
7. name.upper(), name.lower() --> converts lower to upper and upper to lower
8. name.split(",") -->splits according to delimeter and returns the list of substring, space is considered as the default delimeter

f-strings and r-strings :
-----------------------
name = "Stark"
print(f"He said his name is {name}.")

print(r"C\\Users\\Stark\\Documents\\Books\\Python")

output: C\\Users\\Stark\\Documents\\Books\\Python

**Tuples: **
--> Tuples can also store sequence of elements but the values of individual elements cannot be changed. (tuples are immutable). Elements can be homogeneous or heterogeneous but, they are Read-only.

creating tuple: lunch_menu=("welcome drink", "veg starter", "non-veg starter", "main course", "dessert") --> () this is optional, a set of values separated by comma is also considered as tuple ex: "A","c", "d"

Random write : e.g; lunch_menu[0]=" " This will result in an error. Since, tuples are immutable

**list: **
--> list can be used to store a group of elements together in a sequence. If you want to store something of multiple things, instead of creating a separate variables, we can use list as shown below :

ticket_list = (84, 52, 53, 21, 15)
--> In case of having different variables, it will store values in separate memory location. But, when it comes to list all the values can be stored in a contiguous memory locations.
--> list indexing : Each element in the list has a position in the list known as an index. The list index starts from zero. It is like having a seat number starting from zero.
    --> Index positions actually help us to directly access/directly modify a value from the list
list_name[index] --> can be used to directly access the list element at the mentioned index position.

we cannot access values beyond the total number of elements in the list. if we try so then we will get index out of bound error.

List -- Operaitons :
-------------------
creating an empty list 
```python
sample_list=[] or list()
```
creating a list with known size and known elements 
```python
sample_list1=["mark",5,"jack",9,"chan",50]
sample_list2=["charan","welcome","cherry","jack"]
## List can store both homogeneous and heterogeneous elements
```
creating a list with known size and unknown elements `sample_list=[None]*5`
to find the length of the list, we can use len(sample_list1)

Random Read --> print(sample_list[3])
random write --> sample_list[2]="james"
Adding an element to the end of the list, sample_list.append("James")
concatinating two lists --> new_list=["charan","thin"]
sample_list+=new_list
sample_list=sample_list+new_list

list - Slicing :
----------------
list | al1 | al2 | al3 | al4
index | 0 | 1 | 2 | 3 | 4
negative index | -5 | -4 | -3 | -2 | -1

list functions :
~~~~~~~~~~~~~~~~~
num_list.append(60) --> adds an element to the end of the list
num_list.index(10) --> returns index position of the element. in case of multiple occurances of the element, returns the index of the first occurence. Throws valueerror, if the element is not found.
num_list.insert(3,60) --> inserts an element at a given position
num_list.pop(3) --> Removes and returns the element at given index position from the list
num_list.remove(30) --> Removes the first occurence element whose value is 30
num_list.sort() --> sorts the list in ascending order
num_list.reverse() --> reverse the list

collections - sets:
------------------
In python sets are used to store unique elements. They are simmilar to arraya in appearance. However, they do not allow duplicate elements. sets also support mathematical operations like union, intersection, difference etc

--> to create set with items 

```python
Items = {"carrot", "chilly", "pepper"}
print(Items)
```
To create empty set --> visited = set()
                        print(visited)

set functions:
-----------------
add() --> Adds an element to the set
discard() --> Removes an element from the set if it is present
pop() --> Removes and returns a random set element. Raises KeyError if the set is empty
clear() --> Removes all elements from the set
union() --> Returns the union of two sets as a new set
intersection() --> Returns the common elements of two sets as a new set
difference() --> Returns the elements that are in the first set but not in the second set
symmetric_difference() --> This function returns the elements that are present in either of the sets but not in the both the sets.

```python
Items = {"Carrot", "Chilly", "Pepper", "Orange"}
Items.add("orange")
print(Items)

Items = {"Carrot", "Chilly", "Pepper"}
Items.discard("Chilly")
print(Items)

Items = {"Carrot", "Chilly", "Pepper"}
Items.pop()

Items = {"Carrot", "Chilly", "Pepper"}
Items.clear()
print(Items)

Items1 = {"Carrot", "Chilly", "Pepper"}
Items2 = {"Carrot", "Chilly", "Pepper", "orange"}
Items3 = Items1.union(Items2)
print(Items3)

Items1 = {"Carrot", "Chilly", "Pepper"}
Items2 = {"Carrot", "Chilly", "Pepper", "orange"}
Items3 = Items1.intersection(Items2)
print(Items3)

Items1 = {"Carrot", "Chilly", "Pepper"}
Items2 = {"Carrot", "Chilly", "Pepper", "orange"}
Items3 = Items1.difference(Items2)
print(Items3)

Items1 = {"Carrot", "Chilly", "Pepper"}
Items2 = {"Carrot", "Chilly", "Pepper", "orange"}
Items3 = Items1.symmetric_difference(Items2)
print(Items3)

```

Collections - Dictionary
-------------------------
--> A dictionary can be used to store an unordered collection of key-value pairs
--> dictionaries and lists are mutable. The key should be unique and can be of any data type. 

creating a dictionary --> crew_details = {"pilot":"kumar", "copilot": "Raghav"}  First element in every pair is the key and the second element is the value

Accessing the value using key: crew_details["pilot"] --> this will return the corresponding value for the specified key

Iterating through dictionary --> 
```python
for key, value in crew_details.items(): 
     print(key,":",value) --> items() function gives both key and value, which can be used in for loop

```
Dictionary - Built-in functions :
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
```python
crew_details={
              "Pilot":"Kumar",
              "Co-pilot":"Raghav",
              "Head-Strewardess":"Malini",
              "Stewardess":"Mala"
              }
```

crew_details.get("pilot") --> returns the value for given key. if the given key not found returns none
crew_details.update({"flight attendant":"jane", "copilot":"henry"}) --> updates the dictionary with the given key-value pairs. if a key-value pair is already existing, it will be overwritten, otherwise it will be added to the dictionary


Libraries and built-in functions in python :
---------------------------------------------
code organization :
```````````````````
In python, code organization and reusability is managed through modules and packages. 

A module is a python file with .py extension.
A package is a folder which contains a file whose name is __init__.py 
package can store many python modules/files in it. 
The import statement is used to load a library module into the program's memory


Import can be done in two ways:
1. from packagename import modulename
```python
from Flights import ManageFlights
ManageFlights.add(10)

```
2. import packagename.modulename
```python
import Flights.ManageFlights
Flights.ManageFlights.add(10)
```

package naming conflict :
-------------------------
Consider a scenario where two modules have the same name which are present in different packages and both of them have the same function ‘add’.

Flights -> Manage.py -> add()

Employees -> Manage.py -> add()

To avoid naming conflicts during import, you can use one of the below techniques:

```python
1. 
import Flights.Manage
import Employees.Manage
Flights.Manage.add()
Employees.Manage.add()

2. 
from Flights import Manage as FManage
from Employees import Manage as EManage
FManage.add()
EManage.add()

3. 
from Flights.Manage import add as add1
from Employees.Manage import add as add2
add1()
add2()

```

Random module :
-------------
--> python has many inbuilt packages and modules. one of the most useful module is `random`. This module helps in generating random numbers

```python
import random
x=10
y=50
print(random.randrange(x,y))
```
math module :
-----------
--> math is another useful module in python, once you have imported math module, you can use below functions

math.ceil(x) --> smallest integer greaterthan or equal to x
math.floor(x) --> largest integer smaller than or equal to x
math.factorial(x) --> factorial of x
math.fabs(x) --> gives absolute value of x

Regular Expressions :
~~~~~~~~~~~~~~~~~~~~~~~~~~~
--> Regular expressions are used to check and extract relevant portions of a string based on a pattern and modify if required. Python has a module named 're' for regular expressions



## filemangement in python
--> Python has a function called open() to open a file programatically. open() function returns a file object using which other file operations like reading, writing, and closing of the file are done.

syntax: file_object = open(file_name_path, [access_mode])
where : 
    - file_name_path is the filename or path of file to be opened
    - access_mode  is the mode in which the file has to be opened,which is optional if not specified, default value will be read
    - file_object is the object returned by open method which is used for further file operations

Access Modes : 
   r -
   w -
   a - 

--> closing file 
file_object.close()

--> read the single line form the file at a time
var_name = file_object.readline()

--> read entire content of file into a variable, where each line will present as an element of the list.

var=file_object.readlines()

--> read(size) function to read the specified size(number) of characters from the file as a string into a variable. if no size is specified, then entire content of the file is read as a string into a variable

var_name=file_object.read(size)

--> we can also iterate through file object to read the content of the file line by line in a simple way. This is the fast and efficienct compared to other methods of the file contents.

```python
fhr = open("data.txt", "r")
for line in fhr:
    print(line, end="")
fhr.close()
```

--> python provides write(data) function to write the given data which is a string into the file and it returns the number of characters written into a file.

var=file_object.write(data)

```python
fhr=open("data.txt", "r")
data=fhr.read()
print("Before  writing:")
print(data)
fhr.close()

fhw=open("data.txt", "w")
num=fhw.write("This new first line written\n")
num1=fhw.write("This new second line written\n")
print("num:", num)
print("num1:", num1)
fhw.close()

fhr=open("data.txt","r")
data =fhr.read()
print("After writing:")
print(data)
fhr.close()
```

--> previous content of the file is preserved. if we use append

```python
fhr=open("data.txt", "r")
data=fhr.read()
print("Before  writing:")
print(data)
fhr.close()

fhw=open("data.txt", "a")
num=fhw.write("This new first line written\n")
num1=fhw.write("This new second line written\n")
print("num:", num)
print("num1:", num1)
fhw.close()

fhr=open("data.txt","r")
data =fhr.read()
print("After writing:")
print(data)
fhr.close()
```

--> python provides tell() method to get current position which is pointed by file object within the file

file_object.tell()

```python
fhr=open("data.txt", "r")
cur_pos=fhr.tell()
print(cur_pos)
data=fhr.readline()
print(data)

cur_pos=fhr.tell()
print(cur_pos)
data=fhr.readline()
print(data)
fhr.close()
```

--> python provides seek() function to navigate the file object pointer to the required position specified.

file_object.seek(offset, [whence]) where
file_object indicates the file object pointer to be navigated
offset indicates which position the file object pointer is to be navigated
if offset is, 
    positive navigation is done in forward direction
    negative navigation is done in backward direction

whence represents reference point for navigating the file object pointer, whence is optional, if not specifie default value is 0

if whence value is, 
0, navigation will take the reference from begining of file (absolute positioning)
1, navigation will take the reference of current position (relative positioning) of the file object pointer
2, navigation will take the reference of end of file (relative positioning)

```python
fhr=open("data.txt","rb+")
print(fhr.tell())
fhr.seek(12) #navigates to 12th position from beginning of the file
print(fhr.tell())
fhr.seek(3,1) #navigates to 3rd position from current position of the file object position
print(fhr.tell())
fhr.seek(-3,2)#navigates to 3rd position from end of the file in backward direction
print(fhr.tell())
fhr.close()

```

--> file object attributes

file_object.closed : closed attribute returns true if the file is closed else it will return false
file_object.mode : mode attribute returns mode in which the file has been opened
file_object.name : name attribute returns the name of the file opened

ex:
```python
fhr=open("data.txt", "rb+")
print("filename: ", fhr.name)
print("accessmode:", fhr.mode)
print("closed?", fhr.closed)
fhr.close()
print("after closing the file closed ?", fhr.closed)
```