'''
Exercise 8: Simple Search
'''

names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"] #A list that contains names.
search = input("Enter a name to search for: ") #Asks user to input what name their searching for.
if search in names:
    print(search,"is in the list.") #If the user inputted name is found in the list, it prints that the name is in the lost.
    if search=="Sam" in names:
       print("Found ",search,"!! He is in the list.") #nested if, if the name the user inputs is Sam in the range/list of
       #of names;it displays that Sam is found since the task is to find him.
else:
    print(search," is not found in the list.")
    #if the user inputted name is not in the list,it prints that the name that the user inputted is not in the list.


