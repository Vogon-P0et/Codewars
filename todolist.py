#To Do List

active = True
tasks = []

while active:
    print("\nWelcome to your brain...Here are the things it thinks you need done...")
    print("\nPlease select one of the following:\n")
    print("1. Add tasks")
    print("2. View tasks")
    print("3. Delete tasks")
    print("4. Quit the Application\n")
    print("You may type quit at any time to exit the application\n")
    
    choice = input("Where would you like to begin? Please select from options 1-4\n")
    
    if choice == "1":
        task_name = input("\nWhat would you like to name this task?\n")
        if task_name.lower() == "quit":
            break
        else:
            tasks.append(task_name)
        print(f"{tasks[-1]} has been successfully added.")     
    if choice == "2":
        for task in tasks:
            print(f"{tasks}, \n")
    if choice == "3":
        for task in tasks:
            print(task)
        item_to_delete = input("""Which task would you like to delete?
                               \nPlease choose the task based on the 
                               position on the list""")
    if choice == "4":
        active = False
        print("Goodbye!")
    if choice.lower() == "quit": #again not needed for terminal but possibly for an application? not sure
        break 
    else:
        print("Incorrect selection.\n\nPlease try again.\n")