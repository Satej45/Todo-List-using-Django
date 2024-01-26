Cloning from GitHub Repository
To get started with the Todo_List Django Web App, you can clone the repository from GitHub using the following steps:

Clone the repository:

git clone https://github.com/NAHIAN-19/Todo-List-Django.git
Navigate to the project folder:

cd Todo_List
Create and activate a virtual environment (optional but recommended):

py -m venv myworld
myworld\Scripts\activate.bat
Install project dependencies:

pip install -r requirements.txt
Run database migrations:

python manage.py makemigrations
python manage.py migrate
Create a superuser account (for admin access)

python manage.py createsuperuser
Start the development server:

python manage.py runserver
Open your web browser and go to http://localhost:8000 to access the Todo_List Django Web App.

Installing from ZIP Archive
Download the zip file Todo_List.zip
Extract the ZIP archive to your desired location on your computer.
Navigate to the project folder: --Right click on the project folder and 'Copy as path' and paste the path like below
cd project_path
Continue with steps 3 to 8 from the "Cloning from GitHub Repository" section to set up and run the project
