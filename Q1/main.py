# . Develop a function f(n) that will be looping from 1 to n
# . During the looping, when the counter is divided by 3, print "fizz"
# . During the looping, when the counter is divided by 5, print "buzz"
# . During the looping, when the counter is divided both 3 and 5, print "fizzbuzz"
# . else print out number
# . In the end of the program, run f(15)
# . Keep the program until the demo session


def f(n):
    if isinstance(n, int) and n >= 0:
        for n in range(n):
            value = n + 1
            if value % 3 == 0 and value % 5 == 0:
                print("fizzbuzz")
            elif value % 3 == 0:
                print("fizz")
            elif value % 5 == 0:
                print("buzz")
            else:
                print(value)


f(15)
