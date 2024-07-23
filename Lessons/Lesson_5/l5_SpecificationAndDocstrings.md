# Specification and Docstrings

When defining functions it is important to inform the person using your function of three things

1. What does the function do?
2. What are the parameters of the function and what type should they be?
3. What does the function return?

Sometimes a function won't take parameters or return anything, so not all of these need documenting.

The standard way of doing these in Python is docstrings. A docstring uses triple quotes ```"""```.

## 1. Creating a Docstring
It is easiest to look at a simple example.

The following function is the simple add function we have seen before:

```python
def add(x, y):
    return x + y
```

The answers to the 3 questions above for this function are 

1. Adds up two numbers and return the result.
2. ``x`` (``int`` or ``float``), ``y`` (``int`` or ``float``). These are the numbers to add.
3. Returns the sum of ``x`` and ``y``.

The following code snippet shows how we add these with a docstring.

```python
def add(x, y):
    """
    Adds up two numbers and returns the result.
    
    Parameters
    ----------
    x: int or float
    First number to add.
    y: int or float
    Second number to add.
    
    Returns
    -------
    int or float
      Sum of x and y.
    """
    return x + y
```

Our basic template is:

```python
    """
    Function description
    
    Parameters
    ----------
    param_name: type
    Description of parameter
    param_name: type
    Description of parameter
    .
    .
    .
    
    Returns
    -------
    type
      Description of return value
    """
```

We will be using the **NumPy** standard in this course that works with the documentation generator library **Sphinx**. We are not looking at this in detail in this course but is important to know about it.

[NumPy Standard](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_numpy.html#example-numpy)

If we are missing either the parameters or return statement then we just leave these out of the docstring.

```python
def print_hello():
    """
    Prints Hello.
    """
    print("Hello")
```

```python
def print_sum(x, y):
    """
    Prints the sum of the two numbers.
    
    Parameters
    ----------
    x: int or float
    First number to add.
    y: int or float
    Second number to add.
    """
    print(x + y)
```

And even though you would rarely see a function like the following, for completeness.

```python
def five():
    """
    Returns 5
    
    Returns
    -------
    int
    Always returns 5
    """
    return 5
```

## 2. Python's help() Function

Python has many built-in functions. You can find an extensive list below.

[Python Built-in Functions](https://docs.python.org/3/library/functions.html)

One of these functions is ``help()`` which will display the docstring of a function.

Try the following in the console:

```python
help(abs)
```

This gives you the docstring for the built-in function ``abs()``.

## 3. When To Document

Generally, when you are hacking away at your own code, documentation probably will be furthest from your mind. I would still suggest putting in a short description. 

Every programmer has written some complicated code and then come back to it at a later date and not had a clue what it does. This then requires time, some hints will help you.

Clearly when working with others and on a shared codebase documenting is important. It is also important if people will be using your code and they would like some hints by using the ``help()`` function. If you don't write a docstring, there won't be any help!

***
# === TASK ===
Copy the following into **main.py**. You won't have to understand this code to pass the task, but you will need to read on.

```python
def add(x, y):
    """
    Adds up two numbers and returns the result.

    Parameters
    ----------
    x: int or float
    First number to add.
    y: int or float
    Second number to add.

    Returns
    -------
    int or float
     Sum of x and y.
    """
    return x + y


# Example from Guttang (2021)
def find_root(x, power, epsilon=0.01):
    """
    Find a y such that y**power = x (within epsilon x).

    e.g. For x = 27 and power = 3 then y = 3 as 3**3 = 27.
    i.e. the cubed root of 27 is 3.

    Parameters
    ----------
    x :int or float
    Number we want the root of.
    power: int
    Root number e.g. square root, power = 2.
    epsilon: int or float, default 0.01 
    Error tolerance for the answer.

    Returns
    -------
    float or None
    """
    # if x is negative and power even. No root exists
    if x < 0 and power % 2 == 0:
        return None
    low = min(-1.0, x)
    high = max(1.0, x)
    ans = (high + low) / 2.0
    # check if the answer is close enough
    while abs(ans**power - x) >= epsilon:
        if ans**power < x:
            low = ans
        else:
            high = ans    
        ans = (high + low) / 2.0
    return ans
   
if __name__ == "__main__":
    # add the line of code here
    pass
```

The built-in ``help()`` function allows us to print out the docstring of a function. 

Run the code in **main.py** and then type 

```python
help(add)
```

into the console.

You will see that you get the docstring for the function. 

You will also see a more complicated function called ``find_root``. 

For now, it doesn't matter how it works, but the docstring does tell us what it does and requires a longer description.

Add a line of code to the bottom of **main.py** that prints out the docstring for ``find_root`` by using the ``help()`` function. Make sure you don't use any indentation so that the code isn't inside a function.

Think carefully, ``help()`` is a function that prints out to the console and returns ``None``.
***