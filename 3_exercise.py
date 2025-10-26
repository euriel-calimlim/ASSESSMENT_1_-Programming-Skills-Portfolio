"""
Exercise 3: Biography
"""
name = input("Enter your name: ")
hometown = input("Enter your hometown: ")
age = int(input("Enter your age: "))
#asks for user to input their name, hometown and age.
#age variable uses 'int(input' which only allows users to input integer data type.
biography={"name=":name,"hometown=":hometown,"age=":age} #Create a dictionary called 'biography' to store the user's information
# The questions are strings like "name=",etc.
# The answers are the user inputs stored in the variables above
for question,answer in biography.items(): #Using a For-loop  to loop through each question and answer pair in
    #the 'biography' dictionary

    print("\n",question,answer) #prints on a new line;
    #the key(e.g. "name="), then the corresponding value that the user inputs for that question(e.g. jonathan).


