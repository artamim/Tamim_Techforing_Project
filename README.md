# Tamim_Techforing_Project

Postman:
    To use the APIs, import each collection in the "Postman Collections" folder. 
    The instructions for using each of the requests are given inside the 
    body section of each of the requests.

App:
	--> If Pipenv is not installed, install it globally with:
	pip install pipenv
 
  --> Create and activate the virtual environment with Pipenv:
	pipenv shell
  
  --> Install all dependencies:
	pipenv install
 	--> If any problem arises while installing dependencies because of previous installations, use "pipenv --rm" and run "pipenv install" again.

  --> Apply migrations to set up the database: 
	python manage.py migrate

  --> Start the Django development server:
	python manage.py runserver

The Postgresql database used for this project is v16.6
