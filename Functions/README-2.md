
# Functions

Q2. What is the difference between a parameter and an argument?
```
def Explanation (parameter):
    pass

def __main__()
    argument = "This is an argument"
    Explanation(argument)
```

Q3. All functions in Python by default return …?
```
None
```

Q4. What are keyword arguments and when should we use them?
```
Key word arguments are the arguments that are passed by giving them a name.

Example: 
-> kwargs are example of Keyword arguments.
Use: 
-> When the number of paraments are decided on run time.

def Function(**kwarg):
    pass
def __main__():
    Funciton(first = "Hi", second = "Bye")
```

Q5. How can we make a parameter of a function optional?
```
Using args and kwargs

def Function (n1, n2, n3, *args, **kwargs):
    pass

def __main__()
    Function(1, 2, 4, 5, 6, 7, number=89, another=90)
```

Q6. What happens when we prefix a parameter with an asterisk (*)?
```
Then we shall be able to provide varibale number of arguments. 
def Function (n1, n2, n3, *args):
    pass

def __main__()
    Function(1, 2, 4, 5, 6, 7)
```

Q7. What about two asterisks (**)?
```
Then we shall be able to send variable number of key value pairs to a Function.

def Function (n1, n2, n3, **kwargs):
    pass

def __main__()
    Function(1, 2, 4, number=89, another=90)

```