
# Control Flow Quetions




## Q1

```pyhton
What is the the difference between 10 / 3 and 10 // 3?
```

10/3 will return 3.33 where as 10//3 will remove the numbers after the decimal point and just return 3

## Q2

```pyhton
What is the result of 10 ** 3?
```
10**3 basically means 10^3. Hence, it will return 1000.

## Q3

```pyhton
Given (x = 1), what will be the value of after we run (x += 2)?
```
x+=2 basically means x=x+2. The Final answer will be 3

## Q4

```pyhton
How can we round a number?
```
Using the round() function. Examples: 
* x = round(5.994, 0) = 6.0  
* x = round(5.994, 1) = 6.0  
* x = round(5.994, 2) = 5.99  
* x = round(5.994, 3) = 5.994  

## Q5

```pyhton
What is the result of float(1)?
```
float(1) = 1.0
## Q6

```pyhton
What is the result of bool(“False”)?
```
Writing bool("False") is no different from wiritng bool("some string"). bool() will return a False value when we use None, "", False or 0.
## Q7

```pyhton
What are the falsy values in Python?
```
* None
* False
* 0
* ""

## Q8
```
What is the result of 10 == “10”?
```
They have different data types, hence the result will be False.
## Q9
```
What is the result of “bag” > “apple”?
```
The answer is True. Characters of both strings are being compared one by one using their UniCode. We get the answer True because the unicode of b is lesser than unicode of a.

## Q10
```
What is the result of not(True or False)?
```
The answer if False. (0||1) = 1 and then ~ of 1 is 0. 

## Q11
```
Under what circumstances does the expression 18 <= age < 65 evaluate to True?
```
The expression will be true when either of the given condition is True :
* Age = 18
* Age is > 18
* Age is < 65

## Q12
```
What does range(1, 10, 2) return?
```
* 1 is the starting point
* 10 is the terminating condition 
* 2 means value will be incremented by 2.
Hence, the answer will be 1, 3, 5, 7, 9

## Q13
```
Name 3 iterable objects in Python.
```
* list
* dict
* set 
* tuple