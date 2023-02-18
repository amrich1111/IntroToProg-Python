# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoList.txt" into a python Dictionary.
#              Add each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# Aimee Richardson, 2/13/23,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
toDoFile = "ToDoList.txt"   # An object that represents a file
lstRow = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strChoice = ""  # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load  any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
# Try to open and load data from existing file, if a file does not exist the program will continue
try:
    objFile = open(toDoFile, "r")
    for row in objFile:
        lstRow = row.split(",")
        dicRow = {"Task": lstRow[0], "Priority": lstRow[1].strip()}
        lstTable.append(dicRow)
except:
    pass

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the usr
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks

    # Step 3 - Show the current items in the table
    if (strChoice.strip() == "1"):
        # Attempt to open and display data from table to the user, if it does not already exist, display message to user
        if (len(lstTable) > 0):     # Check if there is data in the table
            print("Task | Priority")
            for row in lstTable:
                print(row["Task"] + " | " + row["Priority"])
        else:   # If there is no data, display message to user
            print("Your to-do-list does not exist! Add tasks to display current data.")
        continue

    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == "2"):
        # Ask user to input a task and a priority, then add the inputted data to table and display message to user when complete
        strTask = input("Task: ").strip().title()
        strPriority = input("Priority: ").strip().title()
        lstTable.append({"Task": strTask, "Priority": strPriority})
        print("Task added!\n")
        continue

    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == "3"):
        # Ask user which task they would like to remove from the list
        strRemoveTask = input("Which task would you like to remove?: ").strip()

        # Count number of tasks incase multiple have the same name
        taskCount = 0
        for row in lstTable:
            if (row["Task"].lower() == strRemoveTask.lower()):
                taskCount += 1

        if(taskCount > 1):  # If there are multiple tasks with the same Task name, ask user which to delete
            print("\nMultiple tasks found. Indicate which task you would like to remove!\n")
            for row in lstTable:
                if (row["Task"].lower() == strRemoveTask.lower()):
                    taskIndex = lstTable.index(row)
                    print(str(taskIndex + 1) + ". " + row["Task"] + " | " + row["Priority"])
            removeChoice = input("\nPlease enter the task number you would like to remove: ")
            try:    # Try to remove inputted item from list, if index does not exist display message to user
                lstTable.pop(int(removeChoice) - 1)  # Using pop to remove item from list based on index
                print("The task has been removed!\n")
            except:
                print("\nInvalid entry! Task entered does not exist.")
        elif(taskCount == 1):   # If only 1 task has the inputted name, remove item
            taskIndex = ""
            for row in lstTable:
                if (row["Task"].lower() == strRemoveTask.lower()):
                    taskIndex = lstTable.index(row)
            lstTable.pop(taskIndex)
            print("The task has been removed!\n")
        else:   # If no task has the inputted name, display message to user
            print("Task not found!")
        continue

    # Step 6 - Save tasks to the ToDoList.txt file
    elif (strChoice.strip() == "4"):
        # Open file and write the user's inputted data to the file
        objFile = open(toDoFile, "w")
        for row in lstTable:
            objFile.write(str(row["Task"]) + "," + str(row["Priority"] + "\n"))
        objFile.close()
        print("To Do List Saved!")
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == "5"):
        # Display message to user and break out of menu loop
        print("You have exited. Goodbye!")
        break  # and Exit the program
