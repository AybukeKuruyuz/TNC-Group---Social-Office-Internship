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

## How to Run (VS Code)
1. **Download and install VS Code**:  
   If you don't have **VS Code** installed, download and install it from [here](https://code.visualstudio.com/).

2. **Clone or open your project**:  
   Open your project folder in **VS Code**. If you're using **GitHub**, you can clone the repo using the **Source Control** panel in VS Code.

3. **Install Python Extension**:  
   Make sure you have the **Python extension** installed in **VS Code**. You can find it in the Extensions tab on the left sidebar.

4. **Run the program**:  
   Open the **`main.py`** file, and press **Ctrl + Shift + P**, then type **Python: Select Interpreter** to select your Python environment. After that, press **F5** or go to **Run > Start Debugging** to run the program.

5. **Follow the on-screen menu** to manage your tasks.

---

## Notes
- All tasks are saved to `tasks.txt`. If the file doesn't exist, it will be created automatically when you run the program for the first time.
