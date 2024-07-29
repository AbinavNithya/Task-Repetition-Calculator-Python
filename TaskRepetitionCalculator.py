import math
import datetime
from datetime import datetime
from datetime import timedelta

# initialising variables

breaksTime = 0
validOption = False
validOptionBreaks = False
validUserOptionBreaks = ""
validUserOption = ""
breaks = False
scaleOfTimeBreaks = ""
numberOfTimes = 0
timePerTask = 0
taskAdjustedBreaksTime = 0

# initialise customer's start date
startDate = input("What date do you want to start your task on? (Please enter date in the DD-MM-YYYY format) : ")
dt_startDate = datetime.strptime(startDate, "%d/%m/%Y")

endDate = input("What date do you want to end your task on? (Please enter date in the DD-MM-YYYY format) : ")
dt_endDate = datetime.strptime(endDate, "%d/%m/%Y")

totalDays = dt_endDate - dt_startDate
totalSeconds = totalDays.total_seconds()
scaleAdjustedTime = 0

# selecting scale of time and input validation

while validOption == False:

    userOptionInput = input("Does your task take - seconds, minutes, hours, days, months or years to complete? keep in mind that when a future question asks you for how long your task takes, it only accepts whole numbers): ")

    if userOptionInput == "seconds" or userOptionInput == "minutes" or userOptionInput == "hours" or userOptionInput == "days" or userOptionInput == "months" or userOptionInput == "years":
            
        validOption = True
        validUserOption = userOptionInput
        print("Thanks for entering a valid input!")
            
    else:
            
        print("Invalid option")

scaleOfTime = validUserOption

if scaleOfTime == "minutes":
    
    scaleAdjustedTime = totalSeconds / 60

elif scaleOfTime == "hours":
    
    scaleAdjustedTime = totalSeconds / 3600

elif scaleOfTime == "days":
    
    scaleAdjustedTime = totalSeconds / 86400

elif scaleOfTime == "months":
    
    scaleAdjustedTime = totalSeconds / 2629746
    
elif scaleOfTime == "years":
    
    scaleAdjustedTime = totalSeconds / 31556952
    
else:
    
    scaleAdjustedTime = totalSeconds
    
timePerTask = int(input("How many " + scaleOfTime + " does 1 repetition of your task to complete? (Please enter as a whole number) : "))

if scaleOfTime == "minutes":
    
    timePerTask = timePerTask * 60

elif scaleOfTime == "hours":
    
    timePerTask = timePerTask * 3600

elif scaleOfTime == "days":
    
    timePerTask = timePerTask * 86400

elif scaleOfTime == "months":
    
    timePerTask = timePerTask * 2629746
    
elif scaleOfTime == "years":
    
    timePerTask = timePerTask * 31556952

else:
    
    timePerTask = timePerTask
    
cool = True

while cool == True:
    
    ifBreaks = input("Does your task require you to take breaks e.g. sleep, rest? (please enter Yes or No) : ")
    
    if ifBreaks == "Yes" or ifBreaks == "No":
    
        print("Thank you for entering a valid input!")

        cool = False
    
    else:
        
        print("Your answer was not Yes or No. Please try again.")
        
if ifBreaks == "Yes":
    
    breaks = True
    
else:
    
    breaks = False
    
while validOptionBreaks == False:

    userOptionInputBreaks = input("Does your break take - seconds, minutes or hours to complete (keep in mind that when a future question asks you for how long your breaks take, it only accepts whole numbers): ")

    if userOptionInputBreaks == "seconds" or userOptionInputBreaks == "minutes" or userOptionInputBreaks == "hours":
            
        validOptionBreaks = True
        validUserOptionBreaks = userOptionInputBreaks
        print("Thanks for entering a valid input!")
        scaleOfTimeBreaks = validUserOptionBreaks
        
    else:
            
        print("Invalid option")

if breaks == True and scaleOfTimeBreaks == "seconds":
    
    breaksTime = int(input("Please enter the amount of seconds that each break takes (Please enter as a whole number) : "))
    taskAdjustedBreaksTime = breaksTime * 1
    totalTime = timePerTask + taskAdjustedBreaksTime
    numberOfTimes = totalSeconds / totalTime
    if numberOfTimes < 1:
        
        numberOfTimes = 0
    
    print("You are able to complete your task " + str(math.floor(numberOfTimes)) + " times in " + str(scaleAdjustedTime) + " " + scaleOfTime + " with breaks of " + str(breaksTime) + " " + scaleOfTimeBreaks)

elif breaks == True and scaleOfTimeBreaks == "minutes":
    
    breaksTime = int(input("Please enter the amount of minutes that each break takes (Please enter as a whole number) : "))
    
    taskAdjustedBreaksTime = breaksTime * 60
    totalTime = timePerTask + taskAdjustedBreaksTime
    numberOfTimes = totalSeconds / totalTime
    if numberOfTimes < 1:
        
        numberOfTimes = 0
    
    print("You are able to complete your task " + str(math.floor(numberOfTimes)) + " times in " + str(scaleAdjustedTime) + " " + scaleOfTime + " with breaks of " + str(breaksTime) + " " + scaleOfTimeBreaks)

elif breaks == True and scaleOfTimeBreaks == "hours":
    
    breaksTime = int(input("Please enter the amount of hours that each break takes (Please enter as a whole number) : "))
    
    taskAdjustedBreaksTime = breaksTime * 3600
    totalTime = timePerTask + taskAdjustedBreaksTime
    numberOfTimes = totalSeconds / totalTime
    if numberOfTimes < 1:
         
        numberOfTimes = 0

    print("You are able to complete your task " + str(math.floor(numberOfTimes)) + " times in " + str(scaleAdjustedTime) + " " + scaleOfTime + " with breaks of " + str(breaksTime) + " " + scaleOfTimeBreaks)
    
else:
    
    numberOfTimes = totalSeconds / timePerTask
    if numberOfTimes < 1:
        
        numberOfTimes = 0
    
    print("You are able to complete your task " + str(math.floor(numberOfTimes)) + " times in " + str(scaleAdjustedTime) + " " + scaleOfTime)