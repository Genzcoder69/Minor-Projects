# First we have to import operating System
import os
def To_Do_List():

    while True:
        print("1. Add Tasks :>>>")
        print("2. Show Tasks :>>>")
        print("3. Completed Tasks :>>>")
        print("4. Skip for tomorrow")
        print("5. Quit :>>>")
        
        choice = input("Enter Your choice :>>>")

        if(choice == "1"):
            task = input("Enter your Task :>>>")
            # Here we have to use file management for storing tasks
            with open("ToDoList.txt","a") as f:
                f.write(task + "\n")

        elif(choice == "2"):
            # Here we use os to find the path that file is present in our system or not
            if not os.path.exists("ToDoList.txt"):
                print("No Tasks Found !")
            else:
                with open("ToDoList.txt","r") as f:
                    tasks = [line.strip() for line in f.readlines() if line.strip()]
                if tasks:
                    print("Your Tasks :")
                    # For loop print the tasks with proper numbering
                    for i, task in enumerate(tasks,1):
                        print(f"{i}.{task}")
                else:
                    print("No Tasks Yet !")

        # We give the number to delete the completed tasks from the file
        elif(choice == "3"):
            if not os.path.exists("ToDoList.txt"):
                print("No Tasks Found !")
            else:
                with open("ToDoList.txt","r") as f:
                    tasks = [line.strip() for line in f.readlines() if line.strip()]

                if not tasks:
                    print("No Tasks Available !")
                else:
                    print("Your Tasks :>>>")
                    for i,task in enumerate(tasks,1):
                        print(f"{i}.{task}")
                    try:
                        task_no = int(input("Enter the completed task number :>>>"))
                        if 1 <= task_no <= len(tasks):
                            completed = tasks.pop(task_no - 1)
                            print(f"Task '{completed}' marked as completed")
                            
                            with open("ToDoList.txt","w") as f:
                                for task in tasks:
                                    f.write(task + "\n")
                        else:
                            print("Invalid Task Number !")
                    except ValueError:
                        print("Please Enter a valid number !")

        # If tasks are not completed today then we have chance to skip the tasks by tomorrow
        elif(choice == "4"):
            if not os.path.exists("ToDoList.txt"):
                print("No Tasks found !")
                print("Nothing to skip !")
            else:
                with open("ToDoList.txt","r") as f:
                    tasks = [line.strip() for line in f.readlines() if line.strip()]
                    if not tasks:
                        print("No tasks available to skip !")
                    else:
                        print(f"These tasks are skipped for tomorrow :")
                        for i,task in enumerate(tasks,1):
                            print(f"{i}.{task}")
        # Quit the program
        elif(choice == "5"):
            break
        else:
            print("Wrong choice <!>")
            print("Pleas enter 1-5")

To_Do_List()
