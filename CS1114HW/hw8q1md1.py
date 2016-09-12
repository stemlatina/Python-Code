#Marilu D


def oneMonth(totalNumbDay, startDay):
    '''Month function that prints one month and then loops'''
    #Print days label
    print("Mo\tTu\tWe\tTh\tFr\tSa\tSu")

    #Print Empty Spaces
    print("\t"* (startDay - 1), end = '')

    #Start Printing First Week 
    printDay = 1
    for i in range(startDay, 8):
        print(printDay, end = "\t")
        printDay += 1
    print()
    
    #Print Remaining Weeks 
    while (printDay < totalNumbDay):
        for i in range(7):
            print(printDay, end = '\t')
            printDay += 1
            if printDay > totalNumbDay:
                break#stopslooping
        print()
            
def leapYearOrNot(year):
    '''To determine if it is a leap year or not'''
    if (year % 400 == 0):#see if its a leap year
        return True
    else:
        if (year % 4 == 0 and year % 100 != 0):
            return True
        else:#if its not then...
            return False

def getUserInput():
    '''Function that gets the users input'''
    year = int(input("Which Year? "))
    day = int(input("Start at which day? "))
#returns the year and day for the function
    return year, day

def firstDayOfMonth(totalNumbDay, startDay):
    '''Calculates the first day of each month '''
    # Shift by Days % 7 days
    FirstDayShift = totalNumbDay % 7
    newStartDay = startDay + FirstDayShift
    if newStartDay > 7:
        newStartDay -= 7
#returns the function
    return newStartDay

def printYear(year, startDay, leapYearOrNot):
    '''prints the year, month and days.'''
    monthNames = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    if leapYearOrNot == True:#if leap year add feb.29
        days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else:#if not leap year add feb.28
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    for i in range(1, 13):
        print()
        print("\t\t\t", year, monthNames[i-1])
        oneMonth(days[i-1], startDay)
        startDay = firstDayOfMonth(days[i-1], startDay)
        

def main():
    year, day = getUserInput()
    leapOrNot = leapYearOrNot (year)
    printYear(year, day, leapOrNot)

main()
