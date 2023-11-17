# Function Basics

As we mentioned in the overview a function consists of three parts:

1. The input(s) to the function
2. The function itself
3. The output from the function

You can think of a function as a machine (black box) that takes some input(s), does something, and then produces an output.

Once you define a function, you can reuse it. This is the principal reason for their existence. Don't Repeat Yourself! (DRY)

In essence it is a way of packaging up bits of code for reuse or to make your program more readable.

## 1. Defining a Function in Python
We define a function using the keyword ``def``, a function name, and the function parameters. We then write the code the function performs in the function body.
```python
def function_name(<formal parameters>):
    <function body>
```

The easiest way to demonstrate a function is by an example. 

Our first function will just add 5 to the input

```python
def add_five(x):
    return x + 5
```

Note that the ``return`` keyword is how you return (output) something from a function. Here the function ``add_five()`` returns the result of adding ``5`` to the input ``x``.

## 2. Calling a Function in Python

``add_five()`` is now a function that you can call with different values of ``x``. e.g. ``add_five(10)``

Try running the following code in **main.py**,

```python
def add_five(x):
    return x + 5

result = add_five(10)  # call function with 10 and bind result
print(result)      # this prints the value of result
```
and you will get 
```
15
``` 
as the output.

![Function Call Visualisation](assets/function_call_animation.gif)

You can visualise this yourself on [Python Tutor](https://pythontutor.com/).

Note that we could have called this function twice.
```python
def add_five(x):
    return x + 5

result_one = add_five(10)  # call function with 10 and bind result
result_two = add_five(7)   # call function with 7 and bind result
print(result_one)      # this prints the value in result_one
print(result_two)      # this prints the value in result_two
```
and you will get 
```
15
12
``` 
as the output.
### 2.1 Define a Function Before You Call It
Now try the following,

```python
result = add_five(10)
print(result)

def add_five(x):
    return x + 5
```
and you will get ``NameError``. This is because the function has not yet been defined, i.e. it is below the function call. Python does not know about that name.

### 2.2 Order of Precedence

We can also do more interesting things like:

```python
def add_five(x):
    return x + 5

result = add_five(10)*add_five(7) # same as 15*12
print(result) # prints 180
```

Here Python will evaluate ``add_five(10)`` and then evaluate ``add_five(7)``, then multiply them together. 

This is because other than parentheses ``()``, function calls have higher precedence than everything else in Python.

### 2.3 Multiple Return Statements

Consider the following function.

```python
def greater_than_five(x):
    if x > 5:
        return True
    else:
        return False

if __name__ = "__main__":
    print(greater_than_five(3)) # prints False
    print(greater_than_five(7)) # prints True
```
Here we use an ``if`` statement to test whether ``x`` is greater than ``5``, if it is the function returns ``True``, otherwise it returns ``False``.

This is a key point, although your function can only return one output, it can have more than one ``return`` statement in your function.

Note that we could have done this with one ``return`` statement by returning the result of the boolean expression.

```python
def greater_than_five(x):
    return x > 5

if __name__ = "__main__":
    print(greater_than_five(3)) # prints False
    print(greater_than_five(7)) # prints True
```

Again which one you use will be your preference and which one you are more comfortable with. Both ways are fine. If the second one isn't for you, then use the first one.

## 3. ``if __name__ = "__main__":``

You will have noticed in the last couple examples used the ``if __name__ = "__main__":`` block. This is not needed to call your functions, but as stated in the **5.1 - MP: Passing Unit Tests** you should write any code and calls to your functions inside this block. 

The reason is that the unit tests import your code and anything outside the ``if __name__ = "__main__":`` will get run due to the import. **This can mess up the unit tests!**

**We will cover this properly in unit 8!**

***
# === TASK ===

Create a function that tests whether a number is odd or even. 

Copy the following into **main.py**.

```python
def odd_test(x):
    # delete pass and replace with code to implement the function
    pass

if __name__ == "__main__":
    print(odd_test(3))     # should output True
    print(odd_test(8))     # should output False
```

Your function ``odd_test`` and take in one input.
It should return a ``True`` or ``False`` depending on the number.

For example:

``odd_test(3)`` should return ``True`` and ``odd_test(8)`` should return ``False``.

***
