# Hackathon 

## Background 
For this Hackathon, you'll be working in groups (we'll decide them in class) to 
solve several exercises described below. For each exercise, you'll have to provide: 
    1. Code written in python for the problem in the appropriate file (e.g. your solution for exercise 1 will go in 1.py)
    2. Some kind of documentation to tell the reader what your code is doing (this could either be comments or pseudocode in a google doc)

**Important: The two components above will be weighted equally (make sure to provide comments/pseudocode)! Even if you aren't sure how 
to exactly write the code for a particular problem, you can still receive points for well-written comments and/or pseudocode. 

Each file in the problem folder will have some starter code in the form of a function.
Most of your code should be written inside the function (unless you are opening any modules or defining additional functions).  
DO NOT modify the function name or the number of parameters/arguments/inputs or any starter code unless otherwise noted. However, you may 
modify the variable names of those parameters. You should also feel free to define additional functions that 
may help you solve each problem. 

**Important: Pay attention to the wording of the question. Some questions will have you either return 
a value or print something to the terminal. Feel free to ask clarification questions if you are confused! 

**Another Note: On the last day, you'll be presenting your solutions to some of these problems to your 
instructors and your parents! Make sure that everyone in your group is comfortable (at least on a high-level) with 
each solution you come up with because everyone will have to contribute something! 

**Last Note: We encourage you to google about things you do not know (googling is a big part of programming!), but in terms 
of fariness, make sure you're not looking for complete answers to any of these problems. For instance, it's completely fair game 
to look up modules, syntax, functions/methods, etc., but you shouldn't be looking at someone else's solution to a problem that
may be similar or the same as the exercises above. 

On Friday, you'll submit your Hackathon solutions. You're instructors will grade them (with the help of an autograder), 
assigning points to each question. Whoever has the most points will be deemed the winner! 

## Problems 

#### Exercise 1 
In the ```main()``` function in 1.py, create a program that asks the user for the 
following input: 
    1. The price of an item
    2. The tax percentage (as a percent)
    3. Prints the total cost of the item (including tax) 
You may leave the ```return``` in ```main()``` unchanged. Print the number as a 
float (do not add a $ symbol), and be careful of how you should represent money as 
a float! 

Look at the example output below: 
```
$ python3 1.py

Price of item: 200
Tax percentage: 4
208.00
```

#### Exercise 2
In the ```main()``` function create a program the calculates the monthly salary of 
an employee where
    ```monthy_salary = minimum_wage + (number of years employed * 20) + (number of children * 30)```. 
The program should ask the user for: 
    1. a minimum wage (this can be a float)
    2. the number of years the worker has been employed (this can be a float)
    3. the number of children they have 

Again, pay attention to how money should be represented! 

Follow the example output: 
```
$ python3 2.py 

Minimum Wage: 600 
Number of Years Employed: 7
Number of Children: 2 
800.00
```

#### Exercise 3 
In ```main()```, write code that asks the user to enter their age 
(you may assume they enter the age they will be by the end of the year). Print 
out the year they turn 90 years old. Assume the current year is 2022. If the user 
is already 90 years old, you should still print out the year they turned 90. For example,
someone who is currently 95, turned 90 in 2017. 

Example Output: 
```
$ python3 3.py 

Enter an age: 19
2093 

$ python3 3.py 
Enter an age: 95 
2017
``` 

#### Exercise 4
The function ```search(value, list)``` takes in a list of elements and a value. The function 
should return the appropriate boolean based on whether the value is in the list or not. For this function,
all you need to do is return a value (no need to print anything here!). 

Example: 
```
search(1, [1,2,3,4,5]) => true 
search("a", [3, "a", "b", 5.6]) => true 
search(7.2, [5,6]) => false 
```

#### Exercise 5 
The function ```common(list1, list2)``` takes in two lists and returns a list that 
contains only the elements that are common between the two lists (without duplicates).
Make sure the program works on two lists of different sizes and returns a list! Again, no need
to print anything here. 

Example: 
```
common([1,1,2,3,5,9,14,17,28,56], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) => [1,2,3,5,9]
```



#### Exercise 6 
```luhn(card_number)``` is a function that takes in a credit-card number (as an integer) and returns 
true or false based on whether the card_number is valid. How do we determine if a credit card 
number is valid? Well, there's Luhn's algorithm. Based on Luhn's algorithm, you follow these steps to determine if a card is valid:
    1. Multiply every other digit by 2, starting with the number's second-to-last digit, and then add those products' digits together. 
    2. Take the sum you calculated in Step (1) and add it to the sum of the digits that were not multiplied by 2.
    3. If the total is divisible by 10, then the card number is valid. 

```
luhn(378282246310005) => true 
```
Here is a link to a few valid credit card numbers you can test with: 
<https://developer.paypal.com/api/nvp-soap/payflow/payflow-pro/payflow-pro-testing/#credit-card-numbers-for-testing>. 



#### Exercise 7 
The ```lettersum(string)``` function takes in a string as input and sums the value of the letters 
of the string where a corresponds to 1, b corresponds to 2, ..., and z corresponds to 26. 
You may assume that either the empty string or alphabetic strings will be inputted into the function. 
```
lettersum("") => 0
lettersum("a") => 1
lettersum("z") => 26
lettersum("cab") => 6
lettersum("excellent") => 100
```

#### Exercise 8 
```numcompare(numeral_one, numeral_two)``` takes in two strings representing a Roman numeral. 
A Roman numeral is a non-empty string of the characters M, D, C, L, X, V, and I, each of which 
has the value 1000, 500, 100, 50, 10, 5 and, 1. The characters are arranged in descending order 
and the total value of the numeral is the sum of the values of its characters. There are a few 
exceptions, however. Numerals such as IV, IX, XIX, XC will stand for 5, 9, 19, and 90 respectively. 
Look at this Roman numeral chart: <https://www.cuemath.com/numbers/roman-numerals-1-to-100/>. 

Otherwise, ```numcompare()``` returns true or false based on whether the first numeral is less than 
the second one (i.e. numeral_one < numeral_two). You may assume that the inputs for these functions will 
always be valid roman numerals. 

```
numcompare("I", "I") => false
numcompare("IV", "V") => true 
numcompare("I", "II") => true
numcompare("II", "I") => false
numcompare("V", "IIII") => false
numcompare("XC", "C") => true 
numcompare("MDCLXV", "MDCLXVI") => true
numcompare("MM", "MDCCCCLXXXXVIIII") => false
```

#### Exercise 9 
The country of CryptoDreamers has coins that are worth 1, 5, 10, 25, 100, and 500 currency units. 
At the bank of CryptoDreamers, you are trained to make various amounts of money by using as 
many ¤500 coins as possible, then as many ¤100 coins as possible, and so on
down.

For instance, if you want to give someone ¤468, you would give them four ¤100 coins, two
¤25 coins, one ¤10 coin, one ¤5 coin, and three ¤1 coins, for a total of 11 coins.

The ```change(amount)``` takes in a currency amount and returns the number of coins used 
to make a given amount of change. 

```
change(0) => 0
change(12) => 3
change(468) => 11
change(123456) => 254
```

#### Exercise 10 
The ```factorial(number)``` takes in an integer and computes the factorial of that integer. 
A factorial is the product of an integer and all the integers below it. For example, 
5! = 5 x 4 x 3 x 2 x 1 = 120. Note that the factorial of 0 is 1. You may assume that the factorial 
function will always take in a number greater than or equal to 0. 

```
factorial(0) => 1 
factorial(1) => 1 
factorial(2) => 2 
factorial(3) => 6 
factorial(4) => 24 
factorial(12) => 479001600
``` 

#### Exercise 11 
The nation of Examplania follows the US marginal income tax rate system and has the following tax 
brackets: 
    | income cap | marginal tax rate 
    |   :---:    |   :---: 
    |   $10000   |   0.00 (0%)
    |   $30000   |   0.10 (10%)
    |   $100000  |   0.25 (25%)
    |   --       |   0.40 (40%) 

If you're not familiar with how taxes work, each tax rate applies only to income within the specific tax 
bracket. For example, let's say someone makes $80000. The first $10000 of their income will be taxed at a 
0% rate. Then, there income from $10,000 to $30000 will be taxed at 10%. From there, the income they have from 
$30,000 to $80,000 will be taxed at 25%. So, the total amount in taxes they would have to pay would equate to: 
(10000 * 0.00) + (30000-10000) * 0.10 + (80000-30000) * 0.25 = 14,500. Watch this video for an explanation on how 
tax brackets work: <https://www.youtube.com/watch?v=VJhsjUPDulw>. Again, like in problem one and problem two, take note 
of how money values should be represented! 

The ```tax(income)``` function takes in an income and returns the amount of taxes someone of that income would own. 
Here are some examples below: 

```
tax(80000) => 14500.00
tax(35344) => 3361.40 
tax(125000) => 29500.00 
```

***Important: In the tax function, return your answer as a string rather than a float! 

#### Exercise 12
```sum_primes(number)``` is a function that takes in a number and sums all the prime numbers 
below that number (but not including the number). For example, the function call 
```sum_primes(2000)``` would sum all the primes that are strictly less than 2000. Note that
only positive integers can be prime. Return an integer representing the sum. 

#### Exercise 13 
You are given the following information, but you may prefer to do some research yourself. 
    * 1 Jan 1900 was a Monday 
    * Thirty days has September, April, June, and November. All the rest have thirty-one,
    Saving February alone, Which has twenty-eight, rain or shine. And on leap years, twenty-nine. 
    * A leap year occurs on any year evenly divisible by 4, but not on a century unless it is 
    divisible by 400. 
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to
31 Dec 2000)?

To answer this question in the ```sundays()``` function, write code that determines the number of Sundays 
that occured between the two dates above. The function takes in no arguments, but returns an integer 
representing the answer. 

#### Exercise 14 
```shiftRight(string, num)``` takes in a string and a number and will return a string that is 
shifted `num` characters to the right from the input string. 

```
shiftRight('Hello', 3) => "lloHe"
shiftRight('World', 2) => "ldWor"
``` 

#### Exercise 15 
Calculate the [additive persistence] (https://mathworld.wolfram.com/AdditivePersistence.html) of a number, defined as 
how many loops you have to do summing its digits until you get a single digit number. Take an integer N:
    1. Add its digits 
    2. Repeat until the result has one digit 
The total number of iterations is the additive persistence of N. 

Note that all single-digit numbers have an additive_persistance of 0. Negative numbers 
can also have an additive persistence of well so make sure to handle that! 

```additive_persistence(number)``` takes in an integer and then returns the additive_persistance 
of that number as an integer 

```
additive_persistence(5) => 0 
additive_persistence(-5) => 0 
additive_persistence(13) => 1 
additive_persistence(9876) => 2 
additive_persistence(-199) => 3 
```

#### Exercise 16 
```zip(list1, list2)``` takes in two lists and combines the two lists into an array 
of 2-element lists. You may assume that the two lists inputted into the function 
will always have equal length. If the two list are empty, just return the empty list. 

```
zip([], []) = []. 
zip([1, 2, 3], [5, 3, 1]) => [[1, 5], [2, 3], [3, 1]]
```

#### Exercise 17 
```unzip(lst)``` does the opposite of ```zip()``` are a list of 2-list. You may assume
that all the list in the input list are 2-element list. 

```
unzip([]) => [[], []]
unzip([[1, 5], [2, 3], [3, 1]]) => [1, 2, 3], [5, 3, 1]
``` 

#### Exercise 18 
The algorithm to calculate, referred to as "comptus", proceeds by calculating the following 
values on the basis of the year Y: 
```
a = Y mod 19 
b = Y / 100 
c = Y mod 100 
d = b / 4 
e = b mod 4 
f = (b + 8) / 25 
g = (b - f + 1) / 3 
h = (19a + b − d − g + 15) mod 30
i = c / 4 
k = c mod 4 
l = (32 + 2e + 2i - h - k) mod 17 
m = (a + 11h + 22l) / 451 
month = (h + l - 7m + 114) / 31 
day = ((h + l - 7m + 114) mod 31) + 1 
```

```comptus(year)``` takes in a year and then returns a dictionary containing a key-value 
pair of the month as a string, the day as an integer, and the year as an integer. For the months, do not abbreviate 
the names! 

```
comptus(2018) => {"month": "April", "day": 1, "year": 2018}
``` 

#### Exercise 19 
```largest(lst)``` takes in a list and returns the "largest" element in the list. 
The input list can have elements of any type (i.e. strings, booleans, integers, floats, even
lists). How can we compare strings to integers or floats or booleans? Here, we'll say 
a "string" is larger than a number of float if the number of characters it has is greater
than the value of the integer or float. The say will apply for a list potentially being larger
than a integer or float. As for booleans, we will say that the value ```true``` will be represented 
by the value ```0``` while ```false``` will be represented by the value 1. 

So, if you have a list such as: 
```[[1,2,3], 6, "hello world", 7.5, true, false]```
The largest item in the list would be the string ```hello world``` which has 11 characters. 
The smallest value in the list would be true (i.e. 0). 

In ```largest(lst)```, return whatever the largest value is.

```
largest([[1,2,3], 6, "hello world", 7.5, true, false]) => "hello world"
```

#### Exercise 20 
Following the idea of "largest" provided in problem 19, sort a list from the smallest
value to the largest value. Write code inside the ```sort2(lst)`` function. 

```
sort2([[1,2,3], 6, "hello world", 7.5, true, false]) => [true, false, [1,2,3], 6, 7.5, "hello world"]
```

