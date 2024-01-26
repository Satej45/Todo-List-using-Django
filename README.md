# Django Todo List App

A simple Todo List application built with Django.

## Features

- Add, edit, and delete tasks.
- Mark tasks as completed or incomplete.
- Organize tasks by categories.
- User-friendly interface.

## Technologies Used

- [Django](https://www.djangoproject.com/) - A high-level Python web framework.
- [SQLite](https://www.sqlite.org/) - A lightweight and embedded database.
- [Bootstrap](https://getbootstrap.com/) - A front-end framework for styling.

## Setup Instructions

1. Clone the repository:

   ```bash
   git clone https://github.com/Satej45/Todo-List-using-Django.git
   cd django-todo-list

Install dependencies:
pip install -r requirements.txt

Apply migrations:
python manage.py migrate

Create a superuser account (optional but recommended):
python manage.py createsuperuser

Run the development server:
python manage.py runserver
Open your browser and navigate to http://localhost:8000 to access the application.

Usage
Access the admin interface to manage tasks and categories: http://localhost:8000/admin/
Use the task list interface to add, edit, and manage tasks: http://localhost:8000/tasks/
