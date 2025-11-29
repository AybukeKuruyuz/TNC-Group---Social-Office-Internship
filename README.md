# To-Do List Application – User Guide  
**(TNC Group – Python Basic Programming Project)**

## Project Purpose
This is a console-based To-Do List application developed during my summer internship at TNC Group. The purpose of this application is to **manage daily tasks** quickly and simply. Users can add, list, edit, and delete tasks, with all data being stored in a **UTF-8 encoded text file** (`tasks.txt`).

## User Interface
Upon launching, the program displays a clear menu for the user to choose from:

### --- TO-DO LIST APPLICATION ---
1. **List Tasks**  
2. **Add New Task**  
3. **Modify Task**  
4. **Delete Task**  
5. **Exit**

To perform an action, type a number between **1–5** and press **Enter**. 

- **Invalid** or **empty input** will trigger an error message and the menu will be displayed again.

---

## Core Functions

### 1. **Add Task**
- Enter a new task.
- Empty input is **not allowed**.

### 2. **List Tasks**
- View all tasks with a number for easy reference.
- If there are no tasks, the program will display a message stating that the list is empty.

### 3. **Modify Task**
- Update a task by specifying its number.
- The program rejects **invalid task numbers** or **blank text** for updates.

### 4. **Delete Task**
- Remove a task by specifying its number.
- The program validates the input before deleting the task.

### 5. **Exit**
- Safely close the program.

---

## Data Persistence
- All changes (**add**, **edit**, **delete**) are **immediately saved** to the `tasks.txt` file.  
- If `tasks.txt` doesn’t exist, it will be **automatically created** when you first run the program.

---

## How to Run (Google Colab)
1. **Open the Google Colab link**:  
   [Open Colab Notebook](https://colab.research.google.com/drive/1Bt6nfYB4XdXofDoImtbXr9LYSYlIGYb8?usp=sharing)

2. **Run the code cell**:  
   Press **CTRL + SHIFT + Enter** or click the **Run Cell** button.

3. **Follow the on-screen menu** to manage your tasks.

---

## Notes
- All tasks are saved to `tasks.txt`. If the file doesn't exist, it will be created automatically when you run the program for the first time.
