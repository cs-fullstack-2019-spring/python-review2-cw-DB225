def main():
    problem()


#PROBLEM
#Create a task list. A user is presented with the text below. Let them select an option to list all of their tasks, add a task to their list, delete a task, or quit the program.
#Make each option a different function in your program.
# Do NOT use Google. Do NOT use other students. Try to do this on your own.
#Congratulations! You're running [YOUR NAME]'s Task List program.
#What would you like to do next?
#1. List all tasks.
#2. Add a task to the list.
#3. Delete a task.
#0. To quit the program

def problem():
    taskArray = ["work", "gym", "cooking", "homework"]
    userInput = ''
    while(userInput.lower() != "y"):
        userInput = input("Do you want to run the Task?\nY or N ")
        continue

    print("Congratulations! You're running Didi's Task List program.")
    userInput2 = input("What would you like to do next?\n1.List all tasks\n2. Add a task to the list\n3. Delete a task.\n0. To quit the program\n")
    while(userInput2 != '0'):
        if (userInput2 == '1'):
            for el in taskArray:
                print(el)
            userInput2 = input("What would you like to do next?\n")
            continue
        if (userInput2 == '2'):
            userInput2 = input("which task do you want to add?\n ")
            taskArray.append(userInput2)
            print(taskArray)
            userInput2 = input("What would you like to do next?\n")
            continue

        if(userInput2 == '3'):
            userInput2 = input("which task do you want to remove?\n ")
            while userInput2 not in taskArray:
                print("NOT IN ARRAY!!! TRY AGAIN!")
                userInput2 = input("which task do you want to remove?\n ")
            else:
                taskArray.remove(userInput2)
                print(taskArray)
                userInput2 = input("What would you like to do next?\n")

        else:
            continue



##################################################################################
if __name__ == '__main__':
    main()