# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What): Hayford Teye
# RRoot,1.1.2030,Created started script
# <Hayford Teye>,<2/12/2023>,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = None
strFile = "ToDoList.txt"  # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}  # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""  # A menu of user options
strChoice = ""  # A Capture the user option selection
lstRow = []  # A row of the text data from file

# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
# TODO: Add Code Here

while (True):
    print("Write or Read file Data, then type 'Exit' to quit!")
    strChoice = str(input("Choose to [W]rite or [R]ead data: "))

    # Precess the data
    if (strChoice.lower() == 'exit'):
        break

    elif (strChoice.lower() == 'w'):
        # list of files
        objFile = open(strFile, 'w')
        dicRow = {"Task": "Car", "Priority": "High"}
        objFile.write(str(dicRow["Task"]) + ',' + str(dicRow["Priority"]) + '\n')
        dicRow = {"Task": "Cloth", "Priority": "Medium"}
        objFile.write(str(dicRow["Task"]) + ',' + str(dicRow["Priority"]) + '\n')
        objFile.close()

    elif (strChoice.lower() == 'r'):
        # file to list
        objFile = open(strFile, 'r')
        for row in objFile:
            lstRow = row.split(",")  # returns a list
            dicRow = {"Task": lstRow[0], "Priority": lstRow[1].strip()}
            lstTable.append(dicRow)
        for dicRow in lstTable:
            print(lstTable)
        objFile.close()
    else:
        print('Please choose either W or R!')

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
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
    if (strChoice.strip() == '1'):
        # TODO: Add Code Here
        for dicRow in lstTable:
            print(dicRow["Task"] + '|' + dicRow["Priority"])
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        # TODO: Add Code Here
        while (True):
            strTask = input('Task: ')
            strPriority = input('Priority: ')
            lstTable.append({"Task": strTask, "Priority": strPriority})
            strChoice = input("Exit? ('y/n'): ")
            if strChoice.lower() == 'y':
                break

        continue
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        # TODO: Add Code Here
        while (True):
            strTask = input("Task to Remove: ")
            for row in lstTable:
                if row["Task"].lower() == strTask.lower():
                    lstTable.remove(row)
                    print("row removed")
                else:
                    print("row not found")
            strChoice = input("Exit? ('y/n'): ")
            if strChoice.lower() == 'y':
                break

        continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        # TODO: Add Code Here
        while (True):
            objFile = open(strFile, 'w')
            for row in lstTable:
                objFile.write(str(row["Task"]) + ',' + str(row["Priority"] + '\n'))
            objFile.close()
            print("Please save data to file!")
            break

        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        # TODO: Add Code Here
        break  # and Exit the program
    else:
        print('Please choose either 1, 2, 3, 4, or 5!')
input("Press Enter to Exit \n")
