# Simple To-Do List Application
# Features: add, list, modify, and delete tasks.
# Tasks are stored in a UTF-8 encoded text file (tasks.txt).


tasks = []                # List that holds all tasks
file_name = "tasks.txt"   # Name of the file used for saving tasks

def download_from_file():
   # Reads saved tasks from the text file into the tasks list.
   # If the file does not exist, initializes an empty list and shows a message.
  global tasks
  try:
    with open(file_name, "r", encoding="utf-8") as file:
      tasks = [line.strip() for line in file.readlines()]

  except FileNotFoundError:
    tasks = []
    print("Task file is not found, new file is being created!")

  except Exception as e:
    print(f"There is a error!")
    print(f"Error type: {type(e).__name__}")
    print(f"Error Explanation: {e}")



def save_file():
   # Writes the current tasks list to the text file.
   # Called after every add/modify/delete operation.

  try:
    with open(file_name, "w", encoding="utf-8") as file:
      for task in tasks:
        file.write(task + "\n")

  except Exception as e:
    print("An error occurred while writing to the file!")
    print(f"Error type: {type(e).__name__}")
    print(f"Error Explanation: {e}")



def list_tasks():
   # Prints all tasks with numbering.
   # If the list is empty, informs the user that there are no tasks.

  if tasks == []:
    print("\nThere are no tasks yet.\n")

  else:
    print("")
    print("---- TASK LIST ----")
    for index, t in enumerate(tasks):
      print(f"{index+1}.{t}")

    print("-------------------")


def add_tasks():
    # Prompts the user for a new task and adds it to the list.
    # Rejects empty input and saves the updated list to the file.
    task_name = input("New Task: ")

    if task_name.strip() == "":
      print("Task cannot be empty! Please enter a valid task.")

    else:
      tasks.append(task_name)
      save_file()
      print(f"'{task_name}' is added on the tasks list!")
      print("Tasks saved successfully.")


def modify_tasks():
   # Allows the user to edit an existing task by number.
   # Validates input: non-empty new text and a valid task number.

  list_tasks()

  if tasks == []:
    return


  task_number_str = input("Number of the task you want to edit: ").strip()

  if task_number_str == "":
    print("Task number cannot be empty. Please enter a number.")
    return

  try:
    task_number = int(task_number_str)

  except ValueError:
    print("Please enter a valid number!")
    return

  if task_number < 1 or task_number > len(tasks):
    print(f"Invalid task number! Please choose a number between 1 and {len(tasks)}")
    return

  new_task = input("New task: ").strip()

  if new_task == "":
    print("Task cannot be empty! Please enter a valid task.")
    return

  print("")
  tasks[task_number - 1] = new_task
  save_file()


  print(f"Task {task_number} updated successfully!")
  print("Tasks saved successfully.")



def delete_tasks():
  # Deletes a task selected by number.
  # Checks for empty input, non-integer input, and out-of-range numbers.

  list_tasks()

  if tasks == []:
    return

  task_number_str = input("Number of the task you want to delete: ").strip()

  if task_number_str == "":
    print("Task number cannot be empty. Please enter a number.")
    return


  try:
    task_number = int(task_number_str)

  except ValueError:
    print("Please enter a valid number!")
    return


  if task_number < 1 or task_number > len(tasks):
    print(f"Invalid task number! Please choose a number between 1 and {len(tasks)}")
    return

  elif 1 <= task_number <= len(tasks):
    tasks.pop(task_number - 1)
    save_file()
    print("The task has been deleted.")
    print("Tasks saved successfully.")




def main_menu():
  # Entry point of the application.
  # Displays the menu and routes the user’s choice to the correct function.

  download_from_file()

  while True:
    print("\nWelcome to the To-Do List Application!\n")
    print("""--- TO-DO LIST APPLICATION ---
      1. List Tasks
      2. Add New Task
      3. Modify Task
      4. Delete Task
      5. Exit
    """)

    choice_str = input("Select the Action You Want to Perform: ").strip()

    if choice_str == "":    # User pressed Enter without typing a number: prompt again.
      print("You cannot make an empty selection. Please choose a number between 1 and 5.")
      continue

    try:
      choice = int(choice_str)

    except ValueError:
      print("Invalid input! Please enter a number between 1 and 5.")
      continue

    if choice == 1:
      list_tasks()

    elif choice == 2:
      add_tasks()

    elif choice == 3:
      modify_tasks()

    elif choice == 4:
      delete_tasks()

    elif choice == 5:
      print("Quitting the program...")
      break

# Runs the program
main_menu()
