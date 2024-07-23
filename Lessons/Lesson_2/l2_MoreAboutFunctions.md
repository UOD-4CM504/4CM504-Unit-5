# More About Functions

***HINT: I would copy and past examples into main.py to make sure you understand them.***

***This is one of the most important lessons on functions. Please make sure you understand all 3 of the following.***

In this lesson we will cover the following:
* Different types of functions
* Parameters vs arguments
* Function composition

All of these are important concepts and will help you understand later material.
  
## 1. Types of Function

### 1.1 Function with Multiple Parameters
We are not limited to just one parameter, we can have as many as we like. The following two functions take two parameters.

The first returns the sum of the two inputs.
```python
def add(x, y):
    return x + y

if __name__ == "__main__":
    result = add(3, 13)
    print(result) # prints 16
```
The seconds returns the maximum of the two inputs.
```python
def maximum(x, y):
    if x > y:
        return x
    else:
        return y

if __name__ == "__main__":
    result = maximum(3, 5)
    print(result) # prints 5
```
You will note that this function has two uses of ``return`` for the two possible cases.

### 1.2. Function with No Return Value
Here we define a function with a single parameter ``name`` (the input of the function). 
```python
def print_hello(name):
    print(f"Hello {name}")
```

This is interesting as it takes an input ``name`` and does something with the input. However, it **does not** have a ``return`` statement.

Be careful though, this function does return something, it returns the ``None`` keyword which represents no value.

Copy this bit of code into **main.py** and you will see this for yourself

```python
def print_hello(name):
    print(f"Hello {name}")

if __name__ == "__main__":
    # call the function and bind the return value to a
    a = print_hello("Jimi")
    print(a)
```

You will notice that it outputs,

```
Hello Jimi
None
```
because ``a`` stores the return value of ``print_hello()`` which is ``None``.


### 1.3. Function with No Input and No Return Value

The final function has no input and no ``return`` statement. Its sole purpose is to print two lines.

```python
def print_hello_world():
    print("Hello World")
    print("Welcome to another day on planet earth!")

if __name__ == "__main__":
    print_hello_world()
    print_hello_world()
```

The code above will output,

```
Hello World
Welcome to another day on planet earth!
Hello World
Welcome to another day on planet earth!
```

as the function is called twice.

### 1.4. Some Familiar Functions

You have already met a bunch of Python functions.

| Function | Input | Returns| Purpose| Example  |
|--|--|--|--|--|
|``print()``|``str`` to output to the console. |``None``| Prints the input to the console. | ``print("Hello World")`` |
| ``input()`` |``str`` to output to the console. | ``str`` entered by the user. | Prints the input to the console and returns what the user inputted as a string | ``input("Please enter your name:\n")`` |
| ``int()`` | ``str`` representation of a whole number, e.g.``"5"`` | ``int`` conversion of input. e.g. ``5`` | Converts a ``str`` to an ``int`` if possible. If not throws ``ValueError`` | ``int("5")`` | 

### 1.5 The NotImplementedError

Sometimes it is convenient to define a function, but not write the code yet. This is especially useful when planning a program. It is also useful to make sure that if this function is called it doesn't result in a silent bug.

To stop this, we can define a function that raises a ``NotImplementedError``. This as the name suggests means that you have not implemented the function.

Here we set up a program for computing the total and length of a list. The ``length()`` function has not been implemented and raises a ``NotImplementedError``.

```python
def total(num_list):
    """ compute the total of the numbers in the list"""
    tot = 0
    for x in num_list:
        tot += x
    return tot

def length(num_list):
    """ count the number of numbers in the list"""
    raise NotImplementedError("The length function has not been implemented yet!")

if __name__ == "__main__":
    num_list = [4,3,5,7,4]
    print(f"The total of the list is {total(num_list)}") # This line will run
    print(f"The number of numbers in the list is {length(num_list)}") # This line will fail
```

If you try this in **main.py** you will get the output.

```
The total of the list is 23
Traceback (most recent call last):
  File "main.py", line 14, in <module>
    print(f"The number of numbers in the list is {length(num_list)}") # This line will fail
  File "main.py", line 10, in length
    raise NotImplementedError("The length function has not been implemented yet!")
NotImplementedError: The length function has not been implemented yet!
```

This is because when we call the ``length()`` function it raises the ``NotImplementedError`` with the message ``The length function has not been implemented yet!``.

Note thought that Python actually ran the code before it and printed out the list total.

### 1.6 The Pass Statement

Another way to do this is by using the ``pass`` statement. When a programmer doesn't know what to write or is creating a skeleton program they will sometimes put ``pass``. ``pass`` will mean the code is valid and can therefore be run.

```python
def total(num_list):
    """ compute the total of the numbers in the list"""
    tot = 0
    for x in num_list:
        tot += x
    return tot

def length(num_list):
    """ count the number of numbers in the list"""
    pass

if __name__ == "__main__":
    num_list = [4,3,5,7,4]
    print(f"The total of the list is {total(num_list)}") # This line will run
    print(f"The number of numbers in the list is {length(num_list)}") # This line will run but prints - The number of numbers in the list is None
```
The ``length()`` function has a pass statement and will now return ``None``. 

Try this in **main.py**

## 2. Parameters vs Arguments

It is important to understand the difference between the parameters of a function and arguments. These words are often confused or used interchangeably.

#### Parameters
Parameters are the names that are in the function definition in between the parentheses ``()``. 
#### Arguments
Arguments are the names that are used in the function call. 

The following image shows both the function definition and the function call.

![Parameters vs Arguments](../../../Downloads/Unit%20Material/Unit%20Material/Unit%205/assets/function_def_params_args.png)

## 3. Function Composition

Function composition is the act of applying a function to the result of another function.

The name is taken from the mathematical concept of function composition.

Consider the following code.

```python
def add5(x):
    return x + 5

def mul2(x):
    return 2*x

if __name__ == "__main__":
    x = 10      # binds 10 to x
    x = add5(x) # binds 15 to x, i.e. 10 + 5 = 15
    x = mul2(x) # binds 30 to x, i.e. 2*15 = 30
    print(x)    # prints 30
```

We can write this using function composition, note that we evaluate the innermost function first. So work inner to outer. 

The example below first evaluates ``add5()`` and then evaluates ``mul2()`` with the result of ``add5()``.

```python
x = 10 # binds 10 to x
x = mul2(add5(x)) # first computes add5(10) = 15, then computes 2*15 = 30 and binds to x
print(x) # prints 30
```
We can go further and compose three functions. Now we pass the result of the first two to the ``print()`` function.
```python
x = 10
print(mul2(add5(x))) # first computes add5(10) = 15, then computes 2*15 = 30 and then prints 30
```

You could even just do the following.

```python
print(mul2(add5(10))) # does the whole lot in one line!
```

OK great, we did it in one line! 
  
**However**, take a look at the readability of the code. The examples which use function composition here are not exactly very readable, in fact, it obfuscates things. 

The first example is clear. Assign ``10`` to ``x``, then add ``5`` to ``x``, then multiply ``x`` by ``2`` and finally print ``x``.

There are many examples of complex programs that we can write in python with one-liners. This is fine if it is just for your eyes only. 

I would suggest for readability you avoid it unless it is necessary or makes sense and is readable.
### 3.1 Function Composition Isn't Commutative

It is also important to know that function composition isn't commutative, that is just a fancy way of saying that if you change the order of evaluation it doesn't have the same result.

For example,

```python
3 * 5 == 5 * 3 # True, because multiplication doesn't care about the order (commutative)
3 / 5 == 5 / 3 # False, division cares about the order (not commutative)
```

The following example shows the ``add5()`` and ``mul2()`` functions composed in the two possible ways give two different results.

```python
def add5(x):
    return x + 5

def mul2(x):
    return 2*x

if __name__ == "__main__":
    x = 10
    y = mul2(add5(x))
    z = add5(mul2(x))
    print(y)  # prints 30
    print(z)  # prints 25
```

You can try this in **main.py** and see that ``y`` and ``z`` are different values because the order of composition was changed.

***
# === TASK ===

Copy the following into **main.py**. You will need to remove the ``raise NotImplementedError`` and replace it with your own code. Make sure you read the whole of task.

```python
def reverse(str_to_reverse):
    raise NotImplementedError("You have not implemented the reverse function")

def get_character(string_one, i):
    raise NotImplementedError("You have not implemented the get_character function")

if __name__ == "__main__":
    print(reverse("This is a string")) # prints "gnirts a si sihT"
    print(reverse("Hello World")) # prints "dlroW olleH"
    print(get_character("This is a string", 3)) # prints "i"
    print(get_character("Hello World", 5)) # prints "o"
    
```

The first function is called ``reverse()`` and has a single parameter, a string. The function should output the reverse of the string.

You should do this using a loop. There is a simple way to do this in Python, but it is good practice to write your own ``reverse()`` method.


The second function is called ``get_character()`` and has a string and a number as parameters. It should return the ith character of the string.

The table below gives the return values of the functions for different calls.

| Function call | Expected return value |
| -- | -- |
| ``reverse("This is a string")`` | ``"gnirts a si sihT"`` |
| ``reverse("Hello World")`` | ``"dlroW olleH"`` |
| ``get_character("This is a string", 3)`` | ``"i"`` |
| ``get_character("Hello World", 5)`` | ``"o"`` |

**I suggest you test the above work correctly in the console, you should not rely on the tests as the feedback may not be useful.**
*** 