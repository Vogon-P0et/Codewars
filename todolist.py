#To Do List

active = True
tasks = []

while active:
    print("\nWelcome to your brain...Here are the things it thinks you need to do...")
    print("\nPlease select one of the following:\n")
    print("1. Add tasks")
    print("2. View tasks")
    print("3. Delete tasks")
    print("4. Quit the Application\n")
    print("You may type \"quit\" at any time to exit the application\n")
    
    choice = input("Please select from options 1-4\n")
    
    if choice == "1":
        task_name = input("\nWhat would you like to name this task?\n")
        if task_name.lower() == "quit":
            break
        else:
            tasks.append(task_name) #possibly adding a dictionary here
            print(f"\n{tasks[-1]} has been successfully added.\n")
    elif choice == "2":
        if len(tasks) == 0:
            print("\n\nNotice- Your list is currently empty.")
        else:
            print("Here is your task list:\n\n")
            for i in range(0,len(tasks)):
                print(f"{i+1} - {tasks[i]}")
    elif choice == "3":
        if len(tasks) == 0:
            print("\n\nNotice- Your list is currently empty.")
        else:
            try:
                print("Here is your task list:\n\n")
                for i in range(0,len(tasks)):
                    print(f"{i+1} - {tasks[i]}")
                item_to_delete = input("\n\nPlease select the number of the task you would like deleted\n\n")
                tasks.pop(int(item_to_delete)-1)
            except IndexError:
                print("You have typed an invalid entry, please try again")
    elif choice == "4":
        active = False
        print("Goodbye!")
    elif choice.lower() == "quit": 
        break 
    else:
        print("Incorrect selection.\n\nPlease try again.\n")
        