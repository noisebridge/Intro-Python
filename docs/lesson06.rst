Loops
=====

In programing a loop is a statement that allows a block of code to be repeated. In python we have two different types of loops. A while loop and a for loop. 

While Loops
-----------
While loops always start with a test condition just like we did with our if statements. The loop will execute the block of code over and over again until the test is no longer true. 
::
    i = 0
    while i < 5:
        print i
        i += 1

With all loops it is important that you write your code so the test will eventually be false. If you don't you will write a loop that never ends or better known as an infinite loop. While there might be a reason to write an infinite loop make sure you know exactly why you are doing it. 
::
    i = 1
    while i > 0:
        print i
        i += 1

You can use any valid test in python to enter the loop. In this example we use a dummy value to prime the loop. 
::
    word = 'dummy'
    while word:
        word = raw_input('Enter a Word: ')
        print 'You entered: %s' % (word)

This loop works fine for the most part. But the first problem we have is the print statement runs one last time after the user wants to exit the program. Lets re-write the loop using the while True syntax that is popular in python. This method avoids the need to prime the loop by setting the test to True. When we use this loop we need to use a break statement to break out of the loop. 
::
    while True:
        better = raw_input('Enter a Word: ')
        if not better: break
        print 'You entered: %s' % (better)

For Loops
---------
The other type of loop in python is a for loop. For loops are used for iterating over a a set of values when the set is known before the loop begins. 
::
    range(20)
    for r in range(20):
        print r

The for loop is really you work horse as far as looping goes. In python you can loop over many different data types. We have not covered dictionaries yet, but here is a more advanced example we will see in a couple of weeks.
::
    member = {'First': 'Kellan', 'Last': 'Jacobs', 'Phone': '(415)-555-1212'}
    for key, value in member.items():
        print "{0}: {1}".format(key, value)

Continue Statement
------------------
The continue statement is used when we want to stop this iteration of the loop but we don't want to break out of the loop all together. When a loop hits a continue statement it will stop execution of the current loop block and start over at the next iteration at the top of the loop. 
::
    for r in range(20):
        if r % 2:
            continue
        print r


