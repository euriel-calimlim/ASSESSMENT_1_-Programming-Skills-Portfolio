'''
Exercise 6: Brute Force Attack
'''

correct_password = "12345"#variable with the correct password.
attempts = 0 #how many attempts user has.
max_attempts = 5 #total number of attempts before authorities get alerted.


while attempts < max_attempts:
    password = input("Enter the password: ")
    attempts += 1 #while max attempts is more than attempts, it asks user to enter their password.
    #it's a while loop,so everytime they get the password,wrong, it increases the attempts by 1,and asks the question again.

    if password == correct_password:
        print("Access granted! You have been signed in.") #if the user inputs the correct password,
        #it will print "access granted".it ends the loop when the correct password is entered.
        break
    else: ##else statement is used if the user inputted the wrong password.
        remaining_attempts = max_attempts - attempts #remaining attempts stores the variable of max attempts (5) minus
        #the attempts the users have.
        if remaining_attempts > 0:
           print("Incorrect password.You have",remaining_attempts,"attempts remaining.") #if the remaining attempts when
            #they input wrong answers is more than 0, it will print that they are wrong and how many attempts they have left
            #to get it correct.
        else:
           print("Maximum attempts exceeded.Authorities have been alerted.") #if user inputs 5 wrong attempts,they are
            #given a warning.it ends the loop after,because remaining attempts is 0. ( because of the statement:
            #'if remaining attempts > 0:' ).