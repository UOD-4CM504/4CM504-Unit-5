# Scope

***This can be a tough one to get your head around, so I suggest you speak to the instructors in the labs if it doesn't make sense.***

When you define a function you define a new **namespace** also called a **scope**. 

Any variable defined within the function is said to be a **local variable** and can only be accessed inside the function (the **scope** of the function). 

We use function parameters and the return value to exchange information between parts of our program.

**NOTE: I do not use the ``if __name__ == "__main__":`` block here, it is NOT required, but normally it is very good practice to use it.**

## 1. Example 1

Let's illustrate this using the example from Guttag, J.V. (2021). 

```python
def f(x):
  # variables defined here are only available to f() - local
  # we also do not have access to variables created outside of f()
  y = 1
  x = x + y
  print(f"x = {x}")
  return x


# main body of code starts here
# note we have left out if __name__ == "__main__" here. It isn't needed, but is recommended.
x = 3
y = 3
z = f(x)
print(f"z = {z}")
print(f"x = {x}")
print(f"y = {y}")
```

When a function is called, it creates a new **stack frame** and any variable defined in the function scope exists in this **stack frame** and is local to this **stack frame**. 

Once the function has finished, the **stack frame** is removed and the local variables are also removed.

Here ``x`` and ``y`` are first defined on the global frame. Then we call ``f(x)`` which creates a new **stack frame** and new variables ``x`` and ``y``. We say that information is passed to ``f()``

These two ``x``'s and ``y``s' are different! I cannot stress the importance of this. The same name, but different scope. They are not the same variable!

I have created an animation from [Python Tutor](https://pythontutor.com/visualize.html#mode=edit) which shows the **stack frame** that is created when the function is called and the other local variable ``x``.

![Scope Animation](../../../Downloads/Unit%20Material/Unit%20Material/Unit%205/assets/scope_animation.gif)

I would also copy the example into [Python Tutor](https://pythontutor.com/visualize.html#mode=edit) and follow the program line by line.

## 2. Example 2

The following code defines two functions ``f()`` and ``g()`` and calls both of them one after another.

```python
def f(x):
  """ adds 1 to x and prints result"""
  y = 1
  x = x + y
  print(f"x = {x}")
  return x

def g(x):
  """ adds 2 to x and prints result"""
  y = 2
  x = x + y
  print(f"x = {x}")
  return x

# main body of code starts here
x = 3
y = 3
z = f(x)
t = g(x)
print(f"z = {z}")
print(f"t = {t}")
print(f"x = {x}")
print(f"y = {y}")
```

This has the effect of creating a **stack frame** for ``f()``. When ``f()`` is finished the **stack frame** is removed.

Next a **stack frame** for ``g()`` is created. When ``g()`` is finished the **stack frame** is removed.

The program now drops back to the global **stack frame** and completes.

The animation below illustrates this visually.

![Scope Animation](../../../Downloads/Unit%20Material/Unit%20Material/Unit%205/assets/scope_animation_2.gif)

Again, I would also copy the example into [Python Tutor](https://pythontutor.com/visualize.html#mode=edit) and follow the program line by line.

## 3. Example 3

Each call to a function creates a new **stack frame**. 

So if we call a function from within a function, we actually create a new **stack frame** on top of the previous **stack frame**. 

The reason we call them **stack frames** is because they get stacked upon each other.

Here ``f()`` has been updated to actually call ``g()`` from within its function body. 


```python
def f(x):
  """ adds g(x) to x and prints result"""
  y = g(x)
  x = x + y
  print(f"x = {x}")
  return x

def g(x):
  """ adds 2 to x and prints result"""
  y = 2
  x = x + y
  print(f"x = {x}")
  return x

# main body of code starts here
x = 3
y = 3
z = f(x)
print(f"z = {z}")
print(f"x = {x}")
print(f"y = {y}")
```
You will see from the animation or, by experimenting on [Python Tutor](https://pythontutor.com/visualize.html#mode=edit) or using the debugger, that we end up with the following stack frames all at once.

* Global **stack frame**
* f - **stack frame** for ``f()``
* g - **stack frame** for ``g()``

Once ``g()`` finishes it is popped off (removed) from the stack and we go back to ``f()``. Once ``f()`` finishes we go back to the global frame.

Note that Python Tutor displays them underneath each other, if it helps think of them stacked on top of each other.

![Scope Animation](../../../Downloads/Unit%20Material/Unit%20Material/Unit%205/assets/scope_animation_3.gif)

***
# === TASK ===

### Don't skip reading the above lesson, in the long term it won't help you!

This one is a bit of a freebie. 

Print out the following about scope, namespaces, local variables, and stack frames

```python
print("When you define a function, you define a new namespace also called a scope.\n")

print("Any variable defined within the function is said to be a local variable and can only be accessed inside the function (the scope of the function).\n")
 
print("Calling a function creates a new stack frame and any variable defined in the function scope exists on this stack frame and is local to this stack frame.")
```
 
***

# References

Guttag, J.V. (2021). Introduction to Computation and Programming Using Python, Third Edition (3rd ed.). MIT Press.