"""this is the code to make a todo list in which we can add the work and remove the work and we can view the list of works."""

# initialize an empty list.
to_do_list = []


def add_work():
    """this is a function which is used to add the work to the list."""
    # take the input from the user about no of tasks they want to add.
    n = int(input("enter the number of tasks you want to add: "))
    # start a loop upto the no of inputs given by user.
    for i in range(n):
        # take the input of tasks the want to perform.
        task = input("enter the tasks: ")
        # append the tast variable to to_do_list.
        to_do_list.append(task)
        # then tell that n no of tasks have been inputed in the list
    print(f"{n} tasks have been added to the todo list")


def view_todo_list():
    """this function is defined to view the to do list"""
    print(to_do_list[0:])


def remove_work():
    """this function is defined to remove the existing work fro the todo list"""
    remove_task = int(input("enter the number of task which you want to remove: "))
    if remove_task <= len(to_do_list):
        removed_task = to_do_list.pop(remove_task - 1)
    print("Task has been removed")
    print(to_do_list)


while True:
    print(
        """what you want to do 
        1.Add work in todo list
        2. View your todo list
        3.Remove the work from the todo list"""
    )
    choice = input("enter your choice via 1/2/3: ")
    if choice == "1":
        add_work()
    elif choice == "2":
        view_todo_list()
    elif choice == "3":
        remove_work()
    else:
        pass

    repeat = input("do you want to continue 'y' for yes 'n' for no: ")
    if repeat == "n":
        print("THANK YOU")
        break
