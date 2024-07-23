# Passing by Assignment

**WARNING: This is really fundamental and can cause major bugs and errors if you don't understand it.**

**I strongly suggest that you paste the examples in [Python Tutor](https://pythontutor.com/) and work through them.**

If you are struggling to follow this then please speak to the instructors in the practicals.

Python differs from other programming languages in that everything is an object.

Some of these objects are immutable (cannot be changed) and some are mutable (can be changed).

Immutable and mutable types are common in most languages and how these are dealt with differs. 

**We are specifically talking about what Python does.**

## 1. Immutable vs Mutable Types

### 1.2 Immutable Type
An immutable type is something that once created cannot be changed. Immutable types you have seen in Python are ``str``, ``float``, ``int`` and ``bool``.

Consider the following example which uses ``int``. Here we also use the ``is`` keyword to see if ``x`` and ``y`` are the same object in memory.

```python
x = 1
y = x
print(x is y) # prints True. They are the same object in memory

y += 1
print(x) # prints 1
print(y) # prints 2
print(x is y) # prints False. They are now different objects in memory
```
The first ``print(x is y)`` prints ``True`` because ``x`` and ``y`` are both attached to the same immutable object ``1``.

The reason the second ``print(x is y)`` prints ``False`` is because to start with ``x`` and ``y`` are attached to the immutable object ``1``; however, when we add ``1`` to ``y`` Python creates a new object and reassigns ``y`` to ``2``.

Now ``x`` points to the object ``1`` in memory and ``y`` points to the object ``2`` in memory. Different objects!

### 1.2 Mutable Type

Lists are mutable. If we do something similar to the above we get a very different result.

Consider the following example which uses ``list``. Here we also use the ``is`` keyword to see if ``list_one`` and ``list_two`` are the same object in memory.
```python
list_one = [1,2,3]
list_two = list_one
list_two.append(4)

print(list_one) # prints [1,2,3,4]
print(list_two) # prints [1,2,3,4]
print(list_one is list_two) # prints True. They are the same object in memory
```
When we assign ``list_two = list_one`` both names are pointing to the same object ``[1,2,3]`` in memory.

When we call the append method, we add ``4`` to the end of the list ``[1,2,3]``. Both ``list_one`` and ``list_two`` still point to the same list which is now ``[1,2,3,4]``. Hence ``print(list_one is list_two)`` prints ``True``.

We can stop this from happening by using a copy.

Here we assign ``list_two`` to a copy of the object ``[1,2,3]`` in memory. This now means that ``list_one`` points to one object ``[1,2,3]`` and ``list_two`` points to a separate object ``[1,2,3]``.
```python
list_one = [1,2,3]
list_two = list_one.copy() # now we create a copy 
list_two.append(4) 

print(list_one) # prints [1,2,3]
print(list_two) # prints [1,2,3,4]
print(list_one is list_two) # prints False. They are now different objects in memory
```
The ``append()`` method is now only called on the object attached to ``list_two`` and therefore the object attached to ``list_one`` is not updated. Hence ``print(list_one is list_two)`` prints ``False``.

## 2. Passing by Assignment

When we pass arguments to functions, what we are actually doing is binding objects to the parameters of the function.

### 2.1 Passing an Immutable Type

n Python, a variable is just a name (label) that can be attached to an object. When we pass an object to a function, the function parameter is attached to the passed object

In the example below ``x`` will be attached to whatever is passed into the function ``add_one()``. If you pass in an immutable object, as soon as you try to update the object it will create a new object to reflect the changes.

Remember immutable objects can't be changed. 

The following example illustrates this. We pass in a number that is attached to ``num`` and then add ``1``. Because we are trying to change an immutable object, we have to create a new object. However, we don't return anything and reassign, so the original variable ``num_one`` is not changed.
```python
def add_one(num):
  num += 1 # add one to the local variable x

if __name__ == "__name__":
    num_one = 1
    print(num_one) # prints 1 
    add_one(num_one)
    print(num_one) # prints 1
```

We can reflect the changes by returning the result and reassigning it to ``num_one``.
```python
def add_one(num):
  num += 1
  return num # return the new object created by adding 1

if __name__ == "__name__":
    num_one = 1
    print(num_one) # prints 1
    num_one = add_one(num_one) # reassign x1 to the result of add_one()
    print(num_one) # prints 2
```

### 2.2 Passing a Mutable Type

When you pass a mutable object to a function and change it you are updating the original object. That is doing something to the object passed to the function doesn't create a new copy, it operates on the same object!

Here is a simple example that adds ``4`` to the end of a list.

```python
def func_one(items):
  """ append 4 to the list. """
  # append adds to the end of the list
  items.append(4)

if __name__ == "__main__":
    list_one = [1, 2, 3]
    func_one(list_one) # call func_one with list_one
    print(list_one) # prints [1,2,3,4] - this has been updated by the function call
```

The object attached to variable ``list_one`` is first passed to ``func_one()`` and the variable ``items`` is attached to the object. 

The function then adds ``4`` to the end of the list using the ``append()`` method. What happens here is both ``list_one`` and ``items`` point to the mutable list. When it is updated, both are updated as they point to the same object.

Below are some more examples that illustrate passing a list to a function.

```python
def func_one(items):
    """ append 4 to the list. """
    # append adds to the end of the list
    items.append(4)

def func_two(items):
    """ add the list and [4] """
    # this creates a new object by adding the lists items and [4]
    items = items + [4]

def func_three(items):
    """ add the list and [4] """
    # again this creates a new object by adding the lists items and [4]
    items = items + [4]
    # however this time we return the new object
    return items

if __name__ == "__main__":
    list_one = [1, 2, 3]
    func_one(list_one) # call func_one with list_one
    print(list_one) # prints [1,2,3,4] - this has been updated by the function call
    
    list_one = [1, 2, 3]
    func_two(list_one) # call func_two
    print(list_one) # prints [1,2,3] - this has not been updated by the function call
    
    list_one = [1, 2, 3]
    list_two = func_three(list_one) # call func_three and bind to the variable list_two
    print(list_two) # prints [1,2,3,4] - the new object created by the function call
```

``func_one()`` operates on the original list, this means you don't need to return anything. You could choose to return the list here, but there is no point. 

``func_two()`` adds the original list and the list ``[4]``. This creates a new list but we do not return it and therefore we lose the new list.

``func_three()`` adds the original list and the list ``[4]``. This creates a new list and we return it. This means we can use it outside of our function.

I would experiment with these in **main.py** to make sure you understand what is going on.

### 3.3 To Return or Not To Return

Generally, if you are operating on a mutable object and you don't need to keep a copy of the original then there is no need to return anything.

If you need the original list intact then you need to copy the original list before you operate on it and return the modified copy. See the next section.

### 3.4 Copy and Deep Copy

We will talk about these more in unit 6, but we can stop Python from updating the original list by using a copy of the list.

For now, we will only need the ``copy()`` function as we will demonstrate on a list of numbers. Things get more complicated if we operate on a list that contains other mutable data types like a list of lists.

```python
import copy

def func_four(items):
  """ append 4 to a copy of the list. """
  # create a copy of the list
  new_list = copy.copy(items)
  # append to the copy
  new_list.append(4)
  # return the copy
  return new_list
if __name__ == "__main__":
    list_one = [1,2,3]
    list_two = func_four(list_one)
    print(list_one)  # prints [1,2,3]
    print(list_two)  # prints [1,2,3,4]
```

Note, we could have overwritten the original list by reassigning the return value. e.g.

```python
list_one = [1,2,3]
print(list_one) # prints [1,2,3]
list_one = func_four(list_one)
print(list_one)  # prints [1,2,3,4]
```

***
# === TASK ===

Create two functions. The first function ``update_list_item_one()`` should take a list and a number and update the first item in the list with the number. It should operate on the original list. It does not require a return statement.

For example,

```python
list_one = [1,2,3,4]
update_list_item_one(list_one, 0)
print(list_one) # prints out [0,2,3,4]
``` 

The second function ``new_list_item_one()`` should create a copy of the list that is passed into the function (this will be a new object), update the first item in the new list and then return the new list.

For example,

```python
list_one = [1,2,3,4]
new_list_item_one(list_one, 0)
print(list_one) # prints out [1,2,3,4]
```
does not update the original list, however,

```python
list_one = [1,2,3,4]
list_one = new_list_item_one(list_one, 0) # bind the new object to list_one
print(list_one) # prints out [0,2,3,4]
``` 
reflects the changes made because the new object returned by ``new_list_item_one()`` was reassigned to ``list_one``.

To get you started copy the following into **main.py**
```python
import copy

def update_list_item_one(items, x):
  pass

def new_list_item_one(items, x):
  pass

if __name__ == "__main__":
    list_one = [1,2,3,4]
    update_list_item_one(list_one, 0)
    print(list_one) # should print out [0,2,3,4]
    
    list_one = [1,2,3,4]
    new_list_item_one(list_one, 0)
    print(list_one) # should print out [1,2,3,4]
    
    list_one = [1,2,3,4]
    list_one = new_list_item_one(list_one, 0) # bind the new object to l
    print(list_one) # should print out [0,2,3,4]
```
***

# References


[Python Docs - Passing by Assignment](https://docs.python.org/3/faq/programming.html#how-do-i-write-a-function-with-output-parameters-call-by-reference)

[Python Memory Model](https://www.cs.toronto.edu/~david/course-notes/csc110-111/05-memory-model/03-python-memory-model-1.html#:~:text=However%2C%20now%20that%20we%20know%20about%20reassignment%20and,stored%20in%20a%20Python%20program%20in%20an%20object.)

  