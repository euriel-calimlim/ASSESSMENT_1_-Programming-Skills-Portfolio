'''Exercise 10: Is it even? - 35 Marks
Write a program that tests if a value is even or odd. Follow the instructions outlined below:

Instructions:
•The program should ask the user for a number from within the main function.
•The entered number should be passed to a function that determines if the value is even or odd.
•The function should return a message indicating whether the number is even or odd.
•The message returned by the function should be printed from within the main function.'''
def even_or_odd(number):  #A def function used to define a function;checks if the given number is even or odd.in this case,
    #the variable 'number' is our parameter in the function.
    if number % 2 == 0:  #If the number divided by 2 has no remainder, it's even.
        return f"{number} is even." #Using return function to send the message that their number is even
        # back to main() function so it can be used/printed later.
    else: #Else; If there is a remainder, the number is odd.
        return f"{number} is odd." #Returns the message that the number they inputted is odd.

def main():  #Asks the user to input a number from within a main function.
    u_input = input("Please enter a number: ")
    number = int(u_input)
    #'u_input' Asks the user to input a number,'number' converts user input into integer and stores that value.
    u_message = even_or_odd(number) #The function will return a message, which is stored in this variable u_message.
    print(u_message) #Prints the message from the function 'even_or_odd'; in this case the message '{number} is even.',
    #or '{number} is odd.'.This is possible due to return functions from these messages.

if __name__ == "__main__":
    main() #Calls the main() function only when the script is run directly.
