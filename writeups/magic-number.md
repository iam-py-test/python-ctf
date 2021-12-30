## How to solve Magic Number
There are two ways you can hack this game: <br>
1. [Exploiting the math function](#exploiting-the-math-function)
2. [ Exploiting the type check](#exploiting-the-type-check)

It really is impossible to win without hacking it<br>

### Exploiting the math function
The math function uses eval to get the result of the inputted data. <br>
The problem is that eval runs it runs it as Python code, which means we can just enter `math randnumb` and get the number:
![image](https://user-images.githubusercontent.com/84232764/147794115-fd3c0c6c-127b-45a5-a3e3-645a97c0a69d.png)<br>
However, we still can not set the points value to arbitrary values:
![image](https://user-images.githubusercontent.com/84232764/147794337-6f7b9ee5-6d91-4d6d-b7c4-35cfc00da9a2.png)<br>
So to win, we have to spam `math randnumb`, right?

### Exploiting the type check
If you input a wrong number, you get "wrong number", but if you input text, you get the help screen. Which means it is checking if you inputted a number. <br>
If we look at the source code, we see that check is run inside exec, which runs the string as Python code. However, we tried to simply input something like `print("hacked")`, it will fail.<br>
What we need to do is escape the `int` function. The end command which works is `"1");points += 999999999999999999999999999999999999999;print(randnumb`: <br>
![image](https://user-images.githubusercontent.com/84232764/147794616-684b8c09-8a65-4d6e-b37c-71f2aefdffe6.png)<br>
It worked! The end print of the number is unneeded, however, it does need something valid to match the end ) from the `int` function.

### Version 2
Version 2 is a bit more complex, and fixes the type check exploit, so the steps above won't work on it

