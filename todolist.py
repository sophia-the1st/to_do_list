# to-do list
# add, view, delete tasks
import sys

OPTIONS = {
    1: "Add task",
    2: "View tasks",
    3: "Delete task",
}

TASKS = []

def main():
    open_app()
    
    while True:
        user_select = select_option()
        print(f"\n{OPTIONS[int(user_select)]}".upper().ljust(32, "="))
        match user_select:
            case "1": add_task()
            case "2": view_tasks()
            case "3": delete_tasks()
            case _: sys.exit()
        
        end = close_app()
        if end:
            print("\nThanks for using My To-Do List.")
            sys.exit()
    
    
def open_app():
    print("MY TO-DO LIST".center(32, "="), "\n")
        
        
def select_option():
    print("\nMENU:")
    for key, option in OPTIONS.items():
        print("{}).\t{}".format(key, option))
        
    valid_options = [str(key) for key in OPTIONS.keys()]
    while True:
        choice = input("\nWhat would you like to do? (1,2,3)\n")
        if choice in valid_options:
            return choice
        else:
            print("Invalid entry. Please enter", ",".join(valid_options), ".")
            
            
def add_task():
    task = input("\nEnter task:\n").strip()
    if task:
        TASKS.append(task.capitalize())
    else:
        print("\nTask cannot be empty.\n")
    
    
def view_tasks():
    if not TASKS:
        print("\nThere are no tasks to view.")
    else:
        print("\nTASKLIST:")
        for i, task in enumerate(TASKS, start=1):
            print(f"({i}).\t{task}")
            
            
def delete_tasks():
    if TASKS:
        print("\nTASKLIST:")
        for i, task in enumerate(TASKS, start=1):
            print(f"({i}). \t{task}")
    else:
        print("There are no tasks available.")
        return
        
    valid_options = [str(n) for n in range(1, len(TASKS) + 1)]
    valid_options.append("x")
    
    while True:
        to_delete = input("\nSelect task to delete:\n"
            "Enter 'X' to delete all tasks.\n").strip().casefold()
    
        if to_delete in valid_options:
            if to_delete.isdigit():
                TASKS.pop(int(to_delete) - 1)
                print("\nTask deleted successfully.\n")
                break
            elif to_delete == "x":
                TASKS.clear()
                print("\nAll tasks have been deleted successfully.\n")
                break
        else:
            print("\nInvalid entry. Please enter", ",".join(str(option) for option in valid_options))
        
        
def close_app():
    while True:
        close = input("\nAre you finished? (y/n)\n")
        valid_entries = ["y", "n"]
        if close.casefold() in valid_entries:
            return close.casefold() == "y"
        else:
            print("Please enter 'y' or 'n'.")
    
    
if __name__ == "__main__":
    main()