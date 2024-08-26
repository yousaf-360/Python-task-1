from TaskManager import TaskManager

def display_menu():
    print('Task Manager')
    print('1. Add Task')
    print('2. Delete Task')
    print('3. Mark Task as Completed')
    print('4. List Tasks')
    print('5. Exit')

def handle_menu_options(manager: TaskManager):
    while True:
        display_menu()
        
        try:
            user_input = int(input('Choose an option: '))
            if user_input == 1:
                task_desc = input('Enter task description: ')
                manager.add_task(task_desc)
            elif user_input == 2:
                task_id = input('Enter task ID to delete: ')
                manager.delete_task(task_id)
            elif user_input == 3:
                task_id = input('Enter task ID to update: ')
                manager.update_status(task_id)
            elif user_input == 4:
                manager.print_tasks()
            elif user_input == 5:
                print('Exiting the program')
                manager.save_tasks()
                break
            else:
                print('Invalid value. Enter a valid value.')
        except ValueError:
            print("Invalid input. Please enter a number.")
        except Exception as e:
            print(f'Error: {e}')
