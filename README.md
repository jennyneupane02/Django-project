Django Task Tracker
This is a simple Django web app I built for my assignment. It lets a user add tasks and view their own task list. The tasks are stored using Django sessions so each user sees their own data. The project has two pages: a homepage that shows the list and an add page with a form to submit a new task.

How to Run :

Code :
git clone https://github.com/jennyneupane02/Django-project

cd Django-project

pip install django

python manage.py migrate

python manage.py runserver

Open the app at:

http://127.0.0.1:8000/

Features:

Two pages (list + add)

Django Form with validation

Sessions for user-specific data

Template inheritance

Static CSS file

Redirects using HttpResponseRedirect and reverse()
