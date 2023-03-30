from pathlib import Path

def addEmployeeHours():
    print("--------------------------")
    print("----ADD EMPLOYEE HOURS----")
    print("--------------------------")
    print()
    # declare the number of employees
    nbrEmployees = 7
    # declare employee data write list
    employeeData_Write = []
    # declare employees with <30 hours
    nbrEmployees_LessThan30Hrs = 0
    # declare employees with >40 hours
    nbrEmployees_MoreThan40Hrs = 0
    # Declare Employees between 30-40 hours
    nbrEmployees_Between37_39Hrs = 0
    # Get input for user_ID, employee_name, hours worked each day and week nbr
    # Check to make sure input is valid
    while True:
        try:
            week_nbr_input =  int(input("Enter current working week (1-52) -> "))
        except ValueError:
            print("You have entered an invalid input. Please try again.")
            continue
        if (week_nbr_input < 1) or (week_nbr_input > 52):
            print("Current work week is invalid. Please input a number from 1-52")
            continue
        else:
            break
    week_nbr = "Week {}".format(week_nbr_input)
    
    # # Check if Work week is already in the .csv file
    # path = Path('./homeTracker.csv')
    # if path.is_file() == True:
    #     checkFile = open("homeTracker.csv", "r")
    #     for line in checkFile:
    #         if week_nbr in line:
    #             print("This work week already exists.")
    #             break
    #     checkFile.close()


    for nbr in range(1, nbrEmployees+1):
        # Create a list for 5 day work week
        hoursWorked = []
        # Declare hours worked
        totalHoursWorked = 0

        print("[Employee " + str(nbr) + "]")

        employee_ID = input("Enter Employee " + str(nbr) + " ID -> ")
        employee_name = input("Enter Employee " + str(nbr) + " Name -> ")
        # Put recurring information in a work string
        workStr = week_nbr + "," + employee_ID + "," + employee_name + ","

        # get hours for each day
        dayList = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        for day in dayList:
            while True:
                try:
                    hoursWorkedForDay = int(input("Enter hours worked for {} -> ".format(day)))
                except ValueError:
                    print("You have entered an invalid input. Please try again.")
                    continue
                if (0 > hoursWorkedForDay) or (hoursWorkedForDay > 24):
                    print("Hours must be between 0 - 24.")
                    continue
                else:
                    break
            # append to hours worked array (list)
            hoursWorked.append(hoursWorkedForDay)
            # add hoursWorkedForDay to totalHoursWorked
            totalHoursWorked += hoursWorkedForDay
            if (day != "Friday"):
                workStr = workStr + str(hoursWorkedForDay) + ","
            else:
                workStr = workStr + str(hoursWorkedForDay)
        # end for loop

        # total hours worked
        if (totalHoursWorked < 30):
            nbrEmployees_LessThan30Hrs += 1
        elif(totalHoursWorked > 40):
            nbrEmployees_MoreThan40Hrs += 1
        elif(totalHoursWorked >= 37 and totalHoursWorked <= 39):
            nbrEmployees_Between37_39Hrs += 1
        
        # append to employeeData_Write
        employeeData_Write.append(workStr)

        # Summary of work for each employee
        print("**********************************")
        print("Summary of work for Employee " + employee_ID)
        for i in range(0, len(hoursWorked)):
            if (hoursWorked[i] < 4):
                print("Insufficient hours worked on " + dayList[i])
            elif (hoursWorked[i] > 10):
                print ("Too many hours worked on " + dayList[i])
        print("Total hours worked for " + week_nbr + ": " + str(totalHoursWorked) + " hours.")
        if (totalHoursWorked < 30):
            print("Not enough hours worked this week")
        elif (totalHoursWorked > 40):
            print("You are working too hard!")
        print()
    
    print("**********************************")
    print("      Weekly Employee Report      ")
    print("Number of employees who worked LESS than 30 hours: " + str(nbrEmployees_LessThan30Hrs))
    print("Number of employees who worked MORE than 40 hours: " + str(nbrEmployees_MoreThan40Hrs))
    print("Number of employees who worked BETWEEN 37-39: " + str(nbrEmployees_Between37_39Hrs))
    print()
    print()

    # test the output data
    #for i in range(0, len(employeeData_Write)):
    #    print(employeeData_Write)

    # log to external file
    extFile = open("homeTracker.csv", "a")
    # loop through employee data and write each string to external file
    for entry in employeeData_Write:
        extFile.write(entry + "\n")
    #close file object
    extFile.close()

# end of addEmployeeHours()

# Function: getHoursWOrkedReport()

def getHoursWorkedReport():
    print("---------------------------")
    print("----HOURS WORKED REPORT----")
    print("---------------------------")
    print()
    # declear employee Data Read list
    employeeData_Read = []
    # read from homeTracker.csv
    path = Path('./homeTracker.csv')
    if path.is_file() == True:
        extFile = open("homeTracker.csv", "r")
    else:
        print("------------NOTICE------------")
        print("There are no hours logged yet!")
        print("------------------------------")
        return
    # loop each line in the external file
    for line in extFile:
        #append line to empWork array (list)
        if (len(line) > 0):
            employeeData_Read.append(line.rstrip())
    extFile.close()

    #reverse sort the read-in list
    employeeData_Read.reverse()

    # test the output data in employeeData_Read list to ensure that it is
    # formatted with valid data
    # for i in range(0, len(employeeData_Read)):
    #     print(employeeData_Read[i])
    #     TempWeekData = employeeData_Read[i].split(",")


    # Prompt user for how many records they want to view
    # While loop checks whether input is valid
    while True:
        try:
            nbrRecordsToDisplay = int(input("Enter number of records to display -> "))
        except ValueError:
            print("The input you have provided is invalid. Please try again.")
            continue
        else:
            break
    print()
    print("Employee work data (sorted from most revent)")
    print()
    # check if records to display is not more than the list size
    if (nbrRecordsToDisplay > len(employeeData_Read)):
        nbrRecordsToDisplay = len(employeeData_Read)
    
    #display records
    if (nbrRecordsToDisplay > 0):
        for i in range(0, nbrRecordsToDisplay):
            employeeData = employeeData_Read[i].split(",")
            print(employeeData[0])
            print("Employee ID: " + employeeData[1])
            print("Employee name: " + employeeData[2])
            print("Hours worked (Mon): " + employeeData[3])
            print("Hours worked (Tue): " + employeeData[4])
            print("Hours worked (Wed): " + employeeData[5])
            print("Hours worked (Thu): " + employeeData[6])
            print("Hours worked (Fri): " + employeeData[7])
            print("---------------------------")
    print()
#end getHoursWorkedReport() Method

#---------------------------------------------------
#Method: main()
# purpose: entry point to program
# no input paramets or returns
#----------------------------------------------------
def main():
    print("----------------------------------------------------")
    print("--DIAMOND REALITY: EMPLOYEE WORK FROM HOME PROGRAM--")
    print("----------------------------------------------------")

    # create a variable that tracks menu option made by user
    option = 1

    # prompt user with options
    while (option != 3):
        print("Menu of options")
        print("1. Enter daily hours worked")
        print("2. Produce hours-worked report")
        print("3. Exit")
        print()
        
        while True:
            try:    
                option = int(input("Enter your option 1|2|3 -> "))
            except ValueError:
                print("Your input is invalid. Please try again.")
                continue
            if (option < 1) or (option > 3):
                print("Please select an option between 1 and 3")
                continue
            else:
                break
    
        #check option entered
        if (option == 1):
            addEmployeeHours()
        elif (option == 2):
            getHoursWorkedReport()
        elif (option == 3):
            print("Thank you for using this program")
            break
    # end of main()

if __name__ == '__main__':
    main()

# see if you can make code that checks whether an existing work 
# week can overwrite the current work week to avoid duplication
# additionally see if you can prompt the user to go back in case
# of an error
