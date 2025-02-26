import model.task
import os
import json

print("TASK TRACKER MENU")

opt = 0
tasks_list = []
file = "json/tasks.json"


while opt != 9 or (opt in [1,2,3,4,5,6,7,8]):
    # User menu
    print("1- Add task")
    print("2- Update task")
    print("3- Delete task")
    print("4- Mark task in progress")
    print("5- Mark task done")
    print("6- Tasks done")
    print("7- Tasks not done")
    print("8- Tasks in progress")
    print("9- Exit menu")
    opt = int(input(""))
    #In case input is invalidn
    if(opt not in [1,2,3,4,5,6,7,8,9]):
        print("Invalid option, try again!")

    match opt:
        case 1:
            descr = input("Task description: ")
            task = model.task.Task
            task1 = task.add_task(descr)
            tasks_list.append(task1.to_dict())
            task1.save_in_json(file, tasks_list)
            #Add task
        case 2:
            task_id = int(input("Task id: "))
            new_descr = input("New task description: ")
            task = model.task.Task
            data = task.get_task_from_json(file)
            print(data)
    

            print("Updating task")  
        case 3:
            print("Deleting task")
        case 4:
            print("Task in progress")
        case 5: 
            print("Task done")
        case 6:
            print("Listin finished task")
        case 7:
            print("Listing not finished task")
        case 8:
            print("Listing task in progress")
        case default:
            print("Good bye!")



