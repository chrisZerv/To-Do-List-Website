# Flask Todo List Application Website <img src=https://cdn-icons-png.flaticon.com/128/7692/7692809.png >

This is a simple yet powerful to-do list application built with Python and Flask. The application allows users to add tasks, set due dates, star important tasks, and reorder tasks via drag-and-drop. This project serves as a great introduction to web development using Flask and includes features that are commonly found in more complex task management tools.

## Features

- **Add Tasks**: Users can add new tasks to the list with optional due dates.
- **Toggle Completion**: Mark tasks as complete or incomplete.
- **Star Tasks**: Highlight important tasks by starring them, which moves them to the top of the list.
- **Drag-and-Drop Reordering**: Reorder tasks by dragging them up or down in the list.
- **Persistent Task Order**: The order of tasks is saved and maintained across page reloads.

## Prerequisites

Before you begin, ensure you have the following installed on your system:

- [Python 3.x](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/installation/)

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/flask_todo.git
cd flask_todo
```

### 2. Create a Virtual Environment (Optional but Recommended)

Creating a virtual environment will help isolate dependencies for this project:

```bash
python -m venv venv
source venv/bin/activate   # On Windows use `venv\Scripts\activate`
```

### 3. Install Dependencies

Install the necessary Python packages using `pip`:

```bash
pip install Flask
```

### 4. Run the Application

Start the Flask development server:

```bash
python app.py
```

Open your web browser and navigate to:

```
`http://localhost:5000/`
```

### 5. Using the Application

- **Add a Task**: Use the input field to enter a task and optionally add a due date. Click the "Add" button to save the task.
- **Mark Task as Complete/Incomplete**: Click the "Toggle" button next to a task to mark it as complete or incomplete.
- **Star a Task**: Click the "Star" button to highlight important tasks, which will be moved to the top of the list.
- **Reorder Tasks**: Drag tasks using the handle on the left side to reorder them in the list.
- **Delete a Task**: Click the "Delete" button to remove a task from the list.



## Future Improvements

Here are a few ideas for future enhancements:

- **User Authentication**: Allow multiple users to maintain their own to-do lists.
- **Persistent Storage**: Integrate a database (e.g., SQLite, PostgreSQL) to store tasks persistently.
- **Task Categories**: Add the ability to categorize tasks (e.g., work, personal).
- **Notifications**: Implement due date notifications via email or on-screen alerts.

## Contributing

If you'd like to contribute to this project, please fork the repository and create a pull request with your changes. Contributions are welcome!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
