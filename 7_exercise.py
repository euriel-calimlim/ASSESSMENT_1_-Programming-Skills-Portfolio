'''
Exercise 7: Some Counting - 20 Marks
Use your newly acquired knowledge of the for loop to complete the following tasks. Print all values to the console in each case.

LINE 11= Write a loop that counts up from 0 to 50 in increments of 1.
LINE 15= Write a loop that counts down from 50 to 0 in decrements of 1.
LINE 19= Write a loop that counts up from 30 to 50 in increments of 1.
LINE 23= Write a loop that counts down from 50 to 10 in decrements of 2.
LINE 27= Write a loop that counts up from 100 to 200 in increments of 5. You may include all loops in a single project
'''
#using 'for' loops for this task."i" is just a variable that will run until the intended value. it prints every number
#until the fin

for i in range(51): #inputs numbers starting from 0 and stopping right before reaching 51, so until 50.
    print(i) #prints the numbers given in the for loop.
print("\n") #prints a blank/new line to separate each loop.

for i in range(50,-1,-1): #a range that starts at 50 and stops before reaching -1 (so 0),at decrements of -1 after each number.
    print(i)
print("\n")

for i in range(30,51): #a range that starts at 30 and ends before reaching 51, so it will print numbers 30 up till 50.
    print(i)
print("\n")

for i in range(50,9,-2): #a range that starts at 50 and ends before reaching 9,so it will print numbers 50 until 10,at decrements of -2 after each number.
    print(i)
print("\n")

for i in range(100,201,5): #a range that starts at 100 and ends before reaching 201,so it will print numbers 100 until 200,at increments of +5 after each number.
    print(i)
#no need to print a new line as it is the last loop.
