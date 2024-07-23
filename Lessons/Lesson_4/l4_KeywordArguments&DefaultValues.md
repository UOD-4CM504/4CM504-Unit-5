# Keyword Arguments and Default Values

## 1. Parameters and Arguments 
To date, our functions have just had parameters such as:

```python
def print_name_age(name, age):
    print(f"Hello {name}, your age is {age}")
```

This function takes two parameters; ``name`` and ``age``. When we call the function we can provide arguments (values) to the function that are bound to the parameters.

So ``print_name_age("Jimi", 27)`` will bind ``name = Jimi`` and ``age = 27``. These are then used in the ``print`` statement. 

Formally these are known as **positional** parameters because you call the function and pass the arguments in the correct position.

## 2. Keyword Arguments and Default Values

Python provides another way of defining the parameters of a function called **keyword arguments**. 

You can think of these as optional arguments, you will though need to give them a default value.

Let's look at an example from Guttag, J.V. (2021).

```python
def print_name(first_name, last_name, reverse = False):
    if reverse:
        print(f"{last_name}, {first_name}")
    else:
        print(f"{first_name}, {last_name}")
```

``print_name()`` is now a function whereby the third parameter is a **keyword argument** with a default value of ``False``.

This means we can leave out the **keyword argument**. We can just call using the two positional parameters ``first_name`` and ``last_name``. Inside the function ``reverse`` will take on the default value of ``False``.

```python
print_name("Jimi", "Hendrix")  # prints out Jimi, Hendrix
```

We can also choose to call the function and overwrite the value of the **keyword argument**, for example we can tell the function to set ``reverse`` to ``False``.
```python
print_name("Jimi", "Hendrix", reverse = True)  # prints out Hendrix, Jimi
```
which prints out ``Hendrix, Jimi`` because reverse is ``True``.

There is also nothing stopping you setting ``reverse`` to ``False``, this is perfectly legal, but not necessary.
```python
print_name("Jimi", "Hendrix", reverse = False)  # prints out Jimi, Hendrix
```


### 2.1 Order matters.

You can't put **keyword arguments** before positional parameters. 

The following is illegal in Python:

```python
def print_name(reverse = False, first_name, last_name):
    if reverse:
        print(f"{last_name}, {first_name}")
    else:
        print(f"{first_name}, {last_name}")
```

### 2.2 Another Simple Example

Let's say you want a ``price()`` function that calculates discounted price. 

This has an obvious default, that is, no discount.

Here is a function that reflects this. Note that discount is a percentage between ``0`` and ``100``.

```python
def calculate_price(price, discount=0):
    """ returns new price with discount applied"""
    return price * (1 - discount/100)

if __name__ == "__main__":
    print(calculate_price(30)) # will just return 30. No discount 
    print(calculate_price(30, discount=50)) # will just return 15. 50% discount on the price
```
We could extend this to add an optional tax argument.

```python
def calculate_price(price, discount=0, tax=20):
    """ returns new price with discount applied and tax"""
    total_before_tax = price * (1 - discount/100)
    total_after_tax = total_before_tax * (1 + tax/100)
    return total_after_tax

if __name__ == "__main__":
    print(calculate_price(30)) # will just return 36. No discount, tax=20
    print(calculate_price(30, discount=50)) # will return 18. 50% discount on the price, tax=20
    print(calculate_price(30, discount=50, tax=25)) # will return 18.75. 50% discount on the price, tax=25
```

## 3. A Few More Keyword Arguments

Just to complete the picture. Here is a function with two **keyword arguments**. You can have any number of **keyword arguments**.

```python 
def print_person(first_name, last_name, reverse=True, age=None):
    if reverse:
        print(f"{last_name}, {first_name}")
    else:
        print(f"{first_name}, {last_name}")
    
    if age:
        print(f"Aged {age}.")
```

We can call this function a number of different ways.

```python
print("Jimi", "Hendrix") # Prints Jimi, Hendrix
```

```python
print("Jimi", "Hendrix", age = 27) 
# Prints 
# Jimi, Hendrix
# Aged 27.
```

```python
print("Jimi", "Hendrix", age = 27, reverse = True) 
# Prints 
# Hendrix, Jimi
# Aged 27.
```

Some of you may have spotted in the last example that ``age`` and ``reverse`` are given in a different order to the function definition.

This is deliberate, once you have given the positional arguments, you can give the **keyword arguments** in any order.

## 4. Mutable Keyword Arguments (DO NOT USE)

Consider the following code:

```python
def test_keyword_mutability(list_one=[]):
    list_one.append("sam")
    return list_one

if __name__ == "__main__":
    test_keyword_mutability()
    test_keyword_mutability()
```

We would expect this to print out:

```
['sam']
['sam']
```

Instead it will print out:

```
['sam']
['sam', 'sam']
```
This wasn't the intention, this is because the keyword argument ``list_one=[]`` is mutable and Python stores it the when the function is defined, not when it is called. 

We can correct this by doing the following:

```python
def test_keyword_mutability(list_one=None):
    if list_one is None:
        list_one = []
    list_one.append("sam")
    return list_one

if __name__ == "__main__":
  test_keyword_mutability()
  test_keyword_mutability()
```

```
['sam']
['sam']
```
Much better!

For more information you can see this link:

[Python Mutable Defaults Are The Source of All Evil](https://florimond.dev/en/posts/2018/08/python-mutable-defaults-are-the-source-of-all-evil/)

[Common Gotchas](https://docs.python-guide.org/writing/gotchas/)

***
# === TASK ===

Write a function called ``print_list`` that prints the multiple of each item in the list

For example ``print_list([4,1,6,7], multiple = 2)``

```
8
2
12
14
```

For example ``print_list([4,1,6,7], multiple = 3)``

```
12
3
18
21
```

By default your function when called without the **keyword argument**  ``multiple``, i.e. ``print_list([4,1,6,7])`` should output:

```
4
1
6
7
```
Copy the following into `main.py` to get started.

```python
def print_list():
    pass

if __name__ == "__main__":
    print_list([4,1,6,7], multiple = 2)
    print_list([4,1,6,7], multiple = 3)
    print_list([4,1,6,7])
```

**Note: Due to the way that the tests are written for this task, an incorrect solution may result in the tests looking as though they are "hanging". Refresh the page to reattempt the test after considering why your solution may be incorrect.**

# References

Guttag, J.V. (2021). Introduction to Computation and Programming Using Python, Third Edition (3rd ed.). MIT Press.