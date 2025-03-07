import model.task as Task
import os
import json


print("TASK TRACKER MENU")

opt = 0
file = "json/tasks.json"
task_instance = Task.Task()
tasks_list = task_instance.get_task_from_json(file)

def obtener_ancho_consola():
    try:
        columnas, _ = os.get_terminal_size()
        return columnas
    except:
        return 80 

def centrar_texto(texto):
    ancho_consola = obtener_ancho_consola()
    espacios = (ancho_consola - len(texto)) // 2
    texto_centrado = ' ' * espacios + texto
    return texto_centrado

def mostrar_menu():
    menu = [
        "1- Add task",
        "2- Update task",
        "3- Delete task",
        "4- Mark task in progress",
        "5- Mark task done",
        "6- Tasks done",
        "7- Tasks not done",
        "8- Tasks in progress",
        "9- Exit menu"
    ]
    print(centrar_texto("=== TASK TRACKER MENU ==="))
     
    for opcion in menu:
        print(centrar_texto(opcion))

while opt != 9 or (opt in [1,2,3,4,5,6,7,8]):
    # User menu
    mostrar_menu()
    opt = int(input(""))
    #In case input is invalidn
    if(opt not in [1,2,3,4,5,6,7,8,9]):
        print("Invalid option, try again!")

    match opt:
        case 1:
            descr = input("Task description: ")
            task1 = task_instance.add_task(descr)
            tasks_list.append(task1.to_dict())
            task1.save_in_json(file, tasks_list)
        case 2:
            task_id = int(input("Task id: "))
            new_descr = input("New task description: ")
            task_list = task_instance.update_task(tasks_list, task_id, new_descr)
            task_instance.save_in_json(file, task_list)  
        case 3:
            task_id = int(input("Task id: "))
            tasks_list = task_instance.delete_task(tasks_list, task_id)
            task_instance.save_in_json(file, tasks_list)
        case 4:
            task_id = int(input("Task_id: "))
            tasks_list = task_instance.change_status(tasks_list, task_id, status_code=1)
            task_instance.save_in_json(file, tasks_list)
        case 5: 
            task_id = int(input("Task_id: "))
            tasks_list = task_instance.change_status(tasks_list, task_id, status_code=2)
            task_instance.save_in_json(file, tasks_list)
        case 6:
            print("Finished tasks: \n", ', '.join(task_instance.list_tasks(tasks_list, 1)))
        case 7:
            print("Tasks todo: \n", ', '.join(task_instance.list_tasks(tasks_list, 2)))
        case 8:
             print("In progress tasks: \n", ', '.join(task_instance.list_tasks(tasks_list, 3)))
        case default:
            print("Good bye!")



