# iReporter

#### About
iReporter enables any/every citizen to bring any form of corruption to the notice of appropriate authorities and the general public.

#### Application test badges
[![Build Status](https://travis-ci.org/knightedge-technologies/ireporter.svg?branch=develop)](https://travis-ci.org/knightedge-technologies/ireporter) [![Maintainability](https://api.codeclimate.com/v1/badges/fe7cf9e8af48aa9cefcc/maintainability)](https://codeclimate.com/github/knightedge-technologies/ireporter/maintainability) [![Coverage Status](https://coveralls.io/repos/github/knightedge-technologies/ireporter/badge.svg?branch=develop)](https://coveralls.io/github/knightedge-technologies/ireporter?branch=develop)

#### Development setup

###### Step 1
- Project cloning command - ``git clone hhttps://github.com/knightedge-technologies/ireporter.git``

###### Step 2
- Install a virtual environment with the root directory
- Activate the virtual environment
- Install all the application dependencies with command ``pip install -r requirements.txt``

###### Step 3
- Make migrations for the application modules with the command ``python manage.py makemigrations``
- Migrate the modules of the different apps of the project to the database with the command ``python manage.py migrate``
- Run the Django project with the command ``python manage.py runserver``

#### Frontend

#### Backend
The backend is built in **Django**, which can be run by `python manage.py runserver` command in terminal.

##### Application endpoints
| Name and method			 | Endpoint					    | Description 				       |
| :------------------------- | :--------------------------- | :------------------------------- |
| User sign up (POST)		 | `/api/v1/accounts/signup/`	| For registering new accounts     |
| User login (POST)			 | `/api/v1/accounts/login/`	| For logging into the application |

##### Heroku Link
https://ireporter-dojo.herokuapp.com

##### Technologies used
- Git - For version control
- Pivotal Tracker - For Project management
- Travis CI - For continuous integration
- Coveralls - For test coverage reports
- Slack - As a collaboration tool
