month_days = { 1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31 } #dictionary that stores
#the month number, and how many days are in that month.

month_number = int(input("Enter the month number (1-12): ")) #Asks user to input amonth number.


if month_number in range(1, 13): #checks if the user input is a valid month number in the range january to december. (1-12).

    if month_number == 2:
        leap_year= input("Is it a leap year? (yes/no): ").lower()
        if leap_year == "yes":
            days = 29
        else:
            days = 28
            #Using a Nested-If,if the user inputs the number month of february(2), it asks if the year is a leap year.  if it is a leap year,
            # it will display the days as the value 29. if the user inputs that it is not a leap year,
            # it displays the days as the value 28.
    else:
        days = month_days[month_number]
    print(f"Number of days in month {month_number}: {days}")
    #For all other months, get the number of days from the dictionary and store it in a variable called days.
    #then, print the user inputted month number, and how many days is in that month number.
else:
    print("Invalid month.Please enter a month number between 1 and 12.") #If the month number is outside the valid range,
    #it will show this error message.