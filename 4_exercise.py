""""
Exercise 4:PRIMITIVE QUIZ
"""

answer=input("What is the capital of France?=>") #Asks user a question and allows them to input their answer.
if answer.lower()=="paris": #answer.lower() converts users answers to lowercase,it ignores if the answer is "paris", "Paris", and "PaRis,eg.
   print("Correct!The capital of France is "+answer+" !\n")
   print("Congratulations!You have unlocked a new quiz!\n")#if answer is correct, it is displayed they are correct.gives a new quiz after.\n prints new line.
else:
   print("Incorrect!The capital of France is not",answer,". Please attempt this new quiz.\n")  #if answer is incorrect, this message is displayed.

#putting 10 european countries in a list and putting their capital cities in a separate list.
countries=("Italy","United Kingdom","Germany","Spain","Portugal","Greece","Netherlands","Denmark","Belgium","Ireland")
capitals=("Rome","London","Berlin","Madrid","Lisbon","Athens","Amsterdam","Copenhagen","Brussels","Dublin")
score=0#the base score for the quiz.
index=0 #starts from the very first country. in this case it is Italy.In the list, Italy is 0,United Kingdom is 1,Germany is 2,so on.
while index < 10:
   country = countries[index]
   capital = capitals[index]#country and capital are new variables. they store the index of the lists countries and capitals.
#while loop get the current country and its capital using countries[index] and capitals[index]. the loop runs until 10,because there are 10 countries and capitals.
   answer_q2 = input("What is the capital of "+country+"?=>") #asks the user what the capital city of the country in the index is.
   if answer_q2.lower() == capital.lower():
       score += 1
       print("Correct!\nYou scored a point!Your total score is",score,"out of 10!\n")
       index += 1
#.lower(): function converts the variables into lowercase, so user answer is no longer case-sensitive. User can input rOmE, ROME,etc and the answer will still be correct.
#if user inputted answer is equal to the capital city of the country in the index,it prints a correct message and adds the score by +1 when the answer inputted is correct.
#and displays the current score.then, it moves on to the next country in the list by using index +=1.
   else:
    print("Wrong! The correct answer is "+capital+".Your total score was",score,"out of 10. Please try again.")
    break # else function is used when the answer is wrong,then it displays the correct answer to the question, and displays their final score.
    #break function is used to end/break the while loop, ending the quiz.

if index == 10:#if all the 10 questions were answered correctly/if index reaches 10:
    print("Congratulations!You have completed the quiz!!! :)")#congratulations message displayed.


