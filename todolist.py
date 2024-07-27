to_do_list = []
def add_work():
    n = int(input("enter the number of tasks you want to add"))
    for i in range(n):
        task = input("enter the tasks")
        to_do_list.append(task)
    print(f"{n} tasks have been added to the todo list")
def view_todo_list():
    print(to_do_list[0:])
def remove_work():
    remove_task = int(input("enter the number of task which you want to remove"))
    if remove_task <= len(to_do_list):
        removed_task = to_do_list.pop(remove_task - 1)
    print("Task has been removed")
    print(to_do_list)
while True:
    print("""what you want to do 
        1.Add work in todo list
        2. View your todo list
        3.Remove the work from the todo list""")
    choice = input("enter your choice via 1/2/3")
    if choice == '1':
        add_work()
    elif choice == '2':
        view_todo_list()
    elif choice == '3':
        remove_work()
    else:
        pass
    
    repeat = input("do you want to continue 'y' for yes 'n' for no")
    if repeat == 'n':
        print("THANK YOU")
        break
        