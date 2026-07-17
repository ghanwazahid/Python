tasks=[]
print ("Lets make To-Do-List")
while True:
    print("\n=== To Do List ===")
    print("1. Add Task")
    print("2. View Task")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice:")

    if choice== "1":
        task=input("Enter Task:  ")
        tasks.append(task)
        print("Task added successfully!")

    elif choice=="2":
        if len(tasks) ==0:
            print("No tasks found")
        else:
            print("Your Task: ")
            for task in tasks:
                print("-" , task)

    elif choice=="3":
        if len(tasks) ==0:
            print("No tasks to remove")
        else:
            task=input("Enter tasks to remove. ")
        if task in tasks:
            tasks.remove(task)
            print("Tasks to removed successfully")
        else:
            print("Task not foud")

    elif choice =="4":
        print("GoodBye!")
    

    else:
        print("Invalid choice! Please try again.")  

