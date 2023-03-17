def addEmployeeHours():

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

    for nbr in range(1, nbrEmployees+1):
        # Create a list for 5 day work week
        hoursWorked = []
        # Declare hours worked
        totalHoursWorked = 0

        print("[Employee " + str(nbr) + "]")

        employee_ID = input("Enter Employee " + str(nbr) + " ID -> ")
        employee_name = input("Enter Employee " + str(nbr) + " Name -> ")
        # I do not understand the next line lmao
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
        print("Something idk")
        print("Summary of work for Employee " + employee_ID)
        for i in range(0, len(hoursWorked)):
            if (hoursWorked[i] < 4):
                print("Insufficient hours worked on " + dayList[i])
            elif (hoursWorked[1] > 10):
                print ("Too many hours worked on " + dayList[i])
        print("Total hours worked for " + week_nbr + ": " + str(totalHoursWorked) + " hours.")
        if (totalHoursWorked < 30):
            print("Not enough hours worked this week")
        elif (totalHoursWorked > 40):
            print("You are working too hard!")
        print()
    
    print("Test track")
    print("Weekly Employee Report")
    print("Number of employees who worked LESS than 30 hours: " + str(nbrEmployees_LessThan30Hrs))
    print("Number of employees who worked MORE than 40 hours: " + str(nbrEmployees_MoreThan40Hrs))
    print("Number of employees who worked BETWEEN 37-39: " + str(nbrEmployees_Between37_39Hrs))
    print()
    print()
    # log to external file
    extFile = open("homeTracker.csv", "a")
    # loop through employee data and write each string to external file
    for entry in employeeData_Write:
        extFile.write(entry + "\n")
    #close file object
    extFile.close()

addEmployeeHours()
# end of addEmployeeHours()

# Function: getHoursWOrkedReport()
